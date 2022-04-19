def replace_stars():
    answer = ""
    global word 

    for letter in word:
        if letter == "*":
            answer += " . "
        else:
            answer +- letter

    word = "a*b*c*d*"
    replace_stars()
    print(word)