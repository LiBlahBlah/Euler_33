from fractions import Fraction  # 분수 처리 모듈 (https://docs.python.org/3.6/library/fractions.html)

result = Fraction(1)

for n1 in range(10, 100):  # 분자
    for n2 in range(10, 100):  # 분모
        if n1 >= n2: continue  # 분자가 분모보다 크거가 같은면 무시
        if n1 % 10 == 0 and n2 % 10 == 0: continue  # 진부한 경우 무시

        # 처리 전 후 비교용 변수
        f1 = Fraction(n1, n2)
        f2 = Fraction()

        # 문자로 바꿔놓고 처리한다
        s1, s2 = str(n1), str(n2)

        # 같은 숫자 제거
        try:
            if s1[0] == s2[0]:
                f2 = Fraction(int(s1[1]), int(s2[1]))
            elif s1[0] == s2[1]:
                f2 = Fraction(int(s1[1]), int(s2[0]))
            elif s1[1] == s2[0]:
                f2 = Fraction(int(s1[0]), int(s2[1]))
            elif s1[1] == s2[1]:
                f2 = Fraction(int(s1[0]), int(s2[0]))
            else:
                continue
        except ZeroDivisionError:
            continue

        if f1 != f2: continue  # 값이 달라지면 무시

        # 값 누적 곱하기
        result *= f1

# 분모 출력
print(result.denominator)
