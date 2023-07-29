from a51 import A51
from helpers import *

def use_a51(instance : A51, plain_arr):
	print("Session key:\t", decimal_to_string(instance._get_session_key()))
	cipher = instance #A51(session_key)
	decimal_string = decimal_to_string(plain_arr)
	plaintextString = binary_to_string(decimal_string)
	print("Plaintext:\t", plaintextString)
	print("Plaintext bits:\t", decimal_string)
	cipher_arr = cipher.encrypt(plain_arr)
	ciphertext = decimal_to_string(cipher_arr)
	print("Cipher bits:\t", ciphertext)
	ks = decimal_to_string(cipher.keystream)
	print("Keystream:\t", ks)
	decrypted_arr = cipher.decrypt(cipher_arr)
	decryptedBits = decimal_to_string(decrypted_arr)
	print("Decrypted bits:\t", decryptedBits)
	decrypted = binary_to_string(decryptedBits)
	print("Decrypted text:\t", decrypted)
	print("\n\n")

session_key = "0100111000101111010011010111110000011110101110001000101100111010"
arr_SK = string_to_decimal(session_key)
instance = A51(arr_SK)
text_string = "test123"
text = string_to_binary(text_string)
text = string_to_decimal(text)
use_a51(instance, text)
use_a51(instance, text)
use_a51(instance, text)
