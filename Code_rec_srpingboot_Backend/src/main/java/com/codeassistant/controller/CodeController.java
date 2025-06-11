package com.codeassistant.controller;

import com.codeassistant.dto.*;
import com.codeassistant.service.CodeService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api")
@CrossOrigin(origins = "*")
public class CodeController {

    @Autowired
    private CodeService codeService;

    @PostMapping("/autocomplete")
    public AutocompleteResponse autocomplete(@RequestBody AutocompleteRequest request) {
        return codeService.autocomplete(request);
    }

    @PostMapping("/autocorrect")
    public AutocorrectResponse autocorrect(@RequestBody AutocorrectRequest request) {
        return codeService.autocorrect(request);
    }

    @GetMapping("/test")
    public String test() {
        return "Controller is working!";
    }
}