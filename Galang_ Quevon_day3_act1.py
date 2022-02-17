#Quevon M. Galang

Name = input("Name: ")
Math = input("Math: ")
Science = input ("Science: ")
English = input ("English: ")
Average = float(Math) + float(Science) + float(English)
TotalAverage = float(Average) / 3
Round_average = round(TotalAverage, 2)


print("Name: " + Name)
print("Math: " + str(Math))
print("Science: " + str(Science))
print("English: " + str(English))
print("Average: " + str(Round_average))



if float(Math) < 75 and float(TotalAverage) >= 75 <= float(Science) and 75 <= float(English):
    print("\nCongratulations! You passed the semester. But you need to re-enroll Math Subject")
elif float(Science) < 75 and float(TotalAverage) >= 75 <= float(Math) and 75 <= float(English):
    print("\nCongratulations! You passed the semester. But you need to re-enroll Science Subject")
elif float(English) < 75 and float(TotalAverage) >= 75 <= float(Science) and 75 <= float(Math):
    print("\nCongratulations! You passed the semester. But you need to re-enroll English Subject")
elif float(Science)  < 75 and float(Math) < 75 < float(TotalAverage):
    print("\nCongratulations! You passed the semester. But you need to re-enroll Math and Science Subjects")
elif float(Math)  < 75 and float(English) < 75 < float(TotalAverage):
    print("\nCongratulations! You passed the semester. But you need to re-enroll Math and English Subjects")
elif float(Science) < 75 and float(English) < 75 < float(TotalAverage):
    print("\nCongratulations! You passed the semester. But you need to re-enroll Science and English Subjects")
elif float(TotalAverage) >=75:
    print("\nCongratulations! You passed the semester")
elif float(TotalAverage) < 75:
    print("\nSorry,You failed the semester")






