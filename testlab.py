class E:
    allE = []

    def __init__(self):
        self.allE.append(self)

m1 = E()
m2 = E()

print(m1.allE)