# lab.py


import os
import io
from pathlib import Path
import pandas as pd
import numpy as np


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def trick_me():
    d = [
        ["Don", "Won", 1],
        ["Bon", "Two", 2],
        ["Kon", "Three", 3],
        ["Son", "Four", 4],
        ["Won", "Five", 5]
    ]
    tricky_1 = pd.DataFrame(
        columns=['Name', 'Name', 'Age'], data=d
    )

    tricky_1.to_csv('tricky_1.csv', index=False)

    tricky_2 = pd.read_csv('tricky_1.csv')

    return 3


def trick_bool():
    return [10, 6, 13]


# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


def population_stats(df):
    num_nonnull = df.count()
    prop_nonnull = num_nonnull / len(df)
    num_distinct = df.nunique()
    prop_distinct = num_distinct / num_nonnull

    stats_df = pd.DataFrame({
        'num_nonnull': num_nonnull,
        'prop_nonnull': prop_nonnull,
        'num_distinct': num_distinct,
        'prop_distinct': prop_distinct
    })
    return stats_df

# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


def most_common(df, N=10):
    results = {}
    
    for col in df.columns:
        values = df[col].value_counts()

        top_n = values.iloc[:N]

        values_list = top_n.index.tolist()
        counts_list = top_n.values.tolist()

        if len(values_list) < N:
            n_missing = N - len(values_list)
            values_list.extend([np.nan] *n_missing)
            counts_list.extend([np.nan] * n_missing)

        results[f'{col}_values'] = values_list
        results[f'{col}_counts'] = counts_list
    return pd.DataFrame(results)



# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


def super_hero_powers(powers):
    names = powers['hero_names']
    powers_df = powers.drop(columns="hero_names")

    power_counts = powers_df.sum(axis = 1)
    most_powers_index = power_counts.idxmax()
    hero_most_powers = names.loc[most_powers_index]

    flying_heroes = powers_df[powers_df["Flight"] == True]
    flying_power_counts = flying_heroes.sum(axis = 0)
    flying_power_counts - flying_power_counts.drop("Flight")
    common_flyer_power = flying_power_counts.idxmax()

    single_power_mask = (power_counts == 1)
    single_power_heroes = powers_df[single_power_mask]
    single_power_counts = single_power_heroes.sum(axis = 0)
    common_single_power = single_power_counts.idxmax()

    return [hero_most_powers, common_flyer_power, common_single_power]

# ---------------------------------------------------------------------
# QUESTION 5
# ---------------------------------------------------------------------


def clean_heroes(heroes):
    return heroes.replace(['-', -99], np.nan)


# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


def super_hero_stats():
    return ["Onslaught","George Lucas", "bad", "Marvel Comics", "NBC - Heroes", "Groot"]


# ---------------------------------------------------------------------
# QUESTION 7
# ---------------------------------------------------------------------


def clean_universities(df):
    df_clean = df.copy()

    df_clean['institution'] = df_clean['institution'].str.replace('\n', ', ', regex=False)
    df_clean['broad_impact'] = df_clean['broad_impact'].astype(int)

    nation_splits = df_clean['national_rank'].str.split(', ', expand=True)
    df_clean['nation'] = nation_splits[0]
    df_clean['national_rank_cleaned'] = nation_splits[1].astype(int)

    replacements = {
        'USA': 'United States',
        'UK': 'United Kingdom',
        'Czechia': 'Czech Republic'
    }
    df_clean['nation'] = df_clean['nation'].replace(replacements)

    df_clean = df_clean.drop(columns=['national_rank'])

    df_clean['is_public'] = df_clean['control'] == 'Public'
    
    return df_clean

def university_info(cleaned):
    state_counts = cleaned["state"].value_counts()
    qualifying_states = state_counts[state_counts >= 3].index

    df_states = cleaned[cleaned["state"].isin(qualifying_states)]
    lowest_score_state = df_states.groupby("state")["score"].mean().idxmin()

    top_100_world = cleaned[cleaned['world_rank'] <= 100]
    top_100_faculty_count = (top_100_world['quality_of_faculty'] <= 100).sum()
    prop_faculty = top_100_faculty_count / len(top_100_world)

    state_groups = cleaned.dropna(subset=['state']).groupby('state')
    def find_majority_private(group):
        return (~group["is_public"]).mean() >= 0.5
    num_states_private = state_groups.apply(find_majority_private).sum()

    rank_1_national = cleaned[cleaned['national_rank_cleaned'] == 1]
    worst_inst_index = rank_1_national['world_rank'].idxmax()
    worst_inst_name = rank_1_national.loc[worst_inst_index, 'institution']

    return [lowest_score_state, prop_faculty, int(num_states_private), worst_inst_name]



