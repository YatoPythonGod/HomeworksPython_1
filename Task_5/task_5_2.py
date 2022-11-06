# задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def greate_file(file_name, content):
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(content)


def read_file(file_name):
    with open(file_name, encoding='utf-8') as f:
        return f.read()


def run_length_encoding(text: str):
    """RLE encoding str"""
    result = []
    a = None
    count = 1
    for i in text + chr(ord(text[-1]) + 1):
        if i == a:
            count += 1
        else:
            if count > 1:
                result.append(f'{count}{a}')
            else:
                result.append(a)
            count = 1
        a = i
    result.append(a)

    return ''.join(result[1:-1])


def decode_rle(text: str):
    """RLE decode str"""
    count = ''
    result = ''
    for i in text:
        if i.isdigit():
            count += i
        else:
            if count:
                result += int(count) * i
                count = ''
            else:
                result += i
    return result


if __name__ == '__main__':
    rle_text = run_length_encoding('AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool')
    print(rle_text)
    greate_file('task_5_2.txt', rle_text)
    print(decode_rle(read_file('task_5_2.txt')))
