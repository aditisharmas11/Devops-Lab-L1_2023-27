const express = require("express");

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

app.get("/", (req, res) => {
    res.json({
        service: "product-service",
        status: "running",
        message: "Product Service is running successfully"
    });
});

app.get("/products", (req, res) => {
    res.json({
        service: "product-service",
        products: [
            {
                id: 101,
                name: "Laptop",
                price: 75000
            },
            {
                id: 102,
                name: "Mobile Phone",
                price: 30000
            },
            {
                id: 103,
                name: "Headphones",
                price: 5000
            }
        ]
    });
});

app.get("/health", (req, res) => {
    res.json({
        service: "product-service",
        status: "healthy"
    });
});

app.listen(PORT, () => {
    console.log(`Product Service running on port ${PORT}`);
});