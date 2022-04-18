class Player:
    def __init__(self):
        self.name ="dhoni"
        self.run=678
        print("player initilaized")

    def get_details(self):

        print(f"name = {self.name}\n run={self.run}")

print("-"*40)
ply1=Player()
ply1.get_details()
print("-"*40)
ply2=Player()
ply2.name="Rohith"
ply2.run=567
ply2.get_details()
# def fun5(x, y):
#     print(f"I am from fun5 {x} {y}")
#
# fun5(678, 567)