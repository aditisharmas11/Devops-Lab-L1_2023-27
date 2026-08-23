const express = require("express");

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

app.get("/", (req, res) => {
    res.json({
        service: "user-service",
        status: "running",
        message: "User Service is running successfully"
    });
});

app.get("/users", (req, res) => {
    res.json({
        service: "user-service",
        users: [
            {
                id: 1,
                name: "Alice",
                email: "alice@example.com"
            },
            {
                id: 2,
                name: "Bob",
                email: "bob@example.com"
            }
        ]
    });
});

app.get("/health", (req, res) => {
    res.json({
        service: "user-service",
        status: "healthy"
    });
});

app.listen(PORT, () => {
    console.log(`User Service running on port ${PORT}`);
});