from fractions import Fraction  # 분수 처리 모듈 (https://docs.python.org/3.6/library/fractions.html)

result = Fraction(1)

for n1 in range(10, 100):  # 분자
    for n2 in range(10, 100):  # 분모
        if n1 >= n2: continue  # 분자가 분모보다 크거가 같은면 무시
        if n1 % 10 == 0 and n2 % 10 == 0: continue  # 진부한 경우 무시

        f1 = Fraction(n1, n2)  # 처리 전
        f2 = Fraction()  # 처리 후

        # 교집합으로 같은 숫자 찾기
        s1, s2 = set(str(n1)), set(str(n2))
        inter = set(s1) & set(s2)
        if bool(inter) == False: continue  # 교집합 없으면 무시

        # 같은 숫자 제거
        s1 -= inter
        s2 -= inter
        if bool(s1) == False or bool(s2) == False: continue  # 숫자가 남지 않으면 무시

        try:
            f2 = Fraction(int(list(s1)[0]), int(list(s2)[0]))
        except ZeroDivisionError:
            continue  # 0만 남는 경우 무시

        if f1 != f2: continue  # 값이 달라지면 무시

        # 값 누적 곱하기
        result *= f1

# 분모 출력
print(result.denominator)
