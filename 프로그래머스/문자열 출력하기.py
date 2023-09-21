# 내 풀이
# 제한사항은 고려 안해도 되나?

str = input("입력하세요 :")
if 1 <= len(str) <= 1000000:
    print(str)
else:
    print("다시 입력하세용")


# 타인풀이1
# while이 True 면 반복되니 break를 걸어주었고, False면 계속 반복 bbb
str = input()
while True:
    if len(str) >= 1 and len(str) <= 10000000 and str != ' ':

        print(str)
        break
    else:
        continue


# 타인풀이2
# 이걸 이렇게 풀어버리네...
print(input())