message = "messi is the greatest footballer of all time."
print(message.capitalize())

print(message.__dir__())

print(dir(message))

print(message.upper())

print(message.isnumeric())

print(message.find("essi"))

seq1=("AWS","Python","Bash")
print("/".join(seq1))

footballers = ["Messi", "Ronaldo", "Pele", "Maradona", "Cruyff", "Beckenbauer", "Zidane", "Iniesta", "Platini", "Di Stefano"]
print(footballers)

footballers.append("Cristiano Ronaldo")
print(footballers)

footballers.extend(["Van Basten", "Buffon", "Eusebio"])
print(footballers)

footballers.pop(11)
print(footballers)