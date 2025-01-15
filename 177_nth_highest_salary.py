# 177. Nth Highest Salary

# # This function finds the Nth highest salary from the Employee table
# # using a correlated subquery approach to count higher salaries

# CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
# BEGIN
#   RETURN (
#       # Write your MySQL query statement below.
#       SELECT DISTINCT salary 
#       FROM Employee e1
#       WHERE N-1 = (                    # If N-1 matches the count of higher salaries,
#           SELECT COUNT(DISTINCT salary) # Count distinct salaries that are higher
#           FROM Employee e2             # than the current salary (e1.salary)
#           WHERE e2.salary > e1.salary  # This effectively finds the Nth highest
#       )
#   );
# END


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # Handle empty DataFrame or invalid N
    if employee.empty or N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    
    # Get unique salaries, sort them in descending order
    unique_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
    
    # Check if N is larger than number of unique salaries
    if N > len(unique_salaries):
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    
    # Get the Nth salary and create result DataFrame
    nth_salary = unique_salaries.iloc[N-1]
    return pd.DataFrame({f'getNthHighestSalary({N})': [nth_salary]})


# NOTES:
# Function breakdown:
# - nth_highest_salary(): Takes employee DataFrame and N as input, returns DataFrame with Nth highest salary
#
# Key steps:
# 1. Input validation:
#    - Checks if DataFrame is empty or N <= 0
#    - Returns None in these invalid cases
#
# 2. Data processing:
#    - drop_duplicates(): Removes duplicate salary values
#    - sort_values(ascending=False): Sorts unique salaries in descending order
#
# 3. Length validation:
#    - Checks if N exceeds number of unique salaries
#    - Returns None if N is too large
#
# 4. Result creation:
#    - iloc[N-1]: Gets the Nth salary (N-1 due to 0-based indexing)
#    - Returns result in DataFrame format with dynamic column name