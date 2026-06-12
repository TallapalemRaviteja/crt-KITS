class Student:
    def __init__(self, student_id, student_name, attendance):
        self.student_id = student_id
        self.student_name = student_name
        self.attendance = attendance


class Assessment:
    def __init__(self, assessment_score):
        self.assessment_score = assessment_score


class PlacementManager:
    def __init__(self):
        self.students = []

    def add_student(self, student, assessment):
        self.students.append((student, assessment))

    def check_eligibility(self, student, assessment):
        return student.attendance >= 75 and assessment.assessment_score >= 60

    def generate_report(self):
        print("=" * 50)
        print("          PLACEMENT ELIGIBILITY REPORT")
        print("=" * 50)

        for student, assessment in self.students:
            status = "Eligible" if self.check_eligibility(student, assessment) else "Not Eligible"

            print(f"\nStudent ID       : {student.student_id}")
            print(f"Student Name     : {student.student_name}")
            print(f"Attendance       : {student.attendance}%")
            print(f"Assessment Score : {assessment.assessment_score}")
            print(f"Placement Status : {status}")
            print("-" * 50)


# Input
student_id = input("Student ID      : ")
student_name = input("Student Name    : ")
attendance = int(input("Attendance      : "))
assessment_score = int(input("Assessment Score: "))

# Objects
student = Student(student_id, student_name, attendance)
assessment = Assessment(assessment_score)

manager = PlacementManager()
manager.add_student(student, assessment)

# Report
manager.generate_report()