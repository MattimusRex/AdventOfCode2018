import sys

detour_counts = [0]
def solve(string, start, end, current_count):
    count = 0
    counts = []
    i = start
    while i < end:
        if string[i].isalpha():
            count += 1
        elif string[i] == '(':
            new_start = i + 1
            para_count = 1
            while para_count > 0:
                i += 1
                if string[i] == '(':
                    para_count += 1
                elif string[i] == ')':
                    para_count -= 1
            sub_count = solve(string, new_start, i, count + current_count)
            if string[i - 1] == '|':
                detour_counts.append(current_count + count + (sub_count//2))
            else:
                count += sub_count
        elif string[i] == '|':
            counts.append(count)
            count = 0
        i += 1
    
    counts.append(count)
    return max(counts)



with open('input.txt', 'r') as inputFile:
    string = inputFile.readline()


answer = solve(string, 0, len(string), 0)
print(detour_counts)
biggest_detour = max(detour_counts)
print(max(answer, biggest_detour))

