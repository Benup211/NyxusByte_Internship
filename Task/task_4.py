"""4.	Develop a program that takes a sentence from the user and counts the number of vowels in it using a loop and conditional statement.
"""
import re
user_sentence=input("Enter a sentence:")
user_sentence.lower()
list_of_vowel=re.findall(r'[aeiou]',user_sentence)
print(f"Total vowel used in the {user_sentence} is {len(list_of_vowel)}")