
database = []
words = input("Enter a word: ")
database.append(words)
yesChoice = 'yes'
noChoice = 'no'
while True:
    question = input("Do you want to try again? yes/no: ").lower()
    if question == yesChoice :
        words = input("Enter a word: ")
        database.append(words)
        continue
    elif question == noChoice :
        print ('Total number of words: ' ,len(database))
        print ('Words in list: '  + str(database))
        break
    else:
        print ('Enter either yes/no')
