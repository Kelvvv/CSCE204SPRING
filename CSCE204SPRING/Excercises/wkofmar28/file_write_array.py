friends = ["Amy", "Beth","Carl","Dave"]

with open("Excercises/wkofmar28/friends.txt","w") as file:
    for friend in friends:
        file.write(f"{friend}\n")