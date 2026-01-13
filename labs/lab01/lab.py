# lab.py


from pathlib import Path
import io
import pandas as pd
import numpy as np
np.set_printoptions(legacy='1.21')



# ---------------------------------------------------------------------
# QUESTION 0
# ---------------------------------------------------------------------


def consecutive_ints(ints):
    if len(ints) == 0:
        return False

    for k in range(len(ints) - 1):
        diff = abs(ints[k] - ints[k+1])
        if diff == 1:
            return True

    return False


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def median_vs_mean(nums):
    nums_mean = sum(nums) / len(nums)
    
    if len(nums) % 2 == 0:
        nums_median = (nums[int(len(nums) / 2)] + nums[int(len(nums) / 2) + 1]) / 2 
    else:
        nums_median = nums[int(len(nums) / 2)]
    
    if nums_median <= nums_mean:
        return True
    else:
        return False



# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


def n_prefixes(s, n):
    out = ""
    for i in range(n, 0, -1):
        out += s[0:i]
    return out


# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


def exploded_numbers(ints, n):
    max_val = max(ints) + n
    width = len(str(max_val))
    
    result = []
    
    for num in ints:
    
        current_range = range(num - n, num + n + 1)
        
        exploded_str = " ".join([str(num).zfill(width) for num in current_range])
        
        result.append(exploded_str)
        
    return result






# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


def last_chars(fh):
    result = ""
    for line in fh:
        result += line[-2]
        
    return result



# ---------------------------------------------------------------------
# QUESTION 5
# ---------------------------------------------------------------------


def add_root(A):
    indices = np.arange(len(A))
    return A + np.sqrt(indices)


def where_square(A):
    square_roots = np.sqrt(A)
    return square_roots % 1 == 0

# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


def filter_cutoff_loop(matrix, cutoff):
    rows, cols = matrix.shape
    valid_col_index = []

    for col in range(cols):
        col_sum = 0
        for row in range(rows):
            col_sum += matrix[row][col]

        col_mean = col_sum / rows
        if col_mean > cutoff:
            valid_col_index.append(col)
    
    output = []
    for row in range(rows):
        new_row = []
        for col in valid_col_index:
            new_row.append(matrix[row][col])
        output.append(new_row)

    return np.array(output)


# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


def filter_cutoff_np(matrix, cutoff):
    col_means = np.mean(matrix, axis = 0)
    boolean = col_means > cutoff

    return matrix[:, boolean]


# ---------------------------------------------------------------------
# QUESTION 7
# ---------------------------------------------------------------------


def growth_rates(A):
    initial_days = A[:-1]
    final_days = A[1:]

    growth_rate = (final_days - initial_days) / initial_days

    return np.round(growth_rate, 2)

def with_leftover(A):
    left_over_money = 20 % A
    total_savings = np.cumsum(left_over_money)

    can_buy = total_savings >= A

    valid_days = np.where(can_buy)[0]

    if valid_days.size == 0:
        return -1
    
    return valid_days[0]


# ---------------------------------------------------------------------
# QUESTION 8
# ---------------------------------------------------------------------


def salary_stats(salary):
    num_players = salary.shape[0]

    num_teams = salary['Team'].nunique()

    total_salary = salary["Salary"].sum()

    highest_salary = salary.sort_values("Salary", ascending = False).iloc[0]["Player"]

    lakers = salary[salary['Team'] == 'Los Angeles Lakers']
    avg_los = round(lakers["Salary"].mean(), 2)

    sorted_ascending = salary.sort_values('Salary', ascending=True)
    fifth_player = sorted_ascending.iloc[4]
    fifth_lowest = f"{fifth_player['Player']}, {fifth_player['Team']}"

    def get_last_name(full_name):
        parts = full_name.split()
        suffixes = ['Jr.', 'Sr.', 'II', 'III', 'IV']

        if parts[-1] in suffixes:
            return parts[-2]
        return parts[-1]
    last_names = salary['Player'].apply(get_last_name)
    duplicates = last_names.duplicated().any()

    highest_team_name = salary.sort_values("Salary", ascending = False).iloc[0]["Team"]
    total_highest = salary[salary['Team'] == highest_team_name]['Salary'].sum()


    return pd.Series({
        'num_players': num_players,
        'num_teams': num_teams,
        'total_salary': total_salary,
        'highest_salary': highest_salary,
        'avg_los': avg_los,
        'fifth_lowest': fifth_lowest,
        'duplicates': duplicates,
        'total_highest': total_highest
    })

# ---------------------------------------------------------------------
# QUESTION 9
# ---------------------------------------------------------------------


def parse_malformed(fp):
    with open(fp, 'r') as f:
        lines = f.readlines()
    
    parsed_data = []
    
    for line in lines[1:]:
        clean_line = line.strip().replace('"', '')

        parts = clean_line.split(',')

        cleaned_parts = [p.strip() for p in parts if p.strip() != '']
        
        if len(cleaned_parts) == 6:
            first, last= cleaned_parts[0], cleaned_parts[1]
            weight, height = float(cleaned_parts[2]), float(cleaned_parts[3])
            
            geo = f"{cleaned_parts[4]},{cleaned_parts[5]}"
            
            parsed_data.append([first, last, weight, height, geo])
            
    df = pd.DataFrame(parsed_data, columns=['first', 'last', 'weight', 'height', 'geo'])
    
    return df
