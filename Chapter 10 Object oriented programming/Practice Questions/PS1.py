class programmer :
    company = "Microsoft"

    def __init__(self, name, skill,  salary, pin):
        self.name = name
        self.skill = skill
        self.salary = salary
        self.pin = pin



p = programmer("Deepanshu", "python",  1500000, 29324134)
print(p.name, p.company, p.skill, p.salary, p.pin)

r = programmer("Rahul", "C++",  1400000, 42524142)
print(r.name, r.company, r.skill, r.salary, r.pin)