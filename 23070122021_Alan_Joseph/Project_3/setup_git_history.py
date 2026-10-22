#!/usr/bin/env python3
"""Builds a demo Git repository that follows the branching model in branching-model.md."""
import os
import shutil
import subprocess
import sys

LAB_DIR = os.path.dirname(os.path.abspath(__file__))
REPO = sys.argv[1] if len(sys.argv) > 1 else "demo"


def git(*args):
    subprocess.run(["git", *args], cwd=REPO, check=True)


def write(filename, content):
    with open(os.path.join(REPO, filename), "w") as f:
        f.write(content)


def commit(message):
    git("add", ".")
    git("commit", "-m", message)


def main():
    if os.path.exists(REPO):
        shutil.rmtree(REPO)
    os.makedirs(REPO)
    git("init", "-b", "main")
    git("config", "user.email", "student@example.com")
    git("config", "user.name", "Lab Student")

    # 1. main: initial release
    shutil.copy(os.path.join(LAB_DIR, "app.py"), REPO)
    shutil.copy(os.path.join(LAB_DIR, "test_app.py"), REPO)
    commit("Initial commit")
    git("tag", "v1.0.0")

    # 2. develop is created from main
    git("checkout", "-b", "develop")

    # 3. feature branch from develop, merged back with --no-ff
    git("checkout", "-b", "feature/greeting")
    write("app.py", open(os.path.join(LAB_DIR, "app.py")).read().replace(
        "if __name__",
        'def greet(name):\n    return f"Hello, {name}!"\n\n\nif __name__'))
    commit("Add greet() function")
    git("checkout", "develop")
    git("merge", "--no-ff", "-m", "Merge feature/greeting into develop", "feature/greeting")
    git("branch", "-d", "feature/greeting")

    # 4. release branch from develop
    git("checkout", "-b", "release/1.1.0")
    write("app.py", open(os.path.join(REPO, "app.py")).read().replace(
        '__version__ = "1.0.0"', '__version__ = "1.1.0"'))
    commit("Bump version to 1.1.0")
    git("checkout", "main")
    git("merge", "--no-ff", "-m", "Merge release/1.1.0 into main", "release/1.1.0")
    git("tag", "v1.1.0")
    git("checkout", "develop")
    git("merge", "--no-ff", "-m", "Merge release/1.1.0 back into develop", "release/1.1.0")
    git("branch", "-d", "release/1.1.0")

    # 5. hotfix branch from main
    git("checkout", "-b", "hotfix/1.1.1", "main")
    write("app.py", open(os.path.join(REPO, "app.py")).read().replace(
        '__version__ = "1.1.0"', '__version__ = "1.1.1"'))
    commit("Hotfix: bump version to 1.1.1")
    git("checkout", "main")
    git("merge", "--no-ff", "-m", "Merge hotfix/1.1.1 into main", "hotfix/1.1.1")
    git("tag", "v1.1.1")
    git("checkout", "develop")
    git("merge", "--no-ff", "-m", "Merge hotfix/1.1.1 into develop", "hotfix/1.1.1")
    git("branch", "-d", "hotfix/1.1.1")

    git("checkout", "develop")
    print(f"Demo repository created in ./{REPO}")


if __name__ == "__main__":
    main()
