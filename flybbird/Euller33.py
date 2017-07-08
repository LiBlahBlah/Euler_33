"""
Euller 33

분수 49/98에는 재미있는 성질이 있습니다.
수학을 잘 모르는 사람이 분모와 분자에서 9를 각각 지워서 간단히 하려고 49/98 = 4/8 처럼 계산해도 올바른 결과가 됩니다.
이에 비해 30/50 = 3/5 같은 경우는 다소 진부한 예라고 볼 수 있습니다.

위와 같은 성질을 가지면서 '진부하지 않은' 분수는, 값이 1보다 작고 분자와 분모가 2자리 정수인 경우 모두 4개가 있습니다.
이 4개의 분수를 곱해서 약분했을 때 분모는 얼마입니까?

"""
"""
 문제 풀이
    1. 분자/분모 는 1보다 작고 
       분자 11 ~ 98
       분모 12 ~ 99
       를 구간에서 찾는다
       
       단 분자나 분모는 분모 가 10으로 나누어 떨어져서는 안된다..
       
    2. 
"""


def reduce_fraction(bunja, bunmo):
    data = [bunja, bunmo]

    if bunmo == 0:
        return 0

    gdc_result = gcd(bunja, bunmo)

    data[0] = data[0]/gdc_result
    data[1] = data[1]/gdc_result

    return data


# 최대 공약수 계산 메소드
def gcd(x, y):
    while y != 0:
        temp = x % y
        x = y
        y = temp

    return abs(x)


start_index = 11
end_index = 98

bunjaTotalValue = 1
bunmoTotalValue = 1

for bunjaValue in range(start_index, end_index):
    for bunmoValue in range(bunjaValue+1, end_index+1):
        # 1. 동일한 애는 return
        if bunjaValue == bunmoValue:
            continue

        # 2. 진부한 수는 return
        if (bunjaValue % 10 == 0) and (bunmoValue % 10 == 0):
            continue

        # 3. 분자 /분모에 동일한 숫자가 있지 않는 경우
        bunjaFirst = int(bunjaValue/10)
        bunjaSecond = bunjaValue % 10

        bunmoFirst = int(bunmoValue/10)
        bunmoSecond = bunmoValue % 10

        # 4. 실제 값
        originValue = bunjaValue / bunmoValue

        # 5. 진부하지 않은 수
        notClicheValue = 0

        if bunjaFirst == bunmoFirst and bunmoSecond != 0:
            notClicheValue = bunjaSecond / bunmoSecond
        elif bunjaFirst == bunmoSecond:
            notClicheValue = bunjaSecond / bunmoFirst
        elif bunjaSecond == bunmoFirst and bunmoSecond != 0:
            notClicheValue = bunjaFirst / bunmoSecond
        elif bunjaSecond == bunmoSecond:
            notClicheValue = bunjaFirst / bunmoFirst

        if originValue == notClicheValue:
            print("===========================")
            print(" BunjaValue =", bunjaValue)
            print(" BunmoValue =", bunmoValue)
            # print(" ORIGIN-VALUE = ", originValue)
            print(" Not Clishe-VALUE =", notClicheValue)
            print("===========================")

            bunjaTotalValue *= bunjaValue
            bunmoTotalValue *= bunmoValue


# 6. 4개의 분수를 곱해서 약분했을때 분모는 얼마입니까???
print("결과를 구해보자")
print(bunjaTotalValue, bunmoTotalValue)
goal = reduce_fraction(bunjaTotalValue, bunmoTotalValue)
print(goal)

