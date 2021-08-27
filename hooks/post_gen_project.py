import subprocess

subprocess.call(["git", "init"])
subprocess.call(
    "git remote add origin https://huggingface.co/datasets/{{cookiecutter.hf_hub_username}}/{{cookiecutter.repo_name}}".split()
)
subprocess.call("git pull origin main".split())
subprocess.call(["git", "add", "."])
subprocess.call(["git", "commit", "-m", "Initial commit"])
