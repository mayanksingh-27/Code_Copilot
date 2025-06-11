from flask import Flask, request, jsonify
import re
import random
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Tokenizer for C-like code
def tokenize_c_code(code):
    token_pattern = r'\w+|==|<=|>=|!=|[{}();,+*/<>=-]'
    return re.findall(token_pattern, code)
    
templates = [
    "for ( int  = 0 ;  <  ;  ++ ) { printf ( \"%d\" ,  ) ; }",
    "while (  <  ) {  ++ ; }",
    "do {  -- ; } while (  > 0 ) ;"
]

subs = {'': ['i', 'j', 'k', 'sum', 'count', 'temp', 'value', 'result']}

def generate_tokens(template):
    tokens = template.split()
    return [random.choice(subs.get(tok, [tok])) for tok in tokens]

def generate_dataset(n=5000):  # 🔼 More samples
    data = []
    for _ in range(n):
        t = random.choice(templates)
        tokens = generate_tokens(t)
        data.append(tokens)
    return data

dataset = generate_dataset(1000)

# --------------------------------------
# 2. Prepare Input/Output for LSTM
# --------------------------------------
X, y = [], []
for tokens in dataset:
    for i in range(1, len(tokens)):
        X.append(" ".join(tokens[:i]))
        y.append(tokens[i])

tokenizer = Tokenizer()
tokenizer.fit_on_texts(X)
X_seq = tokenizer.texts_to_sequences(X)
X_seq = pad_sequences(X_seq, maxlen=20)

label_encoder = LabelEncoder()
y_enc = label_encoder.fit_transform(y)

# --------------------------------------
# 3. Train LSTM Model
# --------------------------------------
model = Sequential([
    Embedding(input_dim=len(tokenizer.word_index)+1, output_dim=64, input_length=10),
    LSTM(64),
    Dense(len(label_encoder.classes_), activation='softmax')
])
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

X_train, X_test, y_train, y_test = train_test_split(X_seq, y_enc, test_size=0.2)
model.fit(X_train, y_train, epochs=5, batch_size=32, validation_data=(X_test, y_test))

# --------------------------------------
# 4. Flask App with LSTM Endpoint
# --------------------------------------
app = Flask(__name__)

@app.route('/autocomplete', methods=['POST'])
def autocomplete_api():
    data = request.get_json()
    code = data.get("code", "")
    tokens = tokenize_c_code(code)
    input_seq = tokenizer.texts_to_sequences([" ".join(tokens)])
    input_seq = pad_sequences(input_seq, maxlen=10)

    probs = model.predict(input_seq)[0]
    top_indices = np.argsort(probs)[-5:][::-1]
    top_tokens = label_encoder.inverse_transform(top_indices)

    suggestions = [{"token": tok, "probability": float(round(probs[i], 4))} for tok, i in zip(top_tokens, top_indices)]
    return jsonify({"suggestions": suggestions})

if __name__ == '__main__':
    app.run(debug=True)