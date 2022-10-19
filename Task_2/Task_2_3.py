# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой. COUNT или FIND нельзя юзать!
# говорил же на семинаре.

def count_substring_in_string(string, substring):
    count = 0
    for i, letter in enumerate(string):
        if substring[0] == letter:
            if substring == string[i: i + len(substring)]:
                count += 1
    return count


user_string = input('Please enter a string to search for a substring: ')
user_substring = input('Please enter a substring: ')

print(count_substring_in_string(user_string, user_substring))
