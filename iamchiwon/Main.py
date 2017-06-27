#
# 분자, 분모 중에서 같은 숫자를 빼고 반환, 없으면 (0,0)
#
def removeSameNumber(son, mom):
    son10 = int(son / 10)
    son01 = son % 10
    mom10 = int(mom / 10)
    mom01 = mom % 10
    if son10 == mom10: return (son01, mom01)
    if son10 == mom01: return (son01, mom10)
    if son01 == mom10: return (son10, mom01)
    if son01 == mom01: return (son10, mom10)
    return (0, 0)


#
# 분자나 분보에 같은 숫자가 있는지 확인, 같은 숫자 뺀 결과가 (0,0)이 아닌경우
#
def hasSameNumber(son, mom):
    return removeSameNumber(son, mom) != (0, 0)


#
# 약분하기 분자가 작으니까 분자~<1 까지 분자/분모 둘 다 나누어 떨이면 값을 나눈다
#
def reductionOfFraction(son, mom):
    _son = son
    _mom = mom
    for n in range(_son, 0, -1):
        if _son % n == 0 and _mom % n == 0:
            _son = int(_son / n)
            _mom = int(_mom / n)
    return (_son, _mom)


####################################
## 여기서부터 시작

finalSon = 1
finalMom = 1

# 분모는 11~99 까지
for mom in range(11, 100):
    # 분자는 10~<분모 까지
    for son in range(10, mom):
        # 진부한 거 빼기
        if son % 10 == 0 and mom % 10 == 0: continue
        # 분모나 분자가 둘 다 같은 숫자인 경우 빼기: 같은 숫자를 없애버리면 남는게 없으니까
        if mom % 11 == 0 or son % 11 == 0: continue
        # 같은 숫자 없는거 빼기
        if not hasSameNumber(son, mom): continue
        # 같은 숫자 빼기 전에 계산 결과
        beforeValue = son / mom
        # 같은 숫자 뺀 후의 분수
        after = removeSameNumber(son, mom)
        # 분자나 분모가 0이 남는 경우는 뺀다
        if after[0] == 0 or after[1] == 0: continue
        # 같은 숫자 뺀 후의 계산 결과
        afterValue = after[0] / after[1]
        # 결과 값이 다른경우 뺀다
        if beforeValue != afterValue: continue
        # 모두 곱한다
        finalSon *= son
        finalMom *= mom
# 약분하기
resultOfReduction = reductionOfFraction(finalSon, finalMom)
# 약분한 결과의 분모
print(resultOfReduction[1])
