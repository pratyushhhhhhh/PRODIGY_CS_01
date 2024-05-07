def encrypt(text, s):
  result = ""
  for char in text:
    if char.isalpha():
      if char.isupper():
        result += chr((ord(char) + s - 65) % 26 + 65)
      else:
        result += chr((ord(char) + s - 97) % 26 + 97)
    else:
      result += char
  return result
def main():
  text = input("Enter the text to encrypt: ")
  while True:
    try:
      s = int(input("Enter the shift value (1-25): "))
      if 1 <= s <= 25:
        break
      else:
        print("Invalid shift value. Please enter a number between 1 and 25.")
    except ValueError:
      print("Invalid input. Please enter a number for the shift value.")

  encrypted_text = encrypt(text, s)
  print("Original Text:", text)
  print("Shift Value:", s)
  print("Encrypted Text:", encrypted_text)

if __name__ == "__main__":
  main()
