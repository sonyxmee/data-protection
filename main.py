def task1():
    try:
        with open('src/lab1/lab1.1.doc', 'rb') as file:
            content = file.read()
            print(f'[ TASK1 ]: Длина файла lab1.1.doc: {len(content)} bytes')
    except IOError:
        print('[ TASK1 ]: Невозможно открыть файл')


def task2(filename):
    dict_count, dict_p, dict_i = {}, {}, {}
    try:
        with open(filename, 'rb') as file:  # , encoding='utf-8'
            content = file.read()
            print(f'\n[ TASK2 ]: Содержимое файла {filename}: \n{content}')
            alphabet = set(content)
            for char in alphabet:
                dict_count[char] = content.count(char)
            print('[ TASK2 ]: Алфавит (символ: частота):')
            for key, value in dict_count.items():
                char_key = chr(key)
                print("{0}: {1}".format(key, value), end='\t')
            n = len(content)
            print(f'\n[ TASK2 ]: Длина файла в символах первичного алфавита: {n}')
    except IOError:
        print('[ TASK2 ]: Невозможно открыть файл')


def code(key, mes, m):
    arr = []
    k = 0
    while len(mes) % m != 0:
        mes += 'z'
    arr.append(list(key))
    t = len(mes) // m
    for i in range(t):
        arr.append(list(mes[k:k + m]))
        k += m
    print("[ TASK3 ]: Таблица шифра:")
    for i in range(t + 1):
        for j in range(m):
            print(arr[i][j], end=' ')
        print()
    i, j = 1, 0
    mes = ''
    while i < m + 1:
        if arr[0][j] == str(i):
            for k in range(1, t + 1):
                mes += arr[k][j]
            i += 1
            j = 0
            continue
        j += 1
    return mes


def decode(key, code_mes, m):
    arr = []
    decode_mes = ''
    t = len(code_mes) // 5

    for k in key:
        number_column = int(k)
        b = t * number_column
        a = b - t
        arr.append(list(code_mes[a:b]))

    for j in range(t):
        for i in range(m):
            decode_mes += arr[i][j]
    decode_mes = decode_mes.replace('z', '')

    return decode_mes


def task3():
    try:
        with open('src/lab1/key.txt', 'r') as file:
            content = file.read()
            key = content.split()[2].replace("'", "")
            print()
    except IOError:
        print("[ TASK3 ]: Невозможно открыть файл. Key не определен.")
        return

    mes = 'вотпримершифравертикальнойперестановки'
    m = 5

    print(f'[ TASK3 ]: Исходное сообщение: {mes}')
    print(f'[ TASK3 ]: Ключ: {key}')

    code_mes = code(key, mes, m)
    print(f'[ TASK3 ]: Закодированное сообщение: {code_mes}')
    decode_mes = decode(key, code_mes, m)
    print(f'[ TASK3 ]: Декодированное сообщение: {decode_mes}')


if __name__ == '__main__':
    task1()

    task2('src/lab1/lab1.1.doc')
    task2('src/lab1/im.bmp')

    task3()
