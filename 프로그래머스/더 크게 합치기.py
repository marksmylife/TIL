def solution(a, b):
    answer = 0
    ab = str(a) + str(b)
    ba = str(b) + str(a)

    if ab > ba:
        answer = ab
    else:
        answer = ba

    return int(answer)


    return int(max(f"{a}{b}", f"{b}{a}"))
