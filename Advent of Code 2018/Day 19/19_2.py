n = 10551314
i = 1
answer = 0

while i <= n:
    if n % i == 0:
        answer += i
    i += 1

print(answer)