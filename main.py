

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo
print(logo)

continue_program = True
  

def ceaser(txt, shift_num, direct):
  updated_text = ""
  for char in txt: 
    if char in alphabet:
      position = alphabet.index(char)
      if direct == 'encode':
        new_pos = position + shift_num
      elif direct == 'decode':
        new_pos = position - shift_num
      new_char = alphabet[new_pos]
      updated_text += new_char
    else:
      updated_text += char

  print(f"The {direct}d text is {updated_text}")

while continue_program:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  ceaser(txt= text, shift_num=shift, direct=direction)
  answer = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
  if answer == 'no':
    print("Goodbye")
    continue_program = False
  


