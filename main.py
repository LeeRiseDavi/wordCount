# Word Count
# This program counts the number of words in a line
# The line being counted comes from the user

print('This program figures out the number of words in a line entered by a user. Please enter text: ')

line = input()

total_count = len(line.split())

print('This line contains: ', total_count, 'words.')