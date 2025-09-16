
def rem(l, word):
    n= []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n



l = ["Deepanshu", "Rahul", "Drea", "Xyz"]

print(rem(l, "Xyz"))