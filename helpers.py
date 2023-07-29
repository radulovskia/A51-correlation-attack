import random
import string

def binary_to_string(st : str):
    n = 8
    bits = [st[i:i+n] for i in range(0, len(st), n)]
    return ''.join([chr(int(i, 2)) for i in bits])

def string_to_binary(st : str):
    bits = [bin(ord(i))[2:].zfill(8) for i in st]
    return ''.join(bits)

def decimal_to_string(arr):
    return ''.join(str(i) for i in arr)

def string_to_decimal(st: str):
    return [int(i) for i in list(st)] 

def get_random_string(length):
    letters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(letters) for i in range (length))