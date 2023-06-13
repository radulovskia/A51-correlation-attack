from a51 import A51

def string_to_binary(st : str):
    bits = [bin(ord(i))[2:].zfill(8) for i in st]
    return ''.join(bits)

def binary_to_string(st : str):
    n = 8
    bits = [st[i:i+n] for i in range(0, len(st), n)]
    return ''.join([chr(int(i, 2)) for i in bits])

def use_a51(instance : A51, plaintext):
	print("Session key:\t", instance._get_session_key())
	cipher = instance #A51(session_key)
	print("Plaintext:\t",plaintext)
	plaintextBits = string_to_binary(plaintext)
	print("Plaintext bits:\t",plaintextBits)
	ciphertext = cipher.encrypt(plaintextBits, len(plaintextBits))
	print("Ciphertext:\t", ciphertext)
	print("Keystream:\t", cipher.keystream)
	decryptedBits = cipher.decrypt(ciphertext)
	print("Decrypted bits:\t", decryptedBits)
	decrypted = binary_to_string(decryptedBits)
	print("Decrypted text:\t", decrypted)
	print("\n\n")

session_key = "0100111000101111010011010111110000011110101110001000101100111010"
instance = A51(session_key)
text = "test123"
use_a51(instance, text)
use_a51(instance, text)
use_a51(instance, text)
