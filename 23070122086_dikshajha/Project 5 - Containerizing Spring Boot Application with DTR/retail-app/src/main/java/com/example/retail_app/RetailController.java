package com.example.retail_app;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class RetailController {

    @GetMapping("/")
    public String home() {
        return "Retail Application is running successfully in Docker!";
    }
}
