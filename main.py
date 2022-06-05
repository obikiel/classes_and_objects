class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,age,tracks,score, name):
        self.age = age
        self.tracks = tracks
        self.score = score
        self.name = name
        print (f"My name is {name},I am {age} years old and I am in the {tracks} with a score of {score} ")
        pass
        #methods
    def changes (self,change_name,change_age,add_track,get_score):
        self.change_name = "Peter"
        self.change_age = 34
        self.add_track = "UI/UX"
        self.get_score = self.score 


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods0
print(Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
