import pyperclip, random, os
from random import randint

fp = open("peanuts/nuts.txt", "r")
everything = fp.read().split('\n')
xd = input("tea color?")
os.system("cls")
used = []

if xd == "yellow" or xd == "y":
    while True:
        words = []        
        answer = ""
        substring = input("L:")
        
        for i in everything:
            if substring in i and i not in used:
                words.append(i)
        
        # Sort by length, shortest to longest
        words = sorted(words, key=lambda x: len(x), reverse=False)
        curr = 0
        
        # Concatenate words until character limit (2000)
        for i in words:
            if curr >= 2001:  # Discord limit
                break
            else:
                curr += len(i)
                curr += 1
                if curr <= 2000: 
                    answer += i 
                    answer += " "
                    used.append(i)  
        
        pyperclip.copy(answer)

elif xd == "black" or xd == "b" or xd == "green" or xd == "g":
    while True:
        words = []        
        answer = ""
        substring = input("L:")
        
        for i in everything:
            if substring in i and i not in used:
                pyperclip.copy(" ")
                pyperclip.copy(i)
                used.append(i)  
                break

elif xd == "red" or xd == "r":
    while True:
        words = []        
        answer = ""
        substring = input("L:")
        
        for i in everything:
            if substring in i and i not in used:
                words.append(i)
        
        words = sorted(words, key=lambda x: len(x), reverse=False)
        
        if words:
            pyperclip.copy(words[-1])
            used.append(words[-1])  
