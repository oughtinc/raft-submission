# RAFT Submission Template

Welcome to the [RAFT benchmark](https://raft.elicit.org/)! RAFT is a few-shot classification benchmark that tests language models:

- across multiple domains (lit review, tweets, customer interaction, etc.)
- on economically valuable classification tasks (someone inherently cares about the task)
- in a setting that mirrors deployment (50 examples per task, info retrieval allowed, hidden test set)

This repository can be used to generate a template so you can submit your predictions for evaluation on [the leaderboard](https://huggingface.co/spaces/ought/raft-leaderboard).

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

## Submitting to the leaderboard

To make a submission to the [leaderboard](https://huggingface.co/spaces/ought/raft-leaderboard), there are three main steps:

1. Generate predictions on the unlabeled test set of each task
2. Validate the predictions are compatible with the evaluation framework
3. Push the predictions to the Hub!

See the instructions below for more details.

### Rules

1. To prevent overfitting to the public leaderboard, we only evaluate **one submission per week**. You can push predictions to the Hub as many times as you wish, but we will only evaluate the most recent commit in a given week. 
2. Transfer or meta-learning using other datasets, including further pre-training on other corpora, is allowed.
3. Use of unlabeled test data is allowed, as is it always available in the applied setting. For example, further pre-training using the unlabeled data for a task would be permitted.
4. Systems may be augmented with information retrieved from the internet, e.g. via automated web searches.


### Submission file format

For each task in RAFT, you should create a CSV file called `predictions.csv` with your model's predictions on the unlabeled test set. Each file should have exactly 2 columns:

* ID (string)
* Label (string)

See the dummy predictions in the `data` folder for examples of the expected format. Each `predictions.csv` file should be stored in the task's subfolder in `data` and at the end you should have something like the following:

```
data
├── ade_corpus_v2
│   ├── predictions.csv
│   └── task.json
├── banking_77
│   ├── predictions.csv
│   └── task.json
├── neurips_impact_statement_risks
│   ├── predictions.csv
│   └── task.json
├── one_stop_english
│   ├── predictions.csv
│   └── task.json
├── overruling
│   ├── predictions.csv
│   └── task.json
├── semiconductor_org_types
│   ├── predictions.csv
│   └── task.json
├── systematic_review_inclusion
│   ├── predictions.csv
│   └── task.json
├── tai_safety_research
│   ├── predictions.csv
│   └── task.json
├── terms_of_service
│   ├── predictions.csv
│   └── task.json
├── tweet_eval_hate
│   ├── predictions.csv
│   └── task.json
└── twitter_complaints
    ├── predictions.csv
    └── task.json
```

### Validate your submission

To ensure that your submission files are correctly formatted, run the following command from the root of the repository:

```
python cli.py validate
```

If everything is correct, you should see the following message:

```
All submission files validated! ✨ 🚀 ✨
Now you can make a submission 🤗
```

### Push your submission to the Hugging Face Hub!

The final step is to commit your files and push them to the Hub:

```bash
git add .
git commit -m "Some commit message"
git push -f origin HEAD:main
```
