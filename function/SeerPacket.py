from function.Algorithm import Decrypt, Encrypt
from function.Misc import get_int_param, string_to_bytearray, hex_to_binary, binary_to_hex, hex_to_bytearray


def decrypt(cipher):
    CipherLen = get_int_param(cipher, 0)
    PlainLen = (CipherLen - 1).to_bytes(4, byteorder='big')
    cipher = cipher[4:]
    plain = Decrypt(cipher)
    plain = PlainLen + plain
    return plain


def encrypt(plain):
    PlainLen = get_int_param(plain, 0)
    CipherLen = (PlainLen + 1).to_bytes(4, byteorder='big')
    plain = plain[4:]
    cipher = Encrypt(plain)
    cipher = CipherLen + cipher
    return cipher

loc1=bytes([ 0x00, 0x00, 0x00, 0x19, 0x31, 0x00, 0x00, 0x09, 0x00, 0x12, 0x31, 0x2C, 0x67, 0x00, 0x00, 0x02, 0x78, 0x64, 0xAD, 0x18, 0xBC, 0x00, 0x00, 0x00, 0x00] )
print(binary_to_hex(encrypt(loc1)))