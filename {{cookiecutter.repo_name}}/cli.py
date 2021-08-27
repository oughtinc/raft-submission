from click.utils import echo
import typer
from datasets import get_dataset_config_names, load_dataset
from pathlib import Path
import subprocess

app = typer.Typer()


@app.command()
def install():
    typer.echo("Installing dependencies ...")
    try:
        p = subprocess.run(
            "pip install --upgrade pip".split(),
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
            check=True,
            encoding="utf-8",
        )
    except subprocess.CalledProcessError as exc:
        raise EnvironmentError(exc.stderr)

    try:
        p = subprocess.run(
            "pip install --upgrade -r requirements.txt".split(),
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
            check=True,
            encoding="utf-8",
        )
    except subprocess.CalledProcessError as exc:
        raise EnvironmentError(exc.stderr)

    typer.echo("Success!")


@app.command()
def validate():
    tasks = get_dataset_config_names("ought/raft")

    # Check that all the expected files exist
    prediction_files = list(Path("data").rglob("*.csv"))
    mismatched_files = set(tasks).symmetric_difference(set([f.parent.name for f in prediction_files]))
    if mismatched_files:
        raise ValueError(f"Incorrect number of files! Expected {len(tasks)} files, but got {len(prediction_files)}.")

    # Check we can load the dataset for each task
    load_errors = []
    for task in tasks:
        try:
            _ = load_dataset("../{{cookiecutter.repo_name}}", task)
        except Exception as e:
            load_errors.append(e)

    if load_errors:
        raise ValueError(f"Could not load predictions! Errors: {load_errors}")

    typer.echo("All submission files validated! ✨ 🚀 ✨")
    typer.echo("Now you can make a submission 🤗")


if __name__ == "__main__":
    app()
