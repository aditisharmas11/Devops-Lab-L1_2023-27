# Branching Model and Git Workflow

This repository demonstrates a lightweight, fast-integration branching model based on the **Feature Branch Workflow** (similar to GitHub Flow). This model is designed to help our team integrate work faster, reduce merge conflicts, and maintain a stable production codebase.

## The Branching Model

### 1. `main` Branch
- **Purpose**: The `main` branch is the source of truth. It contains the official, production-ready release history.
- **Rules**: 
  - NEVER commit directly to `main`.
  - All code in `main` must be deployable and tested.
  - Work is integrated into `main` via Pull Requests (PRs) or Merge Requests (MRs).

### 2. Feature Branches (`feature/*`)
- **Purpose**: Used for developing new features.
- **Naming Convention**: `feature/<issue-number>-<short-description>` (e.g., `feature/123-user-login`).
- **Workflow**:
  - Branch off from: `main`
  - Merge back into: `main`
  - Push frequently to your remote feature branch to share progress.

### 3. Bugfix Branches (`bugfix/*` or `hotfix/*`)
- **Purpose**: Used to fix bugs. `bugfix/*` is typically for non-critical bugs found in development, while `hotfix/*` is for critical production issues.
- **Naming Convention**: `bugfix/<issue-number>-<short-description>` or `hotfix/<issue-number>-<description>`.
- **Workflow**:
  - Branch off from: `main`
  - Merge back into: `main`

---

## Workflow Steps for Faster Integration

To ensure fast work integration and minimize conflicts, follow this cycle for every new task:

### Step 1: Sync with Main
Before starting any new work, ensure your local `main` branch is up to date with the remote repository.
```bash
git checkout main
git pull origin main
```

### Step 2: Create a New Branch
Create a new branch for your feature or bugfix.
```bash
git checkout -b feature/user-authentication
```

### Step 3: Work and Commit Frequently
Make small, logical commits. Small commits are easier to review and revert if something goes wrong.
```bash
git add .
git commit -m "feat: add initial login form UI"
```

### Step 4: Keep Your Branch Updated (Rebase or Merge)
If `main` has moved forward while you were working, bring those changes into your branch to resolve conflicts early.
```bash
git fetch origin
git rebase origin/main
# OR
git merge origin/main
```

### Step 5: Push and Open a Pull Request
Once your work is complete and tested, push your branch and open a Pull Request against `main`.
```bash
git push -u origin feature/user-authentication
```

### Step 6: Review and Merge
- Have team members review your code.
- Once approved and CI checks pass, merge the Pull Request into `main`.
- Delete your feature branch after merging to keep the repository clean.

---

## Best Practices for the Team

- **Keep PRs Small**: Aim for PRs that can be reviewed in under 15 minutes. Small PRs mean faster integration.
- **Don't Let Branches Stagnate**: The longer a branch lives, the harder it is to merge. Aim to integrate your work back to `main` within a few days.
- **Use Meaningful Commit Messages**: A good commit message explains *why* a change was made.
- **Automated Testing**: Rely on CI/CD to run tests automatically on your feature branches before merging.
