# Netflix Content Analysis

This project explores a Netflix titles dataset using Python, Pandas, and Jupyter notebooks. It covers data cleaning, catalog composition, country credits, release-year trends, ratings and genres, and a consolidated business insights report.

## Project contents

| Notebook | Analysis |
| --- | --- |
| [`01_data_cleaning.ipynb`](./notebooks/01_data_cleaning.ipynb) | Load, inspect, clean, and export the dataset |
| [`02_content_type_analysis.ipynb`](./notebooks/02_content_type_analysis.ipynb) | Compare Movies and TV Shows |
| [`03_country_analysis.ipynb`](./notebooks/03_country_analysis.ipynb) | Rank countries by title credits |
| [`04_release_year_trends.ipynb`](./notebooks/04_release_year_trends.ipynb) | Explore title counts by release year |
| [`05_content_rating_genre_analysis.ipynb`](./notebooks/05_content_rating_genre_analysis.ipynb) | Examine ratings and genre labels |
| [`06_netflix_business_insights.ipynb`](./notebooks/06_netflix_business_insights.ipynb) | Consolidated interactive dashboards and executive summary |

## Dataset

- Raw input: [`data/raw/Dataset.csv`](./data/raw/Dataset.csv)
- Cleaned output: [`data/processed/netflix_cleaned_dataset.csv`](./data/processed/netflix_cleaned_dataset.csv)

The cleaned dataset contains 8,790 titles and 10 columns. Country and genre fields may contain multiple credits for a title. In the country analysis, titles with an unknown-country placeholder are excluded from country rankings.

## Getting started

Use Python 3.12 or a compatible Python version, then create and activate a virtual environment and install the project dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

On Windows PowerShell, activate the environment with:

```powershell
.\.venv\Scripts\Activate.ps1
```

Start JupyterLab from the repository root:

```bash
jupyter lab
```

Open the notebooks under `notebooks/` and run their cells in order. Most analysis notebooks load the cleaned CSV from `data/processed/`; run the data-cleaning notebook first if you need to regenerate that file from the raw input.

## Shared helpers

[`src/helpers.py`](./src/helpers.py) provides common dataset loading and country/genre credit preparation functions used by the notebooks. This keeps file paths and multi-credit handling consistent across analyses.

## Current snapshot highlights

- Movies: 6,126 (69.7%); TV Shows: 2,664 (30.3%).
- The most frequent release year in the dataset is 2018, with 1,146 titles.
- The most frequent `date_added` year is 2019, with 2,016 titles.
- The United States has the most recorded country credits (3,240), followed by India (1,057) and the United Kingdom (638).
- TV-MA is the most frequent rating (3,205 titles); the most common genre labels are International Movies (2,752), Dramas (2,426), and Comedies (1,674).

## Interpretation notes

These results describe the supplied catalog snapshot, not Netflix's live catalog, production output, regional availability, viewing behavior, or audience demand. The latest `date_added` value is September 25, 2021, so 2021 is a partial year. Titles with multiple country or genre credits can contribute to multiple category counts; those totals therefore overlap.