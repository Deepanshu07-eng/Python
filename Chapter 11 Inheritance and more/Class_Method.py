class employee:
    a =13
    @classmethod  #CLASS METHOD
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = employee()
e.a = 21

e.show()

# Instead of writing 'self', write 'cls',  now it will print the actual attribute or value