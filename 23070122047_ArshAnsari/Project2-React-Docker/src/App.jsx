import "./App.css";

const projects = [
  { name: "TW1.1", detail: "Git workflow, feature branch, merge conflict" },
  { name: "TW1.2", detail: "Jira Scrum board and issue tracking" },
  { name: "TW1.3", detail: "Flask Docker image + Jenkins freestyle job" },
  { name: "Project 1", detail: "Jenkins pipeline that builds a Docker image" },
  { name: "Project 2", detail: "This React app served from Nginx in Docker" },
  { name: "Project 4", detail: "Distributed Maven pipeline on two Jenkins slaves" },
];

export default function App() {
  return (
    <main className="page">
      <header className="hero">
        <p className="kicker">DevOps Lab L1 · 2023–27</p>
        <h1>Arsh Ansari</h1>
        <p className="prn">PRN 23070122047</p>
        <p className="lede">
          React application running inside a Docker container, served by Nginx
          on port 80.
        </p>
      </header>
      <section className="grid">
        {projects.map((project) => (
          <article key={project.name} className="card">
            <h2>{project.name}</h2>
            <p>{project.detail}</p>
          </article>
        ))}
      </section>
    </main>
  );
}
