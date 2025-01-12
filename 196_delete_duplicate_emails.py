# 196. Delete Duplicate Emails

# Write a SQL query to delete all duplicate email entries in a table named Person, keeping only unique emails based on its smallest Id.

# # Write your MySQL query statement below
# DELETE FROM Person
# WHERE Id NOT IN (
#     SELECT MIN(Id)
#     FROM (SELECT * FROM Person) AS temp
#     GROUP BY Email
# );


# # Using Self JOIN
# DELETE p1
# FROM Person p1, Person p2
# WHERE p1.Email = p2.Email AND p1.Id > p2.Id


# Import the pandas library
import pandas as pd

# Define a function to delete duplicate emails from a DataFrame
def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # Sort the DataFrame by the 'id' column to ensure the order is consistent
    person.sort_values('id', inplace=True)

    # Drop duplicate rows based on the 'email' column, keeping only the first occurrence
    person.drop_duplicates(subset=['email'], keep='first', inplace=True)

# NOTES:
    # - sort_values() sorts the DataFrame by the specified column(s)
    # - drop_duplicates() removes duplicate rows from the DataFrame
    # - subset specifies the columns to consider for identifying duplicates
    # - keep specifies which duplicates to keep (first, last, or False)
