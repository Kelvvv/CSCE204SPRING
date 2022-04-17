#Author: Kelvin Keller
def to_symbols(message):
    for letter in message:
        print(str(ord(letter)))
    return letter


def to_letters(symbols):
    for symbol in symbols:
        print(chr(int(symbol.strip())))
    return symbol

#interface 
print("Secret Messages!!!")
question = input("(E)ncode, (D)ecode, or (Q)uit: ").lower().strip()

while True:
    if question == "e":
        encode = input("Enter a secret message: ")
        print(f"Your encoded message is: {to_symbols(encode)}")
    elif question == "d":
        decode = input("Enter an encoded message: ")
        print(f"Your encoded message is: {to_letters(decode)}")
    else:
        print("Goodbye")
        break
