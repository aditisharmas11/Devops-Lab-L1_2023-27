# Git Feature Branching Model

## Branch Structure

main
|
+-- develop
    |
    +-- feature/user-auth
    +-- feature/payment
    +-- feature/dashboard

## Branch Roles

### main

The main branch contains stable and release-ready code.

### develop

The develop branch is used as the integration branch for ongoing development.

### Feature Branches

Feature branches are created from develop for individual features.

Examples:

- feature/user-auth
- feature/payment
- feature/dashboard

## Development Flow

develop
|
+-- create feature branch
|
+-- develop and commit
|
+-- merge feature into develop
|
+-- release stable work to main

## Example Commands

git checkout develop
git checkout -b feature/user-auth
git add .
git commit -m "Implement user authentication"
git checkout develop
git merge feature/user-auth