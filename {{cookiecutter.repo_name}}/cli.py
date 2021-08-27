import subprocess
from pathlib import Path

import pandas as pd
import typer
from click.utils import echo
from datasets import get_dataset_config_names, load_dataset

CSV_SCHEMA = {
    "banking_77": (5000, 2),
    "overruling": (2350, 2),
    "semiconductor_org_types": (449, 2),
    "ade_corpus_v2": (5000, 2),
    "twitter_complaints": (3399, 2),
    "neurips_impact_statement_risks": (150, 2),
    "systematic_review_inclusion": (2244, 2),
    "terms_of_service": (5000, 2),
    "tai_safety_research": (1639, 2),
    "one_stop_english": (518, 2),
    "tweet_eval_hate": (2966, 2),
}

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

    # Check all files have the expected shape (number of rows, number of columns)
    # TODO(lewtun): Add a check for the IDs per file
    shape_errors = []
    column_errors = []
    for prediction_file in prediction_files:
        df = pd.read_csv(prediction_file)
        incorrect_shape = df.shape != CSV_SCHEMA[prediction_file.parent.name]
        if incorrect_shape:
            shape_errors.append(prediction_file)
        incorrect_columns = sorted(df.columns) != ["ID", "Label"]
        if incorrect_columns:
            column_errors.append(prediction_file)

    if shape_errors:
        raise ValueError(f"Incorrect CSV shapes in files: {shape_errors}")

    if column_errors:
        raise ValueError(f"Incorrect CSV columns in files: {column_errors}")

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
