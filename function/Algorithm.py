StrKey = "!crAckmE4nOthIng:-)"
key = StrKey.encode('utf-8')
import hashlib


def Decrypt(cipher):
    result = key[(len(cipher) - 1) % len(key)] * 13 % (len(cipher))
    cipher = cipher[len(cipher) - result:] + cipher[0:len(cipher) - result]
    plain = bytearray(len(cipher) - 1)
    for i in range(len(cipher) - 1):
        plain[i] = ((cipher[i] >> 5) | (cipher[i + 1] << 3)) & 0xFF
    j = 0
    NeedBecomeZero = False
    for i in range(len(plain)):
        if j == 1 and NeedBecomeZero:
            j = 0
            NeedBecomeZero = False
        if j == len(key):
            j = 0
            NeedBecomeZero = True
        plain[i] = (plain[i] ^ key[j]) & 0xFF
        j += 1
    return plain


def Encrypt(plain):
    cipher = bytearray(len(plain) + 1)
    j = 0
    NeedBecomeZero = False
    for i in range(len(plain)):
        if j == 1 and NeedBecomeZero:
            j = 0
            NeedBecomeZero = False
        if j == len(key):
            j = 0
            NeedBecomeZero = True
        cipher[i] = (plain[i] ^ key[j]) & 0xFF
        j += 1
    cipher[len(cipher) - 1] = 0
    for i in range(len(cipher) - 1, 0, -1):
        cipher[i] = (cipher[i] << 5 | cipher[i - 1] >> 3) & 0xFF
    cipher[0] = (cipher[0] << 5 | 3) & 0xFF
    result = key[len(plain) % len(key)] * 13 % len(cipher)
    cipher = cipher[result:] + cipher[0:result]
    return cipher


def md5(data):
    # 使用hashlib创建md5对象
    md5 = hashlib.md5()
    # 向md5对象中添加需要加密的数据，注意Python3.x中需要先对数据进行encode
    md5.update(data.encode('utf-8'))
    # 获取加密后的16进制字符串
    result = md5.hexdigest()

    return result


def MSerial(a, b, c, d):
    serialNumber = a + c + int(a / (-3)) + b % 17 + d % 23 + 120
    return serialNumber
