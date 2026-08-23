const express = require("express");

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

app.get("/", (req, res) => {
    res.json({
        service: "payment-service",
        status: "running",
        message: "Payment Service is running successfully"
    });
});

app.get("/payments", (req, res) => {
    res.json({
        service: "payment-service",
        payments: [
            {
                id: 1,
                orderId: 1001,
                amount: 75000,
                status: "SUCCESS"
            },
            {
                id: 2,
                orderId: 1002,
                amount: 30000,
                status: "SUCCESS"
            }
        ]
    });
});

app.get("/health", (req, res) => {
    res.json({
        service: "payment-service",
        status: "healthy"
    });
});

app.listen(PORT, () => {
    console.log(`Payment Service running on port ${PORT}`);
});