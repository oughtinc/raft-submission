---
benchmark: raft
type: prediction-upload
---

# RAFT submissions for {{cookiecutter.repo_name}}
## Making a submission

To make a submission, there are three main steps:

1. Generate predictions on the unlabeled test set of each task
2. Validate the predictions are compatible with the evaluation framework
3. Push the predictions to the Hub!

See the instructions below for more details.

> ⚠️  To prevent overfitting to the public leaderboard, we only evaluate **one submission per week**. You can push predictions to the Hub as many times as you wish, but we will only evaluate the most recent commit in a given week. 
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
├── medical_subdomain_of_clinical_notes
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

