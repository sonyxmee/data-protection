from src.config import p, q, e
from bidict import bidict


def get_numerical_equivalents():
    d = {}
    a = ord('А')
    alphabet = ''.join([chr(i) for i in range(a, a + 32)])
    # print(alphabet)
    for i in range(32):
        if i < 6:
            d[alphabet[i]] = i + 1
        if i == 6:
            d['Ё'] = i + 1
            d[alphabet[i]] = i + 2
        if i > 6:
            d[alphabet[i]] = i + 2
    d[' '] = 34
    for i in range(35, 45):
        d[i - 35] = i
    # print(d.items())
    return d


def get_keys(p, q, e):
    n = p * q
    f = (p - 1) * (q - 1)
    # print(f"n = {n}, f = {f}, e = {e}")

    k = 1
    d = (k * f + 1) / e
    while (k * f + 1) % e != 0:
        k += 1
        d = (k * f + 1) / e
    d = int(d)
    # print(f"d = {d}, k = {k}")
    public_keys = (e, n)
    private_keys = (d, n)
    list_keys = [public_keys, private_keys]
    return list_keys


def get_inverse_dict():
    return bidict(get_numerical_equivalents()).inverse


def code_rsa(message):
    coding_mes = ''
    public_keys = get_keys(p, q, e)[0]
    print(f'public keys (e, n): {public_keys}')
    dict_alphabet = get_numerical_equivalents()
    for char in message:
        coding_mes += str(int(dict_alphabet[char] ** public_keys[0]) % public_keys[1])
        coding_mes += ','
    coding_mes = coding_mes[:-1]
    return coding_mes


def decode_rsa(message):
    private_keys = get_keys(p, q, e)[1]
    print(f'private keys (d, n): {private_keys}')
    list_message = message.split(',')
    dict_alphabet = get_inverse_dict()
    decoding_mes = ''
    for item in list_message:
        element = int(int(item) ** private_keys[0] % private_keys[1])
        char = dict_alphabet[element]
        decoding_mes += str(char)
    return decoding_mes


if __name__ == '__main__':
    mes = 'КАФСИ'
    print(f'message: {mes}')
    code_mes = code_rsa(mes)
    print(f'code message: {code_mes}')
    decode_mes = decode_rsa(code_mes)
    print(f'decode message: {decode_mes}')
