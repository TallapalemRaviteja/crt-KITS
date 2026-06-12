class Candidate:
    def __init__(self, name, skills):
        self.name = name
        self.skills = set(skills)

class Job:
    def __init__(self, title, req_skills):
        self.title = title
        self.req_skills = set(req_skills)

c = Candidate("Ravi", ["Python", "SQL"])
job = Job("Developer", ["Python", "SQL"])

scores = {"Ravi": 85}

if job.req_skills.issubset(c.skills) and scores["Ravi"] >= 70:
    print("Selected")
else:
    print("Rejected")