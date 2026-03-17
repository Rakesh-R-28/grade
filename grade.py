sub1 = int(input("Enter subject 1 marks: "))
sub2 = int(input("Enter subject 2 marks: "))
sub3 = int(input("Enter subject 3 marks: "))

class Grade:
    def __init__(self, sub1, sub2, sub3):
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3

    def average(self):
        avg = (self.sub1 + self.sub2 + self.sub3) / 3
        return avg

    def grade(self):
        avg = self.average()

        if avg >= 90:
            print("Grade: A")
        elif 75 <= avg < 90:
            print("Grade: B")
        elif 50 <= avg < 75:
            print("Grade: C")
        else:
            print("Fail")


A = Grade(sub1, sub2, sub3)

print("Average:", A.average())
A.grade()