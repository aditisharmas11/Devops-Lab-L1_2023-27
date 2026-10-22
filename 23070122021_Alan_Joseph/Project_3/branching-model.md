# Branching Model

| Branch | Created from | Merged into | Naming |
|---|---|---|---|
| main | - | - | `main` |
| develop | main | - | `develop` |
| feature | develop | develop | `feature/<short-name>` |
| release | develop | main and develop | `release/<version>` |
| hotfix | main | main and develop | `hotfix/<version>` |

## Rules
1. Never commit directly to `main` or `develop`.
2. Every merge into `main` or `develop` uses `--no-ff` so the history shows the feature boundary.
3. Tag every release on `main` (`v1.0.0`, `v1.0.1`, ...).
4. Delete feature, release and hotfix branches after they are merged.
5. A hotfix must be merged back into `develop` so the fix is not lost in the next release.
