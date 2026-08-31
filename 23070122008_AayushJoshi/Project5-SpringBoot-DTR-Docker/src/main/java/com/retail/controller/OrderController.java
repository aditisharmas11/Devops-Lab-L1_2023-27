package com.retail.controller;

import com.retail.model.Order;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

@RestController
@RequestMapping("/api/orders")
public class OrderController {

    private final List<Order> orders = new ArrayList<>(Arrays.asList(
        new Order(1L, 1L, "Riya Sharma", 1, 49999.00),
        new Order(2L, 3L, "Amit Patel", 3, 2097.00)
    ));

    @GetMapping
    public List<Order> getAllOrders() {
        return orders;
    }

    @GetMapping("/{id}")
    public Order getOrderById(@PathVariable Long id) {
        return orders.stream()
            .filter(o -> o.getId().equals(id))
            .findFirst()
            .orElseThrow(() -> new RuntimeException("Order not found: " + id));
    }

    @PostMapping
    public Order placeOrder(@RequestBody Order order) {
        order.setId((long) (orders.size() + 1));
        order.setStatus("PENDING");
        orders.add(order);
        return order;
    }

    @PatchMapping("/{id}/status")
    public Order updateStatus(@PathVariable Long id, @RequestParam String status) {
        Order order = getOrderById(id);
        order.setStatus(status);
        return order;
    }
}
