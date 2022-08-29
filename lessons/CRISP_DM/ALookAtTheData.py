import pandas as pd
import numpy as np
from collections import defaultdict
import ALookAtTheDataSolns as s # come back to here

def display_gif(fn):
    return f'<img src="{fn}">'


## A Look at the Data
# Question 1
def check_rows_cols(num_rows, num_cols):
    '''
    INPUT:
    num_rows - int the number of rows in df
    num_cols - int the number of cols in df

    This function will print a statement related to whether or not you provided the correct number of rows and columns of the dataset.
    '''
    if num_rows == s.num_rows:
        print(f"Nice job there are {num_rows} rows in the dataset!")
    else:
        print("That doesn't look like what we were expecting for the number of rows.")

    if num_cols == s.num_cols:
        print(f"Nice job there are {num_cols} columns in the dataset!")
    else:
        print("That doesn't look like what we were expecting for the number of columns.")


# Question 2
def no_null_cols(no_nulls):
    '''
    INPUT:
    no_nulls - a set of columns with no missing values

    This function will print a statement related to whether or not you provided the correct set of columns with no missing values
    '''
    if no_nulls == s.no_nulls:
        print("Nice job that looks right!")
        return display_gif('https://bit.ly/2K9X0gD')
    else:
        print(
            f"That doesn't look like for the set of no nulls.  There should be {len(s.no_nulls)} columns in your list"
        )

        return display_gif('https://bit.ly/2Hog74V')
        

# Question 3
def most_missing_cols(most_missing_cols):
    '''
    INPUT:
    most_missing_cols - a set of columns with more than 75% of the values in the column missing

    This function will print a statement related to whether or not you provided the correct set of columns with more than 75% of the values in the column missing
    '''
    if most_missing_cols == s.most_missing_cols:
        print("Nice job that looks right!")
    else:
        print(
            f"That doesn't look like for the set of most nulls.  There should be {len(s.most_missing_cols)} columns in your list"
        )

















