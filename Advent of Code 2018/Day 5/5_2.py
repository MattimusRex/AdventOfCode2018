with open('input.txt', 'r') as inputFile:
    text = list(inputFile.read())

master_text = text
shortest_length = 100000000000
j = 65
while j < 91:
    text = master_text
    text = [char for char in text if char not in [chr(j), chr(j+32)]]

    i = 0
    while i < len(text) - 1:
        if abs(ord(text[i]) - ord(text[i+1])) == 32:
            text.pop(i+1)
            text.pop(i)
            i -= 2
        i += 1

    shortest_length = min(len(text), shortest_length)
    j += 1
    print(len(text))

print(shortest_length)