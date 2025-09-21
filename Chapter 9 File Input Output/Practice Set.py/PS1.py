f = open("text.txt")

c = f.read()

if ("play" in c):
    print("the word play is present in the content")

else:
    print("The word play is not present in the content")

f.close()