package com.codeassistant.service;

import com.codeassistant.dto.*;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.*;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class CodeService {

    private final RestTemplate restTemplate = new RestTemplate();

    @Value("${flask.base-url}")
    private String flaskUrl;

    public AutocompleteResponse autocomplete(AutocompleteRequest request) {
        String url = flaskUrl + "/autocomplete";
        //ResponseBody is expected to have body of AutocompleteResponse
        ResponseEntity<AutocompleteResponse> response = restTemplate.postForEntity(url, request, AutocompleteResponse.class);
        return response.getBody();
    }

    public AutocorrectResponse autocorrect(AutocorrectRequest request) {
        String url = flaskUrl + "/autocorrect";
        ResponseEntity<AutocorrectResponse> response = restTemplate.postForEntity(url, request, AutocorrectResponse.class);
        return response.getBody();
    }
}