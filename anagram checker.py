# Anagram Checker

from string import punctuation

first_word = input("First Word: ")
a = first_word.replace(" ", "")
second_word = input("Second Word: ")
b = second_word.replace(" ", "")

# loops to remove punctuations
for x in a:
    if x in punctuation:
        a = a.replace(x, "")

for y in b:
    if y in punctuation:
        b = b.replace(y, "")

# converting the string to a list
split1 = list(a.lower())
split1.sort()
split2 = list(b.lower())
split2.sort()
result = str(split1 == split2)
print(split1) # Just to show the comparison
print(split2) # Just to show the comparison
print('Are they anagrams? ' + result)