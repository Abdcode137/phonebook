import sys
def intial_phonebook():
    rows, cols=int(input("Enter the number of initial contacts:")), 5
    phonebook = [   ]
    print(phonebook)
    for i in range(rows):
        print("Note: * means the field is mandatory")
        print("...................................................................................................................................")
    temp = 0
    for j in range(cols):
            if j == 0:
                temp.append(str(input("Enter the Name*:")))
                if temp[j] == '' or temp[j]==' ':
                    sys.exit("Name is a mandatory field process exit due to empty field")
            if j == 1:
                temp.append(int(input("Enter the Mobile Number*:")))
            if j == 2:
                temp.append(str(input("Enter the E-mail Address:")))
                if temp[j] == '' or temp[j]==' ':
                    temp[j] = None
            if j == 3:
                temp.append(str(input("Enter the date of birth (dd/mm/yy):")))
                if temp[j] == '' or temp[j]==' ':
                    temp[j] = None
            if j == 4:
                temp.append(str(input("Enter the category (Family/Friends/Workers/Others):")))
                if temp[j] == '' or temp[j]==' ':
                    temp[j] = None
            phonebook.append(temp)
            print(phonebook)
            return phonebook                                     
def menu():
    print("*****************************************************************************************************************")
    print("\t\t\tSmartphone Directory", flush= False)
    print("*****************************************************************************************************************")
       