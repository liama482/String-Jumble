"""
stringjumble.py
Author: Liam A
Credit: http://stackoverflow.com/questions/931092/reverse-a-string-in-python, Wilson,
http://stackoverflow.com/questions/10610158/how-do-i-convert-string-characters-into-a-list,
http://stackoverflow.com/questions/6181763/converting-a-string-to-a-list-of-words

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.
Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Use: There you go! Good Job!

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""

txt=input("Please enter a string of text (the bigger the better): ")
txt2='"'+str(txt)+'"'
print('You entered '+txt2+'. Now jumble it:')
print(txt [::-1]) #prints the entire line backwords

import re
Text = re.sub("[^\w]", " ", txt).split()

wrds=int(len(Text))
#print(wrds)
for v in range(wrds,0,-1):
    print(Text[v-1], end=' ') #prints words in reverse order but the letters in the correct order, within the word
print(' ')
for t in range(0,wrds):
    print(Text[t][::-1], end=' ')
