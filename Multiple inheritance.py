class Employee:
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        print (f"The Name is {self.name} salary is {self.salary} and Role is {self.role}")

class Player:
    def __init__(self, game, level):
        self.game = game
        self.level = level

    def print_game_details(self):
        print (f" Game is {self.game} level is {self.level}")

class Student(Player,Employee):
    # def __init__(self):
    #     super().__init__()
    #     print ("student class constructor")
    pass


karan = Student("football","beginner")
karan.print_game_details()




