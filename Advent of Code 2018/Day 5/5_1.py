with open('input.txt', 'r') as inputFile:
    text = list(inputFile.read())

i = 0
while i < len(text) - 1:
    if abs(ord(text[i]) - ord(text[i+1])) == 32:
        text.pop(i+1)
        text.pop(i)
        i -= 2
    i += 1

print(len(text))
