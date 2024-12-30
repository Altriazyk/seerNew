import binascii
import sys


# 获取包长度
def get_int_param(plain, index):
    temp = plain[index:index + 4]
    tempReversed = temp[::-1]
    intValue = int.from_bytes(tempReversed, byteorder='little')
    return intValue


# 2进制字符串转二进制数组
def string_to_bytearray(binaryString):
    n = len(binaryString) // 8
    bytearrayResult = bytearray()
    for i in range(0, n):
        # 每次取8个字符（即一个字节）
        byteStr = binaryString[i * 8:(i + 1) * 8]
        # 将这8个字符转换为整数（二进制到十进制的转换）
        byteValue = int(byteStr, 2)
        # 将整数添加到bytearray中
        bytearrayResult.append(byteValue)
    return bytearrayResult


# 16进制字符串转二进制字符串
def hex_to_binary(hexString):
    binaryString = ''.join(format(int(c, 16), '04b') for c in hexString)
    return binaryString


# 二进制数组转16进制
def binary_to_hex(binary):
    hexString = ""
    for i in range(len(binary)):
        hexString += str("{:02X}".format(binary[i]))
    return hexString


# 16字符串进制转二进制数组
def hex_to_bytearray(hexString):
    # 移除字符串中的所有空格和非16进制字符（可选，取决于输入数据的清洁程度）
    hexString = ''.join(c for c in hexString if c in '0123456789abcdefABCDEF')

    # 检查十六进制字符串的长度是否为偶数
    if len(hexString) % 2 != 0:
        print("十六进制字符串的长度必须为偶数")
        return None

        # 初始化一个空列表来存储二进制字符串
    byteArray = bytearray()

    # 遍历字符串，每次处理两个字符
    for i in range(0, len(hexString), 2):
        # 从字符串中提取两个字符
        h = hexString[i:i + 2]
        # 将这两个字符从十六进制转换为字节，并添加到字节数组中
        byteArray.append(int(h, 16))

        # 返回字节数组
    return byteArray
#十进制转8位16进制
def decimal_to_8hex(decimal_number):
    # 使用格式化字符串，确保结果至少为8位，不足的前面补0
    hex_string = "{:08x}".format(decimal_number)
    return hex_string
