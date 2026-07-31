import "./App.css";

function App() {
  return (
    <div className="App">
      <header
        style={{
          minHeight: "100vh",
          background: "#0f172a",
          color: "#fff",
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          padding: "40px",
        }}
      >
        <div style={{ maxWidth: "800px", textAlign: "center" }}>
          <h1 style={{ fontSize: "3rem", marginBottom: "10px" }}>
            🚀 DevOps Lab Project 2
          </h1>

          <h2 style={{ color: "#38bdf8" }}>
            Deploy React Application using Docker
          </h2>

          <p
            style={{
              marginTop: "25px",
              fontSize: "18px",
              lineHeight: "1.8",
            }}
          >
            This React application has been containerized using Docker as part
            of the DevOps Lab coursework. The project demonstrates application
            packaging, container deployment, and execution inside an isolated
            Docker environment.
          </p>

          <div
            style={{
              marginTop: "40px",
              textAlign: "left",
              background: "#1e293b",
              padding: "25px",
              borderRadius: "12px",
            }}
          >
            <h3>📌 Technologies Used</h3>

            <ul style={{ lineHeight: "2" }}>
              <li>⚛ React.js</li>
              <li>🐳 Docker</li>
              <li>🌐 Git & GitHub</li>
              <li>⚙ DevOps Fundamentals</li>
            </ul>
          </div>

          <div
            style={{
              marginTop: "35px",
              padding: "20px",
              border: "2px solid #38bdf8",
              borderRadius: "10px",
            }}
          >
            <h3>✅ Project Status</h3>
            <p>Application Successfully Running Inside Docker Container</p>
          </div>

          <p
            style={{
              marginTop: "45px",
              color: "#94a3b8",
            }}
          >
            Submitted by <strong>Bishwajeet Sahoo</strong>
            <br />
            PRN: <strong>23070122073</strong>
          </p>
        </div>
      </header>
    </div>
  );
}

export default App;