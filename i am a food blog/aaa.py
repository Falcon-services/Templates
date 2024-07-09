# # # # # # # def distinct_substrings(S):
# # # # # # #     n = len(S)
# # # # # # #     substrings = set()
    
# # # # # # #     # Iterate through all possible starting points of substrings
# # # # # # #     for i in range(n):
# # # # # # #         # Iterate through all possible ending points of substrings
# # # # # # #         for j in range(i+1, n+1):
# # # # # # #             # Add substring S[i:j] to the set
# # # # # # #             substrings.add(S[i:j])
    
# # # # # # #     return len(substrings)

# # # # # # # # Example usage:
# # # # # # # S = "ababa"
# # # # # # # print(distinct_substrings(S))  # Output: 6
# # # # # # # def distinct_substrings(S):
# # # # # # #     n = len(S)
# # # # # # #     substrings = set()

# # # # # # # # Generate all possible strings by removing characters from the beginning or end
# # # # # # #     for i in range(n):
# # # # # # #         for j in range(i+1, n+1):
# # # # # # #             substrings.add(S[i:n])
# # # # # # #             substrings.add(S[0:j])

# # # # # # # # Add all possible substrings of the generated strings
# # # # # # #     for s in substrings.copy():
# # # # # # #         for i in range(len(s)):
# # # # # # #             for j in range(i+1, len(s)+1):
# # # # # # #                 substrings.add(s[i:j])

# # # # # # # # Remove the empty string from the set (if it exists)
# # # # # # #     substrings.discard("")

# # # # # # #     return len(substrings)


# # # # # # # S = "z"
# # # # # # # print(distinct_substrings(S))  # Output: 14

# # # # # # def max_exclude_tax_report(A, D):
# # # # # #     # N = len(A)
# # # # # #     # max_exclude = 0
    
# # # # # #     # # Try all possible group sizes from 1 to N
# # # # # #     # for group_size in range(1, N + 1):
# # # # # #     #     exclude_sum = 0
# # # # # #     #     # Divide the employees into groups of size 'group_size'
# # # # # #     #     for i in range(0, N, group_size):
# # # # # #     #         current_group_size = min(group_size, N - i)
# # # # # #     #         exclude_sum += current_group_size // D
        
# # # # # #     #     # Keep track of the maximum sum of excluded values
# # # # # #     #     max_exclude = max(max_exclude, exclude_sum)
    
# # # # # #     # return max_exclude
# # # # # #     ans=0
# # # # # #     for i in range(len(A)):
# # # # # #         ans+=A[i]-D
# # # # # #     return ans


# # # # # # # Example usage:
# # # # # # A = [5,2,7,3,4]
# # # # # # D = 3
# # # # # # print(max_exclude_tax_report(A, D))  # Output will vary depending on D and grouping

# # # # # from math import ceil

# # # # # def min_tax_report(A, D):
# # # # #     N = len(A)
# # # # #     # Initialize dp array where dp[i] represents minimum tax for the first i employees
# # # # #     dp = [float('inf')] * (N + 1)
# # # # #     dp[0] = 0  # No employees, no tax
    
# # # # #     # Compute the minimum tax for each number of employees from 1 to N
# # # # #     for i in range(1, N + 1):
# # # # #         for j in range(i):
# # # # #             # Calculate the tax for splitting employees from j+1 to i
# # # # #             project_size = i - j
# # # # #             tax_exclusion = project_size // D
# # # # #             dp[i] = min(dp[i], dp[j] + tax_exclusion)
    
# # # # #     return dp[N]

# # # # # # Example usage:
# # # # # A = [5,2,7,3,4]
# # # # # D = 3
# # # # # print(min_tax_report(A, D))  # Output: 2

# # # # def min_tax(N, D, A):
    
# # # #     A.sort(reverse=True)
    
  
# # # #     total_tax = 0
# # # #     project_size = 0
    
   
# # # #     for salary in A:
       
# # # #         project_size += salary
        
      
# # # #         if project_size >= D:
# # # #             total_tax += project_size - project_size//D
# # # #             project_size = 0
    
# # # #     if project_size > 0:
# # # #         total_tax += project_size - project_size//D
    
# # # #     return total_tax

# # # # N = 5
# # # # D = 3
# # # # A = [5,2,7,3,4]
# # # # print(min_tax(N, D, A))

