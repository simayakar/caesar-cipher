alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceaser(txt, shift_num, direct):
  updated_text = ""
  for letter in txt: 
    position = alphabet.index(letter)
    if direct == 'encode':
      new_pos = position + shift_num
    elif direct == 'decode':
      new_pos = position - shift_num
    new_letter = alphabet[new_pos]
    updated_text += new_letter
  print(f"The {direct}d text is {updated_text}")

ceaser(txt= text, shift_num=shift, direct=direction)
