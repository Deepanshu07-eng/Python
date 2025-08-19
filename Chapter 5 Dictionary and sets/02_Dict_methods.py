marks = {
    "Deepanshu" : 93,
    "Shubham" : 87,
    "Karan" : 67,
    79 : "shivani",

}

#print(marks.items())
#print(marks.keys())
#print(marks.value())
#marks.update({"Karan" : 61, "Shivani" : 87})
#print(marks)

print(marks.get("DeepanshuG")) #Prints None
print(marks["DeepanshuG"]) # Return an error