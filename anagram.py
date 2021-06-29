//Using sorted method
def check_anagram(a,b):
    if (sorted(string1)==sorted(string2)):
        print("Strings are anagram")
    else:
        print("Strings are not anagram")
    
    
    

string1=input()
string2=input()
check_anagram(string1,string2)

//Using Counter method
from collections import Counter

def check_anagram(a,b):
    if(Counter(a)==Counter(b)):
        print("Strings are anagrams")
    else:
        print("Strings are not anagrams")



string1=input()
string2=input()
check_anagram(string1,string2)