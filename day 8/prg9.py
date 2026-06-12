class Student:
  def placement_eligibility(self):
    print("Placement Eligibility: Assessment Score Above 60")
class AdvStudent(Student):
  def placement_eligibility(self):
    print("Placement Eligibility: Assessment Score Above 80")
adv =AdvStudent()
adv.placement_eligibility()