# Generate a CSV with information for 50,000 fake persons

import mimesis
import csv
import random

person = mimesis.Person(locale='en')
genderEnum = mimesis.enums.Gender

with open('persons.csv', mode='w', newline='\n', encoding='utf-8') as person_file:
    writer = csv.writer(person_file)
    
    # Header Row
    writer.writerow(['Id', 'Full Name', 'Age', 'Occupation', 'Email', 'Telephone',
        'Nationality'])
    
    for i in range(0, 50000):
        rando = random.uniform(0, 1)
        if rando >= 0.5:
            gender = genderEnum.FEMALE
        else:
            gender = genderEnum.MALE
                
        row = [
            i,
            person.full_name(gender=gender),
            person.age(),
            person.occupation(),
            person.email(),
            person.telephone(),
            person.nationality()
        ]
        writer.writerow(row)