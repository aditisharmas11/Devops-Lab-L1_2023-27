package com.retail.controller;

import com.retail.model.Product;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

@RestController
@RequestMapping("/api/products")
public class ProductController {

    private final List<Product> products = new ArrayList<>(Arrays.asList(
        new Product(1L, "Smart TV 55\"", "Electronics", 49999.00, 25),
        new Product(2L, "Running Shoes", "Footwear", 3499.00, 100),
        new Product(3L, "Organic Coffee 500g", "Groceries", 699.00, 200),
        new Product(4L, "Denim Jacket", "Apparel", 2199.00, 60),
        new Product(5L, "Yoga Mat", "Sports", 1299.00, 80)
    ));

    @GetMapping
    public List<Product> getAllProducts() {
        return products;
    }

    @GetMapping("/{id}")
    public Product getProductById(@PathVariable Long id) {
        return products.stream()
            .filter(p -> p.getId().equals(id))
            .findFirst()
            .orElseThrow(() -> new RuntimeException("Product not found: " + id));
    }

    @PostMapping
    public Product addProduct(@RequestBody Product product) {
        product.setId((long) (products.size() + 1));
        products.add(product);
        return product;
    }

    @GetMapping("/category/{category}")
    public List<Product> getByCategory(@PathVariable String category) {
        return products.stream()
            .filter(p -> p.getCategory().equalsIgnoreCase(category))
            .toList();
    }
}
