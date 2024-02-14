# Muzaffer Berke Savaş
import sys
inputfile = open(sys.argv[1],"r")
outputfile = open("output.txt","w")
lines = inputfile.readlines()
inputfile.close()
categories = {}

def f_createcategory(lineinfo):
    categoryname = lineinfo[1]
    row = int(lineinfo[2].split("x")[0])
    column = int(lineinfo[2].split("x")[1])
    if categoryname in categories:
        outputfile.write("WARNING:  Cannot create the category for the second time. The stadium has already "+str(categoryname)+"."+"\n")
        print("WARNING:  Cannot create the category for the second time. The stadium has already "+str(categoryname)+".")
    else:
        category = [["X" for column in range(column)]for row in range(row)]
        categories[categoryname] = category
        outputfile.write("The category "+"'"+str(categoryname)+"'"+" having "+str(row*column)+" seats has been created."+"\n")
        print("The category "+"'"+str(categoryname)+"'"+" having "+str(row*column)+" seats has been created.")

def f_sellticket(lineinfo):
    customername = lineinfo[1]
    tickettype = lineinfo[2]
    categoryname = lineinfo[3]
    category = categories[categoryname]
    R = len(category)
    C = len(category[0])
    for index in range(4,len(lineinfo)):
        seat = lineinfo[index]
        row = seat[0]
        row = R - (ord(row) - ord('A')) - 1
        if "-" in seat:
            l = int(seat[1::].split("-")[0])
            r = int(seat[1::].split("-")[1])
            for col in range(l, r+1):
                if row < 0 and col >= len(category[0]):
                    outputfile.write("Error:  The category "+"'"+str(categoryname)+"'"+" has less row and column than the specified index "+str(seat)+"!"+"\n")
                    print("Error:  The category "+"'"+str(categoryname)+"'"+" has less row and column than the specified index "+str(seat)+"!")
                    break
                elif col >= len(category[0]):
                    outputfile.write("Error:  The category "+"'"+str(categoryname)+"'"+" has less column than the specified index "+str(seat)+"!"+"\n")
                    print("Error:  The category "+"'"+str(categoryname)+"'"+" has less column than the specified index "+str(seat)+"!")
                    break
                elif row < 0:
                    outputfile.write("Error:  The category "+"'"+str(categoryname)+"'"+" has less row than the specified index "+str(seat)+"!"+"\n")
                    print("Error:  The category "+"'"+str(categoryname)+"'"+" has less row than the specified index "+str(seat)+"!")
                    break

            try:
                for col in range(l, r + 1):
                    if category[row][col] != 'X':
                        outputfile.write("Warning:  The seats " + str(seat) + " cannot be sold to " + str(customername) + " due some of them have already been sold!" + "\n")
                        print("Warning:  The seats " + str(seat) + " cannot be sold to " + str(customername) + " due some of them have already been sold!")
                        raise ValueError
                for col in range(l, r+1):
                    if tickettype == "full":
                        category[row][col] = "F"
                    elif tickettype == "student":
                        category[row][col] = "S"
                    elif tickettype == "season":
                        category[row][col] = "T"
                outputfile.write("Succes:  " + str(customername) + " has bought " + str(seat) + " at " + str(categoryname) + "\n")
                print("Succes:  " + str(customername) + " has bought " + str(seat) + " at " + str(categoryname))
            except:
                pass
        else:
            col = int(seat[1:])
            if row < 0 and col >= len(category[0]):
                outputfile.write("Error:  The category "+"'"+str(categoryname)+"'"+" has less row and column than the specified index "+str(seat)+"!"+"\n")
                print("Error:  The category "+"'"+str(categoryname)+"'"+" has less row and column than the specified index "+str(seat)+"!")
                break
            elif col >= len(category[0]):
                outputfile.write("Error:  The category "+"'"+str(categoryname)+"'"+" has less column than the specified index "+str(seat)+"!"+"\n")
                print("Error:  The category "+"'"+str(categoryname)+"'"+" has less column than the specified index "+str(seat)+"!")
                break
            elif row < 0:
                outputfile.write("Error:  The category "+"'"+str(categoryname)+"'"+" has less row than the specified index "+str(seat)+"!"+"\n")
                print("Error:  The category "+"'"+str(categoryname)+"'"+" has less row than the specified index "+str(seat)+"!")
                break

            try:
                if category[row][col] != 'X':
                    outputfile.write("Warning:  The seat " + str(seat) + " cannot be sold to " + str(customername) + " since it was already sold!" + "\n")
                    print("Warning:  The seat " + str(seat) + " cannot be sold to " + str(customername) + " since it was already sold!")
                    raise ValueError
                if tickettype == "full":
                    category[row][col] = "F"
                elif tickettype == "student":
                    category[row][col] = "S"
                elif tickettype == "season":
                    category[row][col] = "T"
                outputfile.write("Succes:  " + str(customername) + " has bought " + str(seat) + " at " + str(categoryname) + "\n")
                print("Succes:  " + str(customername) + " has bought " + str(seat) + " at " + str(categoryname))
            except:
                pass

