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
    def change_name(self, new_name):
        self.name = new_name
        print(f"changed name to {new_name}")

    def change_age(self, new_age):
        self.age = new_age

    def add_track(self, new_track):
        self.tracks.append(new_track)
        print(f"this {new_track} has been added")

    def get_score(self):
        return self.score


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods0
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
print(Bob.get_score())
