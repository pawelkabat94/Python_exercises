DevOps = ["AWS", "Python", "Jenkins", "Docker", "Linux", "Maven", "CI/CD"]
Development = ("Java", "JavaScript", ".net", "nodeJS")
employee1 = {"Name":"Pawel","Skill":"QA Tester" }
employee2 = {"Name":"Michal", "Skill":"CloudDeveloper"}

skill = input("Please enter your desired skill:")

if skill in DevOps:
    print(f"We have {skill} in DevOps Department.")
elif skill in Development:
    print(f"We have {skill} in Development Department.")
elif (skill in employee1.values()) or (skill in employee2.values()):
    print(f"We have {skill}, but in different department.")
else:
    print("Unfortunately, we don't have this skill.")
