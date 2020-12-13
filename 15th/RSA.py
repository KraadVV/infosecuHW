def createKey(a, b):
    p = int(a)
    q = int(b)
    n = p*q
    pi = (p-1)*(q-1)
    print(pi)
    divN = []
    e = []
    #n의 약수 구하기
    for i in range(pi):

        if i == 1 or i == 0:
            continue
        if pi%i == 0:
            divN.append(i)
    print(divN)
    #n의 서로소 e 구하기
    for i in range(pi):
        isitseoroso = True
        if i == 1:
            continue
        for j in divN:
            if j == 0:
                continue
            if i%j == 0:
                isitseoroso = False
                break
        if isitseoroso:
            e.append(i)

    print("가능한 e의 값: ")
    count = 1
    for i in range(len(e)):
        print(count, "번: ", e[i])
        count += 1
    eNum = int(input("선택할 e의 번호를 입력하시오: ")) - 1
    chosenE = int(e[eNum])
    #d 구하기
    k = 1
    while (chosenE*k)%pi != 1:
        k += 1
    d = k
    print("공개키: ", n, chosenE, ", 비밀키: ", n, d)
    return n, chosenE, d

def encryption(n, e, m):
    c = (m**e)%n
    return c

def decryption(n, d, c):
    m = (c**d)%n
    return m

if __name__ == '__main__':
    p = input("p를 지정하시오: ")
    q = input("q를 지정하시오: ")
    str = int(input("처리할 숫자를 입력하시오: "))
    n, e, d = createKey(p,q)

    mod = input("1: 암호화\n2: 복호화\n모드를 선택하시오: ")
    if mod == "1":
        c = encryption(n, e, str)
        print("암호화 결과: ", c)
    if mod == "2":
        m = decryption(n, d, str)
        print("복호화 결과: ", m)
    else:
        exit(0)
    exit(0)
