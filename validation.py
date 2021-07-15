from datasets import load_dataset
from pathlib import Path


def main():
    tasks = ["safety_or_not"]

    # check that all the expected files exist
    prediction_files = list(Path(".").glob("*.csv"))
    mismatched_files = set(tasks).symmetric_difference(set([f.stem for f in prediction_files]))
    if mismatched_files:
        raise ValueError(f"Incorrect number of files! Expected {len(tasks)} files, but got {len(prediction_files)}.")

    # check we can load the dataset for each task
    load_errors = []
    for task in tasks:
        try:
            dset = load_dataset("../raft_submission", task)
        except Exception as e:
            load_errors.append(e)

    if load_errors:
        raise ValueError(f"Could not load predictions! Errors: {load_errors}")


if __name__ == "__main__":
    main()
