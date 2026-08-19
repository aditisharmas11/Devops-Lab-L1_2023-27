package com.devops.retail_app.controller;

import com.devops.retail_app.model.Product;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Arrays;
import java.util.List;

@RestController
@RequestMapping("/api/products")
public class ProductController {

    @GetMapping
    public List<Product> getProducts() {

        return Arrays.asList(
                new Product(
                        1,
                        "Laptop",
                        "Electronics",
                        59999
                ),
                new Product(
                        2,
                        "Smartphone",
                        "Electronics",
                        29999
                ),
                new Product(
                        3,
                        "Office Chair",
                        "Furniture",
                        8999
                ),
                new Product(
                        4,
                        "Wireless Headphones",
                        "Accessories",
                        4999
                )
        );
    }

    @GetMapping("/health")
    public String health() {
        return "Retail application is running";
    }
}
