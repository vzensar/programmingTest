class Player:
    def __init__(self):
        self.name ="sachin"
        self.age=88
        print("player initilaized")

    def get_details(self):

        print(f"name = {self.name}\n age={self.age}")


ply1=Player()
ply1.get_details()
print("-"*40)
ply2=Player()
ply2.name="suarav"
ply2.age=77
ply2.get_details()
# def fun4(x, y):
#     print(f"fun4 ..... {x} {y}")
#
# fun4(88, 77)