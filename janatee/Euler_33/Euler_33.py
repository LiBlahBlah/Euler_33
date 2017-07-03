# 약수 리스트
def divisors(a) :
    result = []
    for i in range(2,a+1) :
        if a % i == 0 :
            result.append(i)
    return result

resultOfNume = 1
resultOfDeno = 1

for i in range(12,99) :
    deno1 = int(i / 10)  # 10의 자리
    deno2 = int(i % 10)  # 1의 자리
    if deno1 == deno2 :
        continue
    if deno2 == 0 :
        continue
    for j in range(11,i) :
        nume1 = int(j / 10)  # 10의 자리
        nume2 = int(j % 10)  # 1의 자리
        if nume1 == nume2:
            continue
        if nume2 == 0:
            continue
        if deno2 == nume1 :
            tens = j / i
            ones = nume2 / deno1
            if tens == ones :
                resultOfDeno *= i
                resultOfNume *= j
        elif deno1 == nume2 :
            tens = j / i
            ones = nume1 / deno2
            if tens == ones :
                resultOfDeno *= i
                resultOfNume *= j

a = divisors(resultOfNume)
result = 0
for i in a :
    if resultOfDeno % i == 0 :
        result = resultOfDeno / i

print(result)




