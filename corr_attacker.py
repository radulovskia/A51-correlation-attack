import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from a51 import A51

def string_to_binary(st : str):
    bits = [bin(ord(i))[2:].zfill(8) for i in st]
    return ''.join(bits)

def binary_to_string(st : str):
    n = 8
    bits = [st[i:i+n] for i in range(0, len(st), n)]
    return ''.join([chr(int(i, 2)) for i in bits])

def decimal_to_string(arr):
    return ''.join(str(i) for i in arr)

def string_to_decimal(st: str):
    return [int(i) for i in list(st)] 

session_key = "0100111000101111010011010111110000011110101110001000101100111010"
sk_arr = string_to_decimal(session_key)
cipher = A51(sk_arr)

keystream = ""

known_plaintext = "aleksandar"
plain_arr = string_to_decimal(string_to_binary(known_plaintext))
cipher_arr = cipher.encrypt(plain_arr)
keystream = cipher.keystream

correlation = np.correlate(plain_arr, cipher_arr)
shift = np.mean(plain_arr)
recovered_state = np.argmax(correlation) - shift
print(recovered_state)