import os

class Client:
    def __init__(self, num, name, date, time, adults, child):
        self.reservNum = num
        self.cusName = name
        self.dateRes = date
        self.timeRes = time
        self.adultNum = adults
        self.childNum = child

    def getClient(self):
        return ("%d\t\t\t\t\t%s\t\t\t\t\t%s\t\t\t\t\t%s\t\t\t\t\t%d\t\t\t\t\t\t%d\t\n" % (self.reservNum, self.cusName, self.dateRes, self.timeRes, self.adultNum, self.childNum))


def view(file):
    checker(file)
    f = open(checker(file), "r")
    print(f.read())
    f.close()


def checker(n):
    try:
        N = n
    except ZeroDivisionError:
        print("ERROR: 0 unaccepted value")
    except FileNotFoundError as fError:
        print(fError)
    except:
        print("ALERT: invalid value!")
    else:
        return N


def clearALL():
    resFile = open("reservations.txt", "w")
    resFile.write("#\t\t\t\t\tName\t\t\t\t\tDate\t\t\t\t\tTime\t\t\t\t\tAdults\t\t\t\t\tChildren\n------------------------------------------------------------------------------------------------------------------------------\n")
    resFile.close()

def menu():
    print("\t\tSystem Menu:")
    print("\t[A]. View all reservations\n\t[B]. Make Reservation\n\t[C]. Delete Resevation\n\t[D]. Generate Report\n\t[E]. Exit")


customer = {}
reserve = {}
ctr = 1
clearALL()
while True:
    print("=============== RESTAURANT RESERVATION SYSTEM===============")
    try:
        menu()
        opt = str(input("Enter your option: ").upper())
    except:
        print('Invalid input')
    else:
        if opt == 'A':
            view("reservations.txt")
        elif opt == 'B':
            print("--------------------------------------------------------")
            name = checker(str(input("Name: ").title()))
            date = checker(str(input("Date: ")))
            time = checker(str(input("Time: ")))
            adults = checker(int(input("Number of Adult: ")))
            children = checker(int(input("Number of children: ")))
            resFile = open("reservations.txt", "a")
            customer[ctr] = checker(Client(int(ctr), name, date, time, adults, children))
            reserve[ctr] = customer[ctr]
            resFile.write(customer[ctr].getClient())
            print("RESERVATION DONE!")
            resFile.close()
            ctr += 1
        elif opt == 'C':
            resNumber = checker(int(input("Choose Transaction Number to remove? ")))
            del reserve[resNumber]
            clearALL()
            print(f"You have successfully deleted transaction number {resNumber}!")
            for r in reserve.values():
                resFile = open("reservations.txt", "a")
                resFile.write(r.getClient())
                resFile.close()
        elif opt == 'D':
            total = 0
            TotalAdults = 0
            TotalChildren = 0
            print("#\t\t\t\t\tName\t\t\t\t\tDate\t\t\t\t\tTime\t\t\t\t\tAdults\t\t\t\t\tChildren\n-----------------------------------------------------------------------------------\n")
            for r in reserve.values():
                total = checker(total + float((r.childNum * 300) + (r.adultNum * 500)))
                TotalAdults = checker(int(TotalAdults + r.adultNum))
                TotalChildren = checker(int(TotalChildren + r.childNum))
                print("%stotal|%1.f\n" % (r.getClient(), float((r.childNum * 300) + (r.adultNum * 500))))

            print("Total number of adults: %d" % TotalAdults)
            print("Total number of children: %d" % TotalChildren)
            print("Grand Total: %1.f" % total)
            print("------------------------------------NOTHING FOLLOWS---------------------------------------")
        elif opt == 'E':
            break
        else:
            print('ALERT: entered value is not in the options!')

    finally:
        print('-------------------------------------------------------------')
print("\t\t\tThank you!")

os.remove("reservations.txt")