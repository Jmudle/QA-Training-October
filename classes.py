class Student():
    def __init__(self, name, age, classroom,):
        self.name = name
        self.age = age
        self.cl = classroom
        self.testscores = []
        
    def add_test_scores(self, score):
            self.testscores.append(score)
    def average_test_scores(self):
        
        self.averagescore = sum(self.testscores) / len (self.testscores)
        return self.averagescore  

    def __repr__(self):
        return Student

stud1 = Student("John", 22, "Ladybugs")
stud1.add_test_scores(85)
stud1.add_test_scores(67)
stud1.add_test_scores(98)

stud2 = Student("James", 23, "Bananas")
stud2.add_test_scores(56)
stud2.add_test_scores(67)
stud2.add_test_scores(34)


print(f"Name:{stud1.name}, Age:{stud1.age}, Classroom:{stud1.cl} Test Scores:{stud1.testscores} Average Score:{stud1.averagescore}")
print(f"Name:{stud2.name}, Age:{stud2.age}, Classroom:{stud2.cl}, Test Scores:{stud2.testscores} Average Score:{stud2.averagescore}")

        
        