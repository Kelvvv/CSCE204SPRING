import random 

#email: jsmith@use.edu, username: jsmith
def get_username(email):
    return email.split("a")[0]

#create a password
def get_password(phrase):
   answer = ""
    char_conversion = {
        "a":"@",
        "b":"8",
        "e":"3",
        "g":"9",
        "i":"!",
        "o":"0",
        "s":"$",
        "t":"7",
    }

    for letter in phrase:
        if letter.lower() in char_conversion:
            answerr += char_conversion[leter.lower()]
        else:
            answer += maybe_capitalize(letter)
    
    return password + str(random.randint(0,100))

def maybe_capitalize(letter):
    if random.randint(0,2) == 0:
        return letter.upper()
    else:
        return letter.lower()

print("Username and password program")
email = input("enter email: ")
username = get_username(email)
print(f"username is {username}")

phrase = input("emter phrase:")
print("Username and password program")
email = input("Enter email: ")