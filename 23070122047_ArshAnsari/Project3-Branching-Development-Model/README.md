# Project 3 — Branching Development Model

**Student:** Arsh Ansari | **PRN:** 23070122047

GitFlow on a tiny Node app (`app/`) so the team can see how work moves from feature branches into production.

Nested git history lives in `app/` (also published as [branching-demo-app](https://github.com/arshansari2880-alt/branching-demo-app) with `main`, `develop`, `feature/login`, `release/1.0`, `hotfix/critical-bug`, and tags `v1.0.0` / `v1.0.1`).

## Branch structure

| Branch | Role |
|--------|------|
| `main` | Stable / production |
| `develop` | Integration |
| `feature/login` | Isolated feature, merged into `develop` |
| `release/1.0` | Cut from `develop`, merged into `main` and `develop` |
| `hotfix/critical-bug` | Urgent patch from `main`, merged into `main` and `develop` |

![Branches created](./screenshots/01-branches-created.txt)

## Feature → develop

Created `feature/login` from `develop`, added the login feature, merged with `--no-ff`.

![Feature merged to develop](./screenshots/02-feature-merged-to-develop.txt)

## Release → main

Created `release/1.0`, bumped version to `1.0.0`, merged into `main` (tag `v1.0.0`) and back into `develop`.

![Release merged to main](./screenshots/03-release-merged-to-main.txt)

## Hotfix → main and develop

Created `hotfix/critical-bug` from `main`, merged into both `main` (tag `v1.0.1`) and `develop`.

![Hotfix merged](./screenshots/04-hotfix-merged.txt)

## Full graph

```powershell
git log --graph --oneline --decorate --all
```

![Branch graph](./screenshots/05-branch-graph.txt)
