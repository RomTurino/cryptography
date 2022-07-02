from alphabets import eng_abs, rus_abs
def caesar_code(text: str,key:int, decrypt: bool = False) -> str:
    '''
    Encrypts the text by shifting the letters in the Unicode table 
    by key position
    '''
    # new_text=''
    # for char in text:
    #     new_text+=chr(ord(char)+key)
    key = -key if decrypt else key
    return ''.join([chr(ord(char)+key) for char in text])

def caesar_code_harder(text: str,key:int, decrypt: bool = False)->str:
    '''
    Encrypts text by shifting letters in the alphabet
    '''
   
    key = -key if decrypt else key
    new_text=''
    for char in text:
        if char in eng_abs:
            new_text+=eng_abs[(eng_abs.index(char)+key)%len(eng_abs)]
        elif char in rus_abs:
            new_text+=rus_abs[(rus_abs.index(char)+key)%len(rus_abs)]
        else:
            new_text+=char
    return new_text

def rot13(text: str, decrypt: bool = False)->str:
    '''
    Encrypts text by shifting letters in the alphabet with key=13
    '''
    return caesar_code(text:str, key:int = 13, decrypt:bool = decrypt)