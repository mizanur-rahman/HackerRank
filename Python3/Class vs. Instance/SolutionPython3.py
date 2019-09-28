#Problem
'''Write a Person class with an instance variable,age, and a constructor that takes an integer,initialAge , as a parameter. The constructor must assign initialAge to age   after confirming the argument passed as  is not negative; if a negative argument is passed as initialAge, the constructor should set age to 0 and print Age is not valid, setting age to 0.. In addition, you must write the following instance methods:

yearPasses() should increase the  instance age variable by 1.
amIOld() should perform the following conditional actions:
If age<13, print You are young..
If age>= 13 and age<18, print You are a teenager..
Otherwise, print You are old..'''
# Solutions


class Person:
    def __init__(self, initialAge):
        self.age = initialAge
        if self.age < 0:
            print('Age is not valid, setting age to 0.')
            self.age = 0
            # Add some more code to run some checks on initialAge

    def amIOld(self):
        if self.age < 13:
            print('You are young.')
        elif self.age >= 13 and self.age < 18:
            print('You are a teenager.')
        else:
            print('You are old.')

        # Do some computations in here and print out the correct statement to the console

    def yearPasses(self):
        self.age += 1


t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")
