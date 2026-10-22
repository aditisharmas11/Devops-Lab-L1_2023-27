# Project 3 - Branching Development Model

A Git branching model (based on git-flow) that helps a team integrate work quickly and safely.

- `main` - production-ready code, every release is tagged
- `develop` - integration branch for the next release
- `feature/*` - new work, branched from and merged back into `develop`
- `release/*` - release preparation, merged into `main` (tagged) and `develop`
- `hotfix/*` - urgent fixes branched from `main`, merged into both `main` and `develop`

See `branching-model.md` for the full rules.

## Try it
```bash
pip install -r requirements.txt
pytest -v                          # run the app's tests
python setup_git_history.py demo   # builds a demo repo that follows the model
cd demo && git log --oneline --graph --all
```
