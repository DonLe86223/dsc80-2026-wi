# project.py


import pandas as pd
import numpy as np
from pathlib import Path
import plotly.express as px


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def get_assignment_names(grades):
    columns = grades.columns

    return {
        'lab': [c for c in columns if 'lab' in c and " - " not in c],
        'project': [c for c in columns if 'project' in c and 'checkpoint' not in c and ' - ' not in c],
        'midterm': [c for c in columns if 'Midterm' in c and " - " not in c],
        'final': [c for c in columns if 'Final' in c and " - " not in c],
        'disc': [c for c in columns if 'discussion' in c and " - " not in c],
        'checkpoint': [c for c in columns if 'checkpoint' in c and " - " not in c]
    }


# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


def projects_overall(grades):
    projects = [c for c in grades.columns if 'project' in c and 'checkpoint' not in c and " - " not in c]
    project_nums = [p for p in projects if "_" not in p]
    project_scores = pd.DataFrame(index=grades.index)
    for project in project_nums:
        project_parts = [p for p in projects if p == project or p == f"{project}_free_response"]
        
        points_earned = sum(grades[part].fillna(0) for part in project_parts)

        points_in_total = sum(grades[f"{part} - Max Points"] for part in project_parts)

        project_scores[project] = points_earned / points_in_total

    return project_scores.mean(axis = 1)



# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


def lateness_penalty(col):
    def get_time(time):
        if not isinstance(time, str):
            return 0.0
        
        parts = time.split(":")
        hours = int(parts[0])
        minutes = int(parts[1])
        seconds = int(parts[2])
        return hours + (minutes / 60) + (seconds / 3600)
    
    hours = col.apply(get_time)
    bins = [-float('inf'), 2, 168, 336, float('inf')]
    labels = [1.0, 0.9, 0.7, 0.4]
    return pd.cut(hours, bins=bins, labels=labels).astype(float)


# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


def process_labs(grades):
    lab_cols = [c for c in grades.columns if 'lab' in c and ' - ' not in c]

    lab_cols.sort()

    new_df = pd.DataFrame(index=grades.index)

    for lab in lab_cols:
        score_col = lab
        max_col = f"{lab} - Max Points"
        lateness_col = f"{lab} - Lateness (H:M:S)"

        late_multiplier = lateness_penalty(grades[lateness_col])

        raw_score = grades[score_col].fillna(0)

        max_points = grades[max_col]

        new_df[lab] = (raw_score * late_multiplier) / max_points

    return new_df




# ---------------------------------------------------------------------
# QUESTION 5
# ---------------------------------------------------------------------


def labs_overall(processed):
    total_sum = processed.sum(axis=1)
    min_score = processed.min(axis=1)

    adjusted = total_sum - min_score

    num_labs = processed.shape[1] - 1

    return adjusted / num_labs



# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


def total_points(grades):
    processed_labs = process_labs(grades)
    lab_score = labs_overall(processed_labs)

    project_score = projects_overall(grades)


    def get_simple_category_score(word):
        # Find columns containing the keyword (excluding metadata)
        cols = [c for c in grades.columns if word in c and ' - ' not in c]
        
        # Calculate score (Earned / Max) for each assignment
        # We create a temporary DataFrame to hold these ratios
        scores_df = pd.DataFrame(index=grades.index)
        for c in cols:
            earned = grades[c].fillna(0)
            possible = grades[f"{c} - Max Points"]
            scores_df[c] = earned / possible
            
        # Return the average across all assignments in this category
        return scores_df.mean(axis=1)
    
    checkpoint_score = get_simple_category_score('checkpoint')
    discussion_score = get_simple_category_score('discussion')

    midterm_score = grades['Midterm'].fillna(0) / grades['Midterm - Max Points']
    
    final_score = grades['Final'].fillna(0) / grades['Final - Max Points']

    total = (
        0.20 * lab_score +
        0.30 * project_score +
        0.025 * checkpoint_score +
        0.025 * discussion_score +
        0.15 * midterm_score +
        0.30 * final_score
    )
    return total


# ---------------------------------------------------------------------
# QUESTION 7
# ---------------------------------------------------------------------


def final_grades(total):
    def get_letter(score):
        if score >= 0.9:
            return 'A'
        elif score >= 0.8:
            return 'B'
        elif score >= 0.7:
            return 'C'
        elif score >= 0.6:
            return 'D'
        else:
            return 'F'
        
    return total.apply(get_letter)

def letter_proportions(total):
    letters = final_grades(total)
    proportions = letters.value_counts(normalize=True)
    return proportions


# ---------------------------------------------------------------------
# QUESTION 8
# ---------------------------------------------------------------------


def raw_redemption(final_breakdown, question_numbers):
    ...
    
def combine_grades(grades, raw_redemption_scores):
    ...


# ---------------------------------------------------------------------
# QUESTION 9
# ---------------------------------------------------------------------


def z_score(ser):
    ...
    
def add_post_redemption(grades_combined):
    ...


# ---------------------------------------------------------------------
# QUESTION 10
# ---------------------------------------------------------------------


def total_points_post_redemption(grades_combined):
    ...
        
def proportion_improved(grades_combined):
    ...


# ---------------------------------------------------------------------
# QUESTION 11
# ---------------------------------------------------------------------


def section_most_improved(grades_analysis):
    ...
    
def top_sections(grades_analysis, t, n):
    ...


# ---------------------------------------------------------------------
# QUESTION 12
# ---------------------------------------------------------------------


def rank_by_section(grades_analysis):
    ...


# ---------------------------------------------------------------------
# QUESTION 13
# ---------------------------------------------------------------------


def letter_grade_heat_map(grades_analysis):
    ...
