package com.arshansari.retail;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;
import java.util.Map;

@RestController
public class StoreController {

    @GetMapping("/")
    public Map<String, Object> home() {
        return Map.of(
            "company", "Arsh Retail Labs",
            "prn", "23070122047",
            "message", "Retail store API running in Docker"
        );
    }

    @GetMapping("/catalog")
    public List<Map<String, Object>> catalog() {
        return List.of(
            Map.of("sku", "RET-101", "name", "Wireless Mouse", "price", 799),
            Map.of("sku", "RET-204", "name", "USB-C Hub", "price", 1499),
            Map.of("sku", "RET-330", "name", "Laptop Sleeve", "price", 599)
        );
    }

    @GetMapping("/health")
    public Map<String, String> health() {
        return Map.of("status", "UP");
    }
}
