#Reverse words in a given string using python
string=input()
word=string.split(' ')
word=list(reversed(word))
print(" ".join(word))