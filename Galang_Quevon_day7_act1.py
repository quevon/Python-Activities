import random

firstname = ['Quevon','Josh','Jen','Ben','Chieny','Art','Paul','Niko','Renato','Jake']
middlename = ['A.','B.','C.','D.','E.','F.','G.','H.','I.','J.']
lastname = ['Galang', 'Faa', 'Diva', 'Romero', 'Martino','Rollo','Mendez','Calvo','Galicia','Veneracion']
name = []

yesChoice = 'y'
noChoice = 'n'
while True:
    question = input("Generate New Name? y/n: ").lower()
    if question == yesChoice :
        list = random.choice(firstname) +" "+ random.choice(middlename) +" "+ random.choice(lastname)
        print(list)
        name.append(list)
        continue
    elif question == noChoice :
        print('Thank you! The Generated Names are: \n')
        print ('\n'.join(map(str, name)))
        break
