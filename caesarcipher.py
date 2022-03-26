#I want to compare the two list elements, derive the index of alphlist, decrement it
# and then provide that value in place to stringlist, and then recreate string
string = "skyler"
offset = 2
alphlist = ["a", "b", "c", "d", "e", "f",
            "g", "h", "i", "j", "k",
            "l", "m", "n", "o", "p",
            "q","r", "s", "t", "u",
            "v","w", "x", "y", "z"]
stringlist= []
for idx in range(len(string)):
    stringlist.append(string[idx])

for idx, letter in enumerate(alphlist):
    for i, char in enumerate(stringlist):
        if letter == char:
            stringlist[i] = alphlist[idx-offset]

    
a = ""
string = a.join(stringlist)
print(string)