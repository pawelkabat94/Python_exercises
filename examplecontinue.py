persons=['Elizabeth','Mark@company.com','Rust','Corey','Barbara@company.com','Martin']

domain = '@company.com'
emails = []

for person in persons:
    if '@' in person:
        emails.append(person)
        continue

    email = person + domain
    emails.append(email)

print(emails)
