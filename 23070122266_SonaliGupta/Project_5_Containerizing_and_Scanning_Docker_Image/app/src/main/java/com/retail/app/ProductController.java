package com.retail.app;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class ProductController {

    @GetMapping("/")
    public String home() {
        return "Retail Storefront Portal is Online";
    }

    @GetMapping("/health")
    public String health() {
        return "UP";
    }
}