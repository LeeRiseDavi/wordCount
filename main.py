# Word Count
# This program counts the number of words in a line
# The line being counted comes from the user

# this prompts the user to write something
print('This program figures out the number of words in a line entered by a user. Please enter text: ')

# this ensures that the response is a string
line = str(input())

# this splits the words and counts them
total_count = len(line.split())

# this prints the results
print('This line contains: ', total_count, 'words.')
