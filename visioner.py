from alphabets import eng_abs, rus_abs
import math


def visioner_crypt(text: str,key:str, decrypt: bool = False) -> str:
    '''
    The Vigener cipher is that the key here is a word that
    the size is adjusted to the encryption text. 
    Next, the shift for each letter is recognized
    depending on the letter in the key.
    '''
    key*=math.ceil(len(text)/len(key))
    new_text=''
    decrypt = -1 if decrypt else 1
    for i,char in enumerate(text):
        if not char.isalpha():
            new_text+=char
            continue

        caesar_for_char = ord(char) + ord(key[i])*decrypt
        alphabet = eng_abs if char in eng_abs else rus_abs
        if char.isupper():
            alphabet=alphabet.upper()
        new_text+=chr(caesar_for_char%len(alphabet)+ord(alphabet[0]))
    return new_text


if __name__ == '__main__':
    var = (visioner_crypt('Текст сообщения таков: Москва, Витебск, Краков', 'шифр'))
    print(var)
    print(visioner_crypt(var, 'шифр', decrypt=True))