from pathlib import Path
from typing import Literal

import pandas as pd


def get_project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_netflix_data(
    dataset: Literal["raw", "processed"] = "processed",
) -> pd.DataFrame:
    filenames = {
        "raw": "data/raw/Dataset.csv",
        "processed": "data/processed/netflix_cleaned_dataset.csv",
    }
    dataset_path = get_project_root() / filenames[dataset]
    return pd.read_csv(dataset_path)


def prepare_country_credits(df: pd.DataFrame) -> tuple[pd.DataFrame, int]:
    unknown_labels = {"", "unknown country", "unknown", "not given", "na", "n/a"}
    country_titles = (
        df[["show_id", "country"]]
        .copy()
        .assign(
            country=lambda data: data["country"]
            .astype("string")
            .str.split(r"\s*,\s*")
        )
        .explode("country")
    )
    country_titles["country"] = country_titles["country"].str.strip()

    is_unknown = (
        country_titles["country"].isna()
        | country_titles["country"].str.lower().isin(unknown_labels)
    )
    valid_title_count = country_titles.loc[~is_unknown, "show_id"].nunique()
    unknown_title_count = df["show_id"].nunique() - valid_title_count
    country_titles = (
        country_titles.loc[~is_unknown]
        .drop_duplicates(subset=["show_id", "country"])
        .reset_index(drop=True)
    )
    return country_titles, unknown_title_count


def prepare_genre_credits(df: pd.DataFrame) -> pd.DataFrame:
    genre_titles = (
        df[["show_id", "listed_in"]]
        .dropna(subset=["listed_in"])
        .assign(
            genre=lambda data: data["listed_in"]
            .astype("string")
            .str.split(r"\s*,\s*")
        )
        .explode("genre")
    )
    genre_titles["genre"] = genre_titles["genre"].str.strip()
    return (
        genre_titles.loc[genre_titles["genre"].notna() & genre_titles["genre"].ne("")]
        .drop_duplicates(subset=["show_id", "genre"])
        .reset_index(drop=True)
    )
