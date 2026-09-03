# Project 3: Git Branching Model

## Objective

Define and demonstrate a feature-based Git branching model for organized software development.

## Branching Model

The project uses `main` as the stable branch and `develop` as the integration branch.

Feature development is carried out in separate feature branches created from `develop`.

```text
main
|
+-- develop
    |
    +-- feature/user-auth
    +-- feature/payment
    +-- feature/dashboard