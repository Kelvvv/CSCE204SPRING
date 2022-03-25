def getFriends():
    friends = []
    with open("Excercises/wkofmar21/friends.txt") as file: #opening up the friends text file 
        for line in file: #for every line in the txt file 
            friend = line.replace("\n","")
            friends.append(friend)
        return friends

people = getFriends()

print("See my friends:")

for i in range(len(people)):
    print(f"{i+1}. {people[i]}")