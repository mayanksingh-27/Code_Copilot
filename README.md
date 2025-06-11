#  Code Copilot

**Code Copilot** is an AI-powered assistant that provides **code autocompletion suggestions** for C programming. It uses a custom-trained **LSTM (Long Short-Term Memory)** neural network to predict the next token or line in a code snippet.

---

##  Features

- **LSTM-based Code Autocompletion**  
  Predicts likely next tokens or code lines for C language based on user input.

- 💻 **Frontend (React)**  
  - Simple user interface to type code  
  - Displays autocomplete suggestions in real time

- 🔧 **Backend**  
  - **Spring Boot (Java)**: API gateway that forwards requests to the ML model  
  - **Flask (Python)**: Hosts the LSTM model and serves predictions

---

## 🏗️ Folder Structure
Code_Copilot/
├── code-assistant-frontend/       # React frontend
│   └── src/components/            # UI components
│       ├── CodeInput.js
│       └── SuggestionList.js
│
├── Code_rec_srpingboot_Backend/   # Spring Boot backend
│   └── src/main/java/com/codeassistant/
│       ├── controller/            # REST controller
│       └── service/               # Handles Flask API calls
│
├── Code_Recommendation_Flask/     # Flask + LSTM model
│   └── app.py                     # Loads and serves the model
---

## 🧪 LSTM Model Details

The model is trained on token sequences of C programming code, learning patterns like loop structures, conditional blocks, and common syntax.

- **Model Architecture**
  - Embedding Layer
  - LSTM Layers
  - Dense Output Layer
- **Input**: tokenized and padded sequences of code
- **Output**: predicted next token or code line

---

## 🔌 How to Run

Clone the repository and navigate into it:


git clone https://github.com/mayanksingh-27/Code_Copilot.git
cd Code_Copilot
cd Code_Recommendation_Flask
python app.py
cd Code_rec_srpingboot_Backend
./mvnw spring-boot:run
cd code-assistant-frontend
npm install
npm start
