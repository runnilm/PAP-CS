'''
Created on October 24, 2014

@author: mayberryr
'''
# No Vowels
# Demonstrates creating new strings with a for loop.
# Ronnie Mayberry
# Friday, October 24, 2014

message = input("Enter a message: ")
new_message = ""
VOWELS = "aeiou"

print()
for letter in message:
    if letter.lower() not in VOWELS:
        new_message += letter
        print("A new string has been created:" ,new_message)

print("\nYour message without vowels is:", new_message)

input("\n\nPress the enter key to exit.")
