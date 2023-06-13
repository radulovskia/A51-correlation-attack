from a51 import A51
import main

text1 = "radulovski123"
session_key = "0100111000101111010011010111110000011110101110001000101100111010"
instance1 = A51(session_key)
plaintext_bits = main.string_to_binary(text1)
ciphertext = instance1.encrypt(plaintext_bits, len(plaintext_bits))

print("Original text:\t\t", text1)
print("Original keystream:\t", instance1._get_keystream())
print("Original Plain bits:\t", plaintext_bits)
print("Original Ciphertext:\t", ciphertext)
print("\n")

known_text = "radul"
known_keystream_part = instance1._get_keystream()[:20] #20 from 80, 25%
# keystream will be XOR from plaintext and cipher
known_plain_bits = main.string_to_binary(known_text)

print("Known text:\t\t", known_text)
print("Known keystream:\t", known_keystream_part)
print("Known Plain bits:\t", known_plain_bits)
print("Known Ciphertext:\t", ciphertext)
print("\n")
