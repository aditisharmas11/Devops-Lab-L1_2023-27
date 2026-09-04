package com.example;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
public class RetailApplication {

    @GetMapping("/")
    public String home() {
        return "Retail Web Application is running successfully!";
    }

    public static void main(String[] args) {
        SpringApplication.run(RetailApplication.class, args);
    }
}