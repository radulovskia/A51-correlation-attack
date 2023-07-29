from a51 import A51
import pandas as pd
import random, string
import os
import argparse

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Dataset Generator")
    parser.add_argument("-o", "--output", type=str, default= "output", help="Output folder path")
    parser.add_argument("-l", "--length", type=int, default= 2, help="Length of strings")
    parser.add_argument("-s", "--size", type=int, default= 5, help="Size of dataset")
    parser.add_argument("-n", "--name", type=str, default= "test_dataset", help="Name of dataset")
    return parser.parse_args()

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

def main() -> None:
    args = parse_args()
    output_path : str = args.output
    ds_name : str = args.name
    string_length : int = args.length
    ds_size : int = args.size

    session_key = string_to_decimal(string_to_binary(get_random_string(8)))

    plain_strings = []
    for i in range(ds_size):
        plain_strings.append(string_to_decimal(string_to_binary(get_random_string(string_length))))

    cipher_strings = []
    cipher = A51(session_key)
    for i in range(ds_size):
        cipher_strings.append(string_to_decimal(decimal_to_string(cipher.encrypt(plain_strings[i]))))

    session_keys = [session_key]*ds_size
    df = pd.DataFrame({'Plain Bits':plain_strings, 'Cipher Bits':cipher_strings, 'Session Key':session_keys})

    os.makedirs(output_path, exist_ok=True)
    df.to_csv(os.path.join(output_path, ds_name+".csv"), index=False)


if __name__ == "__main__":
    main()