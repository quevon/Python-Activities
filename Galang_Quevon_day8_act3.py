class Students:
    def __init__(self, name , math, science, english, Average):
        self.myname = name
        self.mymath = math
        self.myscience = science
        self.myenglish = english
        self.average = Average

    def computation(self):
        self.average = int(self.mymath) + int(self.myscience) + int(self.myenglish)
        Average1 = int(self.average) / 3
        print('Average: ' , Average1 , '(Passed)' )
    def Display(self):
        print('Name: ', self.myname)
        print('Math: ', self.mymath)
        print('Science: ', self.myscience)
        print('English: ', self.myenglish)

stud = Students('Quevon M. Galang', "90" , '90' ,'90', '' )
stud.Display()
stud.computation()






