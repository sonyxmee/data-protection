"""
Blowfish - алгоритм блочного симметричного шифрования с ключом переменной длины от 32 до 448 бит.
Данные шифруются блоками по 64 бита и проходят 16 раундов сети Фейстеля.
Алгоритм работает в 2 этапа:
1) Формирование ключей шифрования по секретному ключу.
    - Инициализация подключей и таблиц подстановки при помощи секретного ключа
    - Шифрование ключей и таблиц подстановок
2) Шифрование / расшифрование текста
"""

from blowfish import Blowfish

message = "Hello! It's task 4."

print('The plaintext is: {}'.format(message))

blowfish = Blowfish("secretkey", message)
encrypted_message = blowfish.encrypt(message)
print('The encrypted message is: {}'.format(encrypted_message))
decrypted_message = blowfish.decrypt(encrypted_message)
print('The decrypted message is: {}'.format(decrypted_message))
