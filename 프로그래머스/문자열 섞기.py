def solution(str1, str2):
    answer = ''
    for i in range(0, len(str1)):
        answer = answer + str1[i] + str2[i]
    return answer

# answer = answer + str1[i] + str2[i] 
# answer += str1[i] + str2[i] 생각하자