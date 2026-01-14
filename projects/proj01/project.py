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
    ...


# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


def process_labs(grades):
    ...


# ---------------------------------------------------------------------
# QUESTION 5
# ---------------------------------------------------------------------


def labs_overall(processed):
    ...


# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


def total_points(grades):
    ...


# ---------------------------------------------------------------------
# QUESTION 7
# ---------------------------------------------------------------------


def final_grades(total):
    ...

def letter_proportions(total):
    ...


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
