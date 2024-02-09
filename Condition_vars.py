"""
This script will implement our knowledge on
conditions and different datatypes.
"""
print("This IT Organization has various skill sets.")
print("Find out your match.")

print("Enter Capitalised Values: ")

DevOps = ["Jenkins", "Ansible", "Bash", "Python", "Puppet", "Dockers", "Kubernetes", "Terraform"]
Development = ("Nodejs", "Angularjs", "Java", ".net", "Python")
cntr_emp1 = {"Name":"Santa", "Skill":"Blockchain", "Code":1024}
cntr_emp2 = {"Name":"Rocky", "Skill":"AI", "Code":1218}

usr_skill = input("Enter your desired skill: ")
#print(usr_skill)

# Check in the database if we have this skill
if usr_skill in DevOps:
    print(f"We Have {usr_skill} in DevOps Team.")
elif (usr_skill in Development):
    print(f"We have {usr_skill} in Development Team.")
elif (usr_skill in cntr_emp1.values()) or (usr_skill in cntr_emp2.values()):
    print(f"We have contract employees with {usr_skill} skill.")
else:
    print("Skill not found")
    print("Please check if you have entered value in capitalize or check the spelling.")


# my conditions Pawel

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