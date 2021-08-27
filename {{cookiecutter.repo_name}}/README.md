---
benchmark: raft
type: prediction-upload
---

# RAFT submissions for {{cookiecutter.repo_name}}
## How to make a submission

The following steps will help you get started with submitting to the RAFT benchmark!

### Create an account on the Hugging Face Hub

First you have to create an account on the Hugging Face website and you can sign up [here](https://huggingface.co/join) if you haven't already!

### Create a template repository

Next create a template repository by first installing `cookiecutter`

```
pip install cookiecutter
```

and then running

```
cookiecutter https://github.com/oughtinc/raft_submission.git
```

## Install the dependencies

Create a virtual env!

```
cd my-raft-submissions
python cli.py install
```

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

