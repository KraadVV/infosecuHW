def vigencode(targetText, cipherKey, mode):
    stream = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    output = []

    while True:
        targetText = targetText.upper()
        cipherKey = cipherKey.upper()
        tag = True
        for txt in cipherKey:
            if txt not in stream:
                print("invalid cipher key string '%s' : Key must be alphabet only" %(cipherKey))
                cipherKey = input("new cipher key: ")
                tag = False
                break
        if tag == False:
            continue
        if mode == "encode":
            for i in range(len(targetText)):

                if targetText[i] not in stream:
                    output.append(targetText[i])
                    print("[+]Warning: plain text '%s' is not in alphabet, so it won't be encrypted" % targetText[i])
                    continue
                temTargetNum = stream.index(targetText[i])
                cipherIndex = i%len(cipherKey)
                temCipheNum = stream.index(cipherKey[cipherIndex])
                cipheTxtNum = (temCipheNum + temTargetNum) % 26
                output.append(stream[cipheTxtNum])

            return output
            break
        if mode == "decode":
            for i in range(len(targetText)):

                if targetText[i] not in stream:
                    output.append(targetText[i])
                    print("[+]Warning: plain text '%s' is not in alphabet, so it won't be decrypted" % targetText[i])
                    continue
                temTargetNum = stream.index(targetText[i])
                cipherIndex = i % len(cipherKey)
                temCipheNum = stream.index(cipherKey[cipherIndex])
                cipheTxtNum = (temTargetNum - temCipheNum + 26) % 26
                output.append(stream[cipheTxtNum])

            return output
            break
        else:
            print("invalid mode detected:")
            mode = input("type valid mode: encode or decode!")
            continue



if __name__ == "__main__":
    plain = input("대상 문자를 입력하시오: ")
    ciphe = input("암호화 키를 입력하시오: ")
    cpmod = input("encode/decode: ")
    print("암호문: ",''.join(vigencode(plain,ciphe,cpmod)))
