# Напишите программу, удаляющую из текста все слова, содержащие "абв". Функции FIND и COUNT юзать нельзя.

def remove_word_with_substr(text, substring='абв'):
    return ' '.join([word for word in text.split(' ') if substring not in word])


print(remove_word_with_substr('абвгдейка - это передача'))
