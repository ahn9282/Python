class studentANN:
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address

    def __call__(self, score):
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        else:
            return 'F'

steve = studentANN(1, "hi","seoul")
print(steve)
for i in range(0,3):
    if i == 0:
        print(steve.id)
    if i == 1:
        print(steve.name)
    if i == 2:
        print(steve.address)
print("steve's Grade", steve(95))