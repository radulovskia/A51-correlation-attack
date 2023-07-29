import argparse
from functools import partial
import multiprocessing
import os
import pandas as pd
from sympy.utilities.iterables import multiset_permutations
from itertools import islice

from a51 import A51
from helpers import *

def gen_multiset_perms(elements, counts, limit):
    if len(elements) != len(counts):
        raise ValueError("The length of 'elements' and 'counts' arrays must be the same")

    total_elements = []
    for i in range(len(elements)):
        total_elements.extend([elements[i]] * counts[i])

    return islice(multiset_permutations(total_elements), limit)
    
def gen_bitarr_perms(arr_length, max_ds_size):
    elements = [0, 1]
    result = []
    for i in range(arr_length+1):
        if len(result) > max_ds_size:
            break
        counts = [arr_length-i, i]
        result += gen_multiset_perms(elements, counts, max_ds_size - len(result))
    return result

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Dataset Generator")
    parser.add_argument("-o", "--output", type=str, default= "output", help="Output folder path")
    parser.add_argument("-l", "--length", type=int, default= 2, help="Length of strings")
    parser.add_argument("-s", "--size", type=int, default= 5, help="Size of dataset")
    parser.add_argument("-n", "--name", type=str, default= "complex_dataset", help="Name of dataset")
    return parser.parse_args()

def encrypt_string(cipher, plain):
    return string_to_decimal(decimal_to_string(cipher.encrypt(plain)))

def encrypt_strings(session_key, plain_strings):
    cipher = A51(session_key)
    with multiprocessing.Pool() as pool:
        encrypted_strings = pool.starmap(partial(encrypt_string, cipher), zip(plain_strings))
    return encrypted_strings

def main() -> None:
    args = parse_args()
    output_path : str = args.output
    ds_name : str = args.name
    string_length : int = args.length
    ds_size : int = args.size
    
    plain_strings = gen_bitarr_perms(string_length, ds_size)

    sk = string_to_binary(get_random_string(8))
    session_key = string_to_decimal(sk)

    cipher_strings = encrypt_strings(session_key, plain_strings)

    df = pd.DataFrame({'Plain Bits':plain_strings, 'Cipher Bits':cipher_strings, 'Session Key':[None]*len(plain_strings)})
    session_key_entry = {'Plain Bits': None, 'Cipher Bits': None, 'Session Key': sk}
    df.loc[-1] = session_key_entry
    df.index = df.index + 1
    df = df.sort_index()

    os.makedirs(output_path, exist_ok = True)
    df.to_csv(os.path.join(output_path, ds_name + ".csv"), index=False)

if __name__ == "__main__":
    main()