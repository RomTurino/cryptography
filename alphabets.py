from string import ascii_lowercase, punctuation
eng_abs = ascii_lowercase
rus_abs = ''.join([chr(char) for char in range(ord('а'), ord('я')+1)])
non_letters = punctuation+' '+'/n'

