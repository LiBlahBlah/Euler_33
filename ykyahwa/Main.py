from fractions import Fraction


def digit(number): return [int(i) for i in str(number)]


# 최대 공약수 계산 메서드
# (Euclidean Algorithm; Euclid's Algorithm)
def gcd(a, b):
  while (b != 0):
    temp = a % b
    a = b
    b = temp
  return abs(a)

# 분수 약분 함수 (Reduce a Fraction)
# 분자 분모를 입력받아, 약분 후, 분자 분모가 든 배열을 반환
def reduceFraction(bunja, bunmo):
  frac = [ bunja, bunmo ]

  if (frac[1] == 0): # 분모가 0일 경우에 에러 반환
    frac[0] = 0
    frac[1] = 0
    return frac

  gcd_result = gcd(frac[0], frac[1])

  frac[0] = frac[0] / gcd_result
  frac[1] = frac[1] / gcd_result

  return frac

def search():
    result = Fraction(1,1)
    for mom in range(11, 100):
        for son in range(10, mom):

            print("s = %d, m = %d", mom, son)
            division = son / mom
            digit_mom = digit(mom)
            digit_son = digit(son)


            case = (1, 1)
            if digit_mom[0] == digit_son[0] and digit_mom[1] != 0:
                case = (digit_son[1], digit_mom[1])
            if digit_mom[0] == digit_son[1] and digit_mom[1] != 0:
                case = (digit_son[0], digit_mom[1])
            if digit_mom[1] == digit_son[0] and digit_mom[0] != 0:
                case = (digit_son[1], digit_mom[0])
            if digit_mom[1] == digit_son[1] and digit_mom[0] != 0:
                case = (digit_son[0], digit_mom[0])


            if (case[0] / case[1]) == division and (mom % 10 != 0 and son % 10 != 0):
                result = result * Fraction(case[0], case[1])
                print("case =", case[0], case[1])
                print("s = %d, m = %d", son, mom)

    print("result = ", result)
    return result

f = search()
print("f = ", f)
print("numerator = %d", f.numerator)
print("denominator = %d", f.denominator)


