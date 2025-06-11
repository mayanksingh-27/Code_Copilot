package com.codeassistant.dto;

import lombok.Data;
import java.util.List;

@Data
public class AutocompleteResponse {
    private List<Suggestion> suggestions;

    @Data
    public static class Suggestion {
        private String token;
        private double probability;
    }
}