# # # def min_tax_report(A, N, D):
  

# # #   # Sort the salaries in descending order for better optimization.
# # #     A.sort(reverse=True)

# # #   # Initialize prefix sums for cumulative salaries.
# # #     prefix_sum = [0] * (N + 1)
# # #     for i in range(N):
# # #         prefix_sum[i + 1] = prefix_sum[i] + A[i]

# # #   # Minimum tax to report initialized with total salary.
# # #     min_tax = prefix_sum[N]

# # #   # Loop through possible project divisions.
# # #     for i in range(1, N + 1):
# # #     # Calculate the number of employees excluded for this division (i projects).
# # #         excluded = [(n // D) for n in range(i, N + 1, i)]

# # #     # Calculate the total tax to report for this division.
# # #         tax = prefix_sum[N] - sum(A[i - 1 - e:i] for e in excluded)

# # #     # Update minimum tax if this division offers a lower amount to report.
# # #         min_tax = min(min_tax, tax)

# # #     return min_tax

# # # # Example usage
# # # A = [5,2,7,3,4]
# # # N = len(A)
# # # D = 3

# # # min_tax = min_tax_report(A, N, D)
# # # print("Minimum sum of tax to report:", min_tax)

# # def min_tax_report(A, D):
# #     N = len(A)
# #     dp = [float('inf')] * (N + 1)
# #     dp[0] = 0  # No employees, no tax
    
# #     for i in range(1, N + 1):
# #         for j in range(i):
# #             group_size = i - j
# #             tax_exclusion = group_size // D
# #             dp[i] = min(dp[i], dp[j] + group_size - tax_exclusion)
    
# #     return dp[N]

# # # Example usage:
# # A = [5,2,7,3,4]
# # D = 3
# # print(min_tax_report(A, D))  # Output: 3

# MOD = 10**9 + 7

# def is_valid(x):
#     bin_x = bin(x)[2:]  # Get the binary representation of x without '0b' prefix
#     count_1 = 0
#     count_0 = 0
    
#     for bit in bin_x:
#         if bit == '1':
#             count_1 += 1
#         elif bit == '0':
#             count_0 += 1
#         if count_1 <= count_0:
#             return False
#     return True

# def find_count(l, r, k):
#     dp = {}

#     def count_valid(x):
#         if x in dp:
#             return dp[x]
#         if x < 0:
#             return 0
#         count = 0
#         if is_valid(x) and x % k == 0:
#             count += 1
#         count += count_valid(x - 1)
#         dp[x] = count % MOD
#         return dp[x]
    
#     return (count_valid(r) - count_valid(l - 1)) % MOD

# def main():
#     M = int(input().strip())
#     N = int(input().strip())
#     K = int(input().strip())
#     L = input().strip()
#     R = input().strip()
    
#     l = int(L, 2)
#     r = int(R, 2)
    
#     result = find_count(l, r, K)
#     print(result)

# # Example usage:
# # Input from sample test case
# import sys
# from io import StringIO

# input_data = "1\n2\n1\n1\n11\n"
# sys.stdin = StringIO(input_data)

# main()

MOD = 10**9 + 7

def is_valid(x):
    bin_x = bin(x)[2:]  # Get the binary representation of x without '0b' prefix
    count_1 = 0
    count_0 = 0
    
    for bit in bin_x:
        if bit == '1':
            count_1 += 1
        elif bit == '0':
            count_0 += 1
        if count_1 <= count_0:
            return False
    return True

def find_count(l, r, k):
    dp = {}

    def count_valid(x):
        if x in dp:
            return dp[x]
        if x < 0:
            return 0
        count = 0
        if is_valid(x) and x % k == 0:
            count += 1
        count += count_valid(x - 1)
        dp[x] = count % MOD
        return dp[x]
    
    return (count_valid(r) - count_valid(l - 1)) % MOD

def main():
    M = int(input().strip())
    N = int(input().strip())
    K = int(input().strip())
    L = input().strip()
    R = input().strip()
    
    l = int(L, 2)
    r = int(R, 2)
    
    result = find_count(l, r, K)
    print(result)

# Example usage:
# Input from sample test case
import sys
from io import StringIO

input_data = "1\n2\n1\n1\n11\n"
sys.stdin = StringIO(input_data)

main()
