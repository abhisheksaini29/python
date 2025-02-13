# Write a Python program to count the number of strings where the
# string length is 2 or more and the first and last character are same
# from a given list of strings.

# Input :

# X = ['abc', 'xyz', 'aba', '1221']

# Output :

# 2

def count_matching_strings(string_list):

    count = 0

    for s in string_list:

        # Check if the string length is 2 or more and the first and last character are the same

        if len(s) >= 2 and s[0] == s[-1]:

            count += 1

    return count


# Input list

X = ['abc', 'xyz', 'aba', '1221']


# Get the count of matching strings

result = count_matching_strings(X)


# Print the result

print(result)