package com.devops.project5;

import java.util.List;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.server.ResponseStatusException;

@RestController
public class ProductController {

    private static final List<Product> PRODUCTS = List.of(
            new Product(1L, "Running Shoes", 79.99),
            new Product(2L, "Backpack", 49.50),
            new Product(3L, "Water Bottle", 12.00));

    @GetMapping("/")
    public String home() {
        return "Welcome to the Retail Web App";
    }

    @GetMapping("/api/products")
    public List<Product> listProducts() {
        return PRODUCTS;
    }

    @GetMapping("/api/products/{id}")
    public Product getProduct(@PathVariable Long id) {
        return PRODUCTS.stream()
                .filter(p -> p.id().equals(id))
                .findFirst()
                .orElseThrow(() -> new ResponseStatusException(HttpStatus.NOT_FOUND, "Product not found"));
    }
}
