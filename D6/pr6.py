# take a list of list as input
# use list comprehension to creat a new list 
# this new list contains list starts with vowels only

words = []
words_vowels = []

n = int(input("Enter how many words: "))

for i in range(n):
    words.append(input("Enter words: "))

for word in words:
    #if word[0]=="a" or word[0]=="e" or word[0]=="i" or word[0]=="o" or word[0]=="u":
    if (word.startswith("a") or word.startswith("e") or word.startswith("i") 
        or word.startswith("o") or word.startswith("u")):
        words_vowels.append(word)

print(words_vowels)