def f_cancelticket(lineinfo):
    categoryname = lineinfo[1]
    category = categories[categoryname]
    for index in range(2,len(lineinfo)):
        seat = lineinfo[index]
        row = seat[0]
        col = int(seat[1:])
        R = len(category)
        row = R - (ord(row) - ord('A')) - 1
        if True:
            if row < 0 and col >= len(category[0]):
                outputfile.write("Error:  The category " + "'" + str(categoryname) + "'" + " has less row and column than the specified index " + str(seat) + "!" + "\n")
                print("Error:  The category " + "'" + str(categoryname) + "'" + " has less row and column than the specified index " + str(seat) + "!")
                break
            elif col >= len(category[0]):
                outputfile.write("Error:  The category " + "'" + str(categoryname) + "'" + " has less column than the specified index " + str(seat) + "!" + "\n")
                print("Error:  The category " + "'" + str(categoryname) + "'" + " has less column than the specified index " + str(seat) + "!")
                break
            elif row < 0:
                outputfile.write("Error:  The category " + "'" + str(categoryname) + "'" + " has less row than the specified index " + str(seat) + "!" + "\n")
                print("Error:  The category " + "'" + str(categoryname) + "'" + " has less row than the specified index " + str(seat) + "!")
                break
        if category[row][col] == 'X':
            outputfile.write("Error:  The seat "+str(seat)+" at "+"'"+str(categoryname)+"'"+" has already been free! Nothing to cancel"+"\n")
            print("Error:  The seat "+str(seat)+" at "+"'"+str(categoryname)+"'"+" has already been free! Nothing to cancel")
            return
        category[row][col] = 'X'
        outputfile.write("Succes:  The seat "+str(seat)+" at "+"'"+str(categoryname)+"'"+" has been canceled and now ready to sell again"+"\n")
        print("Succes:  The seat "+str(seat)+" at "+"'"+str(categoryname)+"'"+" has been canceled and now ready to sell again")

def f_showcategory(lineinfo):
    categoryname = lineinfo[1]
    category = categories[categoryname]
    R = len(category)
    C = len(category[0])
    outputfile.write("Printing category layout of "+str(categoryname)+"\n"+"\n")
    print("Printing category layout of "+str(categoryname)+"\n")
    for row in range(R):
        currentRowLetter = chr(ord('A') + (R - row - 1))
        outputfile.write(currentRowLetter + ' ')
        print(currentRowLetter + ' ',end="")
        for col in range(C):
            outputfile.write(category[row][col] + '  ')
            print(category[row][col] + '  ',end="")
        outputfile.write('\n')
        print()

    for col in range(C):
        outputfile.write(' ' * (3 - len(str(col))) + str(col))
        print(' ' * (3 - len(str(col))) + str(col),end="")
    outputfile.write('\n')
    print()

def f_balance(lineinfo):
    categoryname = lineinfo[1]
    category = categories[categoryname]
    R = len(category)
    C = len(category[0])
    student = 0
    full = 0
    season = 0
    for row in range(R):
        for col in range(C):
            if category[row][col] == 'F':
                full = full + 1
            elif category[row][col] == 'S':
                student = student + 1
            elif category[row][col] == 'T':
                season = season + 1
    revenues = 20 * full + 10 * student + 250 * season
    outputfile.write("Category report of "+"'"+str(categoryname)+"'"+"\n"+32*"-"+"\n"+f"Sum of students = {student}, Sum of full pay = {full}, Sum of season ticket = {season}, and Revenues = {revenues} Dollars"+"\n")
    print("Category report of "+"'"+str(categoryname)+"'"+"\n"+32*"-"+"\n"+f"Sum of students = {student}, Sum of full pay = {full}, Sum of season ticket = {season}, and Revenues = {revenues} Dollars")




for line in lines:
    lineinfo = line.split(" ")
    lineinfo[-1]=lineinfo[-1].rstrip("\n")
    command = lineinfo[0]
    if command == 'CREATECATEGORY':
        f_createcategory(lineinfo)
    elif command == 'SELLTICKET':
        f_sellticket(lineinfo)
    elif command == 'CANCELTICKET':
        f_cancelticket(lineinfo)
    elif command == 'SHOWCATEGORY':
        f_showcategory(lineinfo)
    elif command == 'BALANCE':
        f_balance(lineinfo)
    else:
        outputfile.write("Invalid command!")
        print("Invalid command!")
outputfile.close()

