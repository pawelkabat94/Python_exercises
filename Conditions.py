print("Our company offers various skills for both DevOps Department and Development Department.")


DevOps = ("AWS", "CI/CD", "IAAC", "Linux", "Bash Scripting")
Development = ["Java", "Ruby", ".net"]
employee1 = {"Name": "Jason", "Department": "1", "Skill": "Blockchain"}
employee2 = {"Name": "Mike", "Department": "2", "Skill": "DataScience"}

Skill = input("Enter your desired skill: ")

if (Skill in DevOps):
    print(f"We have {Skill} in our DevOps Department.")
elif (Skill in Development):
    print(f"We have {Skill} in our Development Department.")
elif (Skill in employee1.values()) or (Skill in employee2.values()):
    print(f"We have a employee with {Skill} in our company from different department.")
else:
    print("We don't have this skill in our company.")
