# RAFT Submission Template

Welcome to the RAFT benchmark! This repository can be used to generate a template so you can submit your predictions for evaluation on [the leaderboard](https://huggingface.co/spaces/ought/raft-leaderboard).

## Quickstart

### 0. Create an account and repository on the Hugging Face Hub

First create an account on the Hugging Face Hub and you can sign up [here](https://huggingface.co/join) if you haven't already! Next sign in to the Hub and create a new **_private dataset_** by selecting _New Dataset_ under your profile icon. Pick a name for repository and make sure you select the _Private_ button if you want to keep your predictions secret (recommended!). The GIF below also goes through these steps.

![](raft-dataset.gif)

### 1. Create a template repository on your machine

The next step is to create a template repository on your local machine that contains various files and a CLI to help you validate and submit your predictions. You can run the following commands to create the repository:

```bash
# Install the Python cookiecutter library if you don't have it
pip install cookiecutter
# Create the template repository
cookiecutter https://github.com/oughtinc/raft_submission.git
```

This will ask you to specify your Hub username, the name of the repository, and also the name in CamelCase format which is needed for the dataset loading script:

```
hf_hub_username [<huggingface>]:
repo_name [<my-raft-submissions>]:
camelcase_repo_name [<MyRaftSubmissions>]:
```

This will create a Git repository from which you push your predictions to the Hub.

### 2. Install the dependencies

The final step is to install the project's dependencies. We recommend creating a Python virtual environment for the project, e.g. with Anaconda:

```bash
# Navigate to the template repository
cd my-raft-submissions
# Create and activate a virtual environment
conda create -n raft python=3.8 && conda activate raft
# Install dependencies
python cli.py install
```

That's it! You're now all set to start generating predictions - see the instructions below on how to submit them to the Hub.
## Making a submission
### Generate predictions

Store them in `data`

### Validate your submissions

```
python cli.py validate
```

### Push your predictions to the Hugging Face Hub!

```
python cli.py submit
```