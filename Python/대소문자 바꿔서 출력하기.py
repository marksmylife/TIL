str = input()

for i in str:
    if i.isupper():
        print(i.lower(), end='')
    else:
        print(i.upper(), end='')


# 이거 뭔데? ㅋㅋㅋㅋㅋ
print(input().swapcase())


# 많은 답안
str = input()

answer = ''

for a in str:
    if a.isupper() : answer += a.lower()
    else : answer += a.upper()

print(answer)