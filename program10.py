class Course:

    def __init__(self, c_id=0, c_name="", c_dur=""):
        self.c_id, self.c_name, self.c_dur = c_id, c_name, c_dur

    def disp_course(self):
        print(f"Course ID: {self.c_id}\nCourse Name: {self.c_name}\nDuration: {self.c_dur}")


class Student(Course):

    def __init__(self, cid, cnm, cdu, rno, sn, ag):
        super().__init__(cid, cnm, cdu)
        self.rollno, self.s_name, self.age = rno, sn, ag

    def display(self):
        print(f"Roll No: {self.rollno}\nStudent Name: {self.s_name}\nAge: {self.age}")
        self.disp_course()


s1 = Student(2874, "M.Sc.,IT", "2 Years", 113, "Ezhilarasan.S", 22)

print("Course Details")
s1.disp_course()

print("\nStudent Details")
s1.display()


