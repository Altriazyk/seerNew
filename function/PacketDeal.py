import numpy as np

from function import Misc
from function.Misc import get_int_param


class Algorithm:
    def __init__(self):
        self.StrKey = "!crAckmE4nOthIng:-)"
        self.key = None
        self.init_key()

    def init_key(self):
        self.key = self.StrKey.encode('utf-8')

    # 解密算法
    def decrypt(self, cipher):
        # 假设key是一个列表或类似的可迭代对象
        # 假设cipher是一个字节数组（在Python中通常使用bytearray）

        # 第一步：循环移位
        shift_amount = self.key[cipher[-1] % len(self.key)] * 13 % len(cipher)
        cipher = cipher[-shift_amount:] + cipher[:-shift_amount]

        # 第二步：解密（基于每两个字节的位操作）
        plain = bytearray()
        for i in range(0, len(cipher) - 1, 2):
            # 如果cipher长度为奇数，则忽略最后一个字节
            if i + 1 < len(cipher):
                # 合并两个字节为一个字节（实际上丢失了部分数据）
                combined = (cipher[i] >> 5) | ((cipher[i + 1] & 0x07) << 3)
                plain.append(combined)

                # 第三步：异或解密
        j = 0
        need_become_zero = False
        for i in range(len(plain)):
            if j == 1 and need_become_zero:
                j = 0
                need_become_zero = False
            if j == len(self.key):
                j = 0
                need_become_zero = True
            plain[i] ^= self.key[j]
            j += 1

        return plain


cipher = "000000a9".replace(" ", '')
obj = Algorithm()
byte_array=obj.decrypt(Misc.hex_to_byte(cipher))
print(str(byte_array))

print(get_int_param(byte_array,0))  # 输出: 1afb0800
