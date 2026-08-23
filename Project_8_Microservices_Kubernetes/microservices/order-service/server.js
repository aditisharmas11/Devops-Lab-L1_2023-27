const express = require("express");
const http = require("http");

const app = express();
const PORT = process.env.PORT || 3000;

const USER_SERVICE_URL =
    process.env.USER_SERVICE_URL || "http://user-service:3000";

const PRODUCT_SERVICE_URL =
    process.env.PRODUCT_SERVICE_URL || "http://product-service:3000";

const PAYMENT_SERVICE_URL =
    process.env.PAYMENT_SERVICE_URL || "http://payment-service:3000";

app.use(express.json());

function callService(url) {
    return new Promise((resolve, reject) => {
        http.get(url, (response) => {
            let data = "";

            response.on("data", chunk => {
                data += chunk;
            });

            response.on("end", () => {
                try {
                    resolve(JSON.parse(data));
                } catch (error) {
                    reject(error);
                }
            });
        }).on("error", reject);
    });
}

app.get("/", (req, res) => {
    res.json({
        service: "order-service",
        status: "running",
        message: "Order Service is running successfully"
    });
});

app.get("/orders", (req, res) => {
    res.json({
        service: "order-service",
        orders: [
            {
                id: 1001,
                userId: 1,
                productId: 101,
                status: "CONFIRMED"
            },
            {
                id: 1002,
                userId: 2,
                productId: 102,
                status: "CONFIRMED"
            }
        ]
    });
});

app.get("/health", (req, res) => {
    res.json({
        service: "order-service",
        status: "healthy"
    });
});

app.get("/order-summary", async (req, res) => {
    try {
        const users = await callService(`${USER_SERVICE_URL}/users`);
        const products = await callService(`${PRODUCT_SERVICE_URL}/products`);
        const payments = await callService(`${PAYMENT_SERVICE_URL}/payments`);

        res.json({
            service: "order-service",
            status: "success",
            message: "Successfully communicated with all dependent microservices",
            users: users,
            products: products,
            payments: payments
        });
    } catch (error) {
        console.error(error);

        res.status(500).json({
            service: "order-service",
            status: "failed",
            message: "Unable to communicate with dependent services",
            error: error.message
        });
    }
});

app.listen(PORT, () => {
    console.log(`Order Service running on port ${PORT}`);
});