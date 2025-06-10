# make a loop of string (PYTHON).
# use continue to skip vowels & print only consonats.

text = "PYTHON"
for i in text:
    if i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
        continue
    print(i)

