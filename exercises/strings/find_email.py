"""
Print the name, email, organization website and job_title of the contacts below.
"""

contacts = [
    "Paulo Amosse Cuambe, pcuambe@inove.it, Software Engineer",
    "Mariana Leonel Xavier, mariana@gosen.co.mz, Software Consultant",
    "Marcelo Vieira Lemos, marcelo.v.lemos@codinglabs.co.mz, Data Analyst",
    "Mirela Hugo Junior, hmirela@vale.co.mz, Human Resources",
    "Celeste Armando Khuniza, cel.khuniza@edm.co.mz, Electronic Engineer",
]

for contact in contacts:
    [name, email, job_title] = contact.split(', ')
    website = email[email.find('@') + 1:]
    print()
    print(
        f"Name: {name} \nEmail: {email} \nJob Title: {job_title} \nWebsite: {website}"
    )
