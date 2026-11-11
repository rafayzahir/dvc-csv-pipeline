# DVC CSV Pipeline

Copies a CSV from `data/source/` to `data/destination/` using a DVC pipeline,
then pushes it to a DVC remote automatically with GitHub Actions.

## Folder structure
```
dvc-csv-pipeline/
├── .github/workflows/dvc-pipeline.yml  # CI: dvc repro + dvc push
├── .dvc/config                         # DVC remote configuration
├── .dvcignore                          # Files DVC ignores
├── data/
│   ├── source/sample.csv               # Input CSV (tracked by Git)
│   └── destination/                    # Output CSV (tracked by DVC)
├── src/copy_csv.py                     # Copy script
├── dvc.yaml                            # Pipeline definition
├── params.yaml                         # Source/destination paths
├── requirements.txt
└── README.md
```

## Run locally
```bash
git init && pip install -r requirements.txt
dvc repro   # copy CSV
dvc push    # push to remote
```

## Use with GitHub
1. Push this repo to GitHub (branch `main`).
2. Edit `.dvc/config` to a real remote (S3, GDrive...) and add secrets.
   The default `/tmp/dvc-remote` only lives during the CI run;
   the CSV is also uploaded as a workflow artifact.
