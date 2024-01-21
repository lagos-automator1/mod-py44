#! /usr/bin/python3

# Note: The script treats spaces and punctuation as non-alphanumeric characters \
#       and ignores them when checking for palindromes.

def is_palindrome(teststr):
    # The is_palindrome function checks if the input string (teststr) \
    # is equal to its reverse (teststr[::-1]) using the slice trick. \
    # If they are equal, the function returns True; otherwise, it returns False
    if teststr == teststr[::-1]:
        return True
    return False

# The main loop (while run) repeatedly takes user input (teststr) until the user types "exit."
run = True
while (run):
    teststr = input("Enter string to test for palindrome or 'exit':")

    # If the user types "exit" then quit the program
    if teststr == "exit":
        run = False
        break

    # convert the string to all lower case 
    # The entered string is converted to lowercase (teststr = teststr.lower()) \
    # to make the palindrome check case-insensitive
    teststr = teststr.lower()

    # strip all the spaces and punctuation from the string
    # A new string (newstr) is created by iterating through the characters \
    # of the input string and keeping only alphanumeric characters, discarding spaces and punctuation
    newstr = ""
    for x in teststr:
        if x.isalnum():
            newstr += x

    # prints the result of the palindrome test using the is_palindrome function
    print("Palindrome test:", is_palindrome(newstr))
