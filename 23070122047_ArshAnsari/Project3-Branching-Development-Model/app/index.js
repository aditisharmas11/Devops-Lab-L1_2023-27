const http = require("http");
const VERSION = "1.0.1";
const FEATURES = ["home", "login"];
const server = http.createServer((_req, res) => {
  res.writeHead(200, { "Content-Type": "application/json" });
  res.end(JSON.stringify({ app: "branching-demo-app", prn: "23070122047", version: VERSION, features: FEATURES, hotfix: "critical-bug-fixed" }));
});
server.listen(3000, () => console.log("listening on 3000"));
