import random
from alphabets import rus_abs, eng_abs, non_letters

def cipher_creation():
    '''
    Creating a dictionary with letter values.
    It will be used for both encryption and decryption.
    '''
    cipher = dict()
    #33-126
    cipher_list = [chr(i) for i in range(32,126)]+[chr(i) for i in range(ord('А'),ord('я')+1)]
    print(cipher_list)
    for char in cipher_list[::]:
        cipher[char] = random.choice(cipher_list)
        cipher_list.remove(cipher[char])
    return cipher

def get_key(value:str, dictionary:dict) -> str:
    '''
    Get key in dictionary using the value
    '''
    value_index = list(dictionary.values()).index(value)
    dict_key = list(dictionary.keys())[value_index]
    return dict_key

def replacement(text: str,key:dict, decrypt: bool = False):
    '''
    Replacement cipher. 
    The symbol is replaced by an encrypted symbol from the dictionary of values.
    '''
    new_text = ''
    for char in text:
        if decrypt:
            new_text += get_key(char, key)
        else:
            new_text+=key[char]
    return new_text, key

if __name__ == '__main__':
    cr, key = replacement('Текст сообщения таков: Москва, Витебск, Краков', cipher_creation())
    print(cr)
    encr, key = replacement(cr,key, decrypt=True)
    print(encr)
