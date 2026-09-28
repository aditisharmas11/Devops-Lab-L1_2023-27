# Git Branching Development Model (GitFlow)

## Branch Hierarchy & Rules
1. **main**: Production-ready code tagged with release versions (v1.0.0, v1.1.0).
2. **develop**: Central integration branch for ongoing feature aggregation.
3. **feature/*: Dedicated branches created from develop for individual features.
4. **release/*: Release candidate stabilization branch before merging to main and develop.
5. **hotfix/*: Direct patches branched from main for urgent production bug fixes.
