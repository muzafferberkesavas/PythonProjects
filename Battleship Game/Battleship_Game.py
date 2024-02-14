#Muzaffer Berke Savaş
import sys
def outputfunction(x):                      #This function writes into the file
    open("Battleship.out","a").write(x)
def Tableprinter():                          #This function prints table (final board included)
    print(" ",end="")
    outputfunction(" ")
    for word in letterlist:
        print(" "+str(word),end="")
        outputfunction(" "+str(word))
    print("\t\t ",end="")
    outputfunction("\t\t ")
    for word in letterlist:
        print(" "+str(word),end="")
        outputfunction(" "+str(word))
    print("\n",end="")
    outputfunction("\n")
    for number in range(1,10):
        print(number,end="")
        outputfunction(str(number))
        for element in Table1:
            if int(element.split("-")[1]) == number:
                print(" "+str(Table1[element]),end="")
                outputfunction(" "+str(Table1[element]))
        print("\t\t"+str(number),end="")
        outputfunction("\t\t"+str(number))
        for element in Table2:
            if int(element.split("-")[1]) == number:
                print(" "+str(Table2[element]),end="")
                outputfunction(" "+str(Table2[element]))
        print("\n",end="")
        outputfunction("\n")
    print("10",end="")
    outputfunction("10")
    for element in Table1:
        if int(element.split("-")[1]) == 10:
            print(str(Table1[element])+" ",end="")
            outputfunction(str(Table1[element])+" ")
    print("\t\t10",end="")
    outputfunction("\t\t10")
    for element in Table2:
        if int(element.split("-")[1]) == 10:
            print(str(Table2[element])+" ",end="")
            outputfunction(str(Table2[element])+" ")
    print("\n")
    outputfunction("\n")
try:
    player1txt = sys.argv[1]
    player2txt = sys.argv[2]
    player1in = sys.argv[3]
    player2in = sys.argv[4]
    try:
        open(player1txt,"r")
        try:
            open(player2txt,"r")
            try:
                open(player1in,"r")
                try:
                    try:
                        open(player2in,"r")
                        player1txtlines = open(player1txt,"r").readlines()
                        player2txtlines = open(player2txt,"r").readlines()
                        letterlist = ["A","B","C","D","E","F","G","H","I","J"]
                        numberlist = [1,2,3,4,5,6,7,8,9,10]
                        Table1 = {}
                        Table2 = {}
                        player1boats = {}
                        player2boats = {}
                        player1B = 0
                        player1C = 0
                        player1D = 0
                        player1S = 0
                        player1P = 0
                        player2B = 0
                        player2C = 0
                        player2D = 0
                        player2S = 0
                        player2P = 0
                        r = 0
                        Round = 1
                        BPboatsplayer1 = open("OptionalPlayer1.txt","r").readlines()
                        BPboatsplayer2 = open("OptionalPlayer2.txt","r").readlines()
                        if len(player1txtlines) < 10:
                            outputfunction("IndexError: Player1.txt line number is less than 10!\n")
                            print("IndexError: Player1.txt line number is less than 10!\n")
                            raise IndexError
                        elif len(player1txtlines) > 10:
                            outputfunction("IndexError: Player1.txt line number is greater than 10!\n")
                            print("IndexError: Player1.txt line number is greater than 10!\n")
                            raise IndexError
                        else:
                            if len(player2txtlines) < 10:
                                outputfunction("IndexError: Player2.txt line number is less than 10!\n")
                                print("IndexError: Player2.txt line number is less than 10!\n")
                                raise IndexError
                            elif len(player2txtlines) > 10:
                                outputfunction("IndexError: Player2.txt line number is greater than 10!\n")
                                print("IndexError: Player2.txt line number is greater than 10!\n")
                                raise IndexError
                            else:
                                pass
                        for line in BPboatsplayer1:
                                direction = line.rstrip("\n").split(";")[1]
                                boatnumber = line.rstrip("\n").split(";")[0].split(":")[0]
                                startingnumber = int(line.rstrip("\n").split(";")[0].split(":")[1].split(",")[0])
                                startingletter = line.rstrip("\n").split(";")[0].split(":")[1].split(",")[1]
                                if str(boatnumber) == "B1" or str(boatnumber) == "B2":
                                    if direction == "right":
                                        a = letterlist.index(str(startingletter))
                                        player1boats[boatnumber] = f"{letterlist[a]}{startingnumber},{letterlist[a+1]}{startingnumber},{letterlist[a+2]}{startingnumber},{letterlist[a+3]}{startingnumber}"
                                    elif direction == "down":
                                        player1boats[boatnumber] = f"{startingletter}{startingnumber},{startingletter}{startingnumber+1},{startingletter}{startingnumber+2},{startingletter}{startingnumber+3}"
                                elif str(boatnumber) == "P1" or str(boatnumber) == "P2" or str(boatnumber) == "P3" or str(boatnumber) == "P4":
                                    if direction == "right":
                                        a = letterlist.index(str(startingletter))
                                        player1boats[boatnumber] = f"{letterlist[a]}{startingnumber},{letterlist[a+1]}{startingnumber}"
                                    elif direction == "down":
                                        player1boats[boatnumber] = f"{startingletter}{startingnumber},{startingletter}{startingnumber+1}"
                        for line in BPboatsplayer2:
                                direction = line.rstrip("\n").split(";")[1]
                                boatnumber = line.rstrip("\n").split(";")[0].split(":")[0]
                                startingnumber = int(line.rstrip("\n").split(";")[0].split(":")[1].split(",")[0])
                                startingletter = line.rstrip("\n").split(";")[0].split(":")[1].split(",")[1]
                                if str(boatnumber) == "B1" or str(boatnumber) == "B2":
                                    if direction == "right":
                                        a = letterlist.index(str(startingletter))
                                        player2boats[boatnumber] = f"{letterlist[a]}{startingnumber},{letterlist[a+1]}{startingnumber},{letterlist[a+2]}{startingnumber},{letterlist[a+3]}{startingnumber}"
                                    elif direction == "down":
                                        player2boats[boatnumber] = f"{startingletter}{startingnumber},{startingletter}{startingnumber+1},{startingletter}{startingnumber+2},{startingletter}{startingnumber+3}"
                                elif str(boatnumber) == "P1" or str(boatnumber) == "P2" or str(boatnumber) == "P3" or str(boatnumber) == "P4":
                                    if direction == "right":
                                        a = letterlist.index(str(startingletter))
                                        player2boats[boatnumber] = f"{letterlist[a]}{startingnumber},{letterlist[a+1]}{startingnumber}"
                                    elif direction == "down":
                                        player2boats[boatnumber] = f"{startingletter}{startingnumber},{startingletter}{startingnumber+1}"
                        for line in player1txtlines:
                            a = line.rstrip("\n").split(";")
                            c = 1
                            if len(a) == 10:
                                for element in a:
                                    if element == "B":
                                        c += 1
                                        player1B += 1
                                    elif element == "C":
                                        try:
                                            if a[c] == "C" and a[c + 1] == "C" and a[c + 2] == "C" and a[c + 3] == "C":
                                                player1boats["C1"] = f"{letterlist[c-1]}{r+1},{letterlist[c]}{r+1},{letterlist[c+1]}{r+1},{letterlist[c+2]}{r+1},{letterlist[c+3]}{r+1}"
                                                c += 1
                                                player1C += 1
                                            else:
                                                raise IndexError
                                        except IndexError:
                                            try:
                                                if player1txtlines[r + 1].rstrip("\n").split(";")[c - 1] == "C" and player1txtlines[r + 2].rstrip("\n").split(";")[c - 1] == "C" and player1txtlines[r + 3].rstrip("\n").split(";")[c - 1] == "C" and player1txtlines[r + 4].rstrip("\n").split(";")[c - 1] == "C":
                                                    player1boats["C1"] = f"{letterlist[c-1]}{r+1},{letterlist[c-1]}{r + 2},{letterlist[c-1]}{r + 3},{letterlist[c-1]}{r + 4},{letterlist[c-1]}{r + 5}"
                                                    c += 1
                                                    player1C += 1
                                                else:
                                                    raise IndexError
                                            except IndexError:
                                                c += 1
                                                player1C += 1
                                                continue
                                    elif element == "P":
                                        c += 1
                                        player1P += 1
                                    elif element == "S":
                                        try:
                                            if a[c] == "S" and a[c + 1] == "S":
                                                player1boats["S1"] = f"{letterlist[c-1]}{r+1},{letterlist[c]}{r+1},{letterlist[c+1]}{r+1}"
                                                c += 1
                                                player1S += 1
                                            else:
                                                raise IndexError
                                        except IndexError:
                                            try:
                                                if player1txtlines[r + 1].rstrip("\n").split(";")[c - 1] == "S" and player1txtlines[r + 2].rstrip("\n").split(";")[c - 1] == "S":
                                                    player1boats["S1"] = f"{letterlist[c-1]}{r+1},{letterlist[c-1]}{r + 2},{letterlist[c-1]}{r + 3}"
                                                    c += 1
                                                    player1S += 1
                                                else:
                                                    raise IndexError
                                            except IndexError:
                                                c += 1
                                                player1S += 1
                                                continue
                                    elif element == "D":
                                        try:
                                            if a[c] == "D" and a[c + 1] == "D":
                                                player1boats["D1"] = f"{letterlist[c-1]}{r+1},{letterlist[c]}{r+1},{letterlist[c+1]}{r+1}"
                                                c += 1
                                                player1D += 1
                                            else:
                                                raise IndexError
                                        except IndexError:
                                            try:
                                                if player1txtlines[r + 1].rstrip("\n").split(";")[c - 1] == "D" and player1txtlines[r + 2].rstrip("\n").split(";")[c - 1] == "D":
                                                    player1boats["D1"] = f"{letterlist[c-1]}{r+1},{letterlist[c-1]}{r + 2},{letterlist[c-1]}{r + 3}"
                                                    c += 1
                                                    player1D += 1
                                                else:
                                                    raise IndexError
                                            except IndexError:
                                                c += 1
                                                player1D += 1
                                                continue
                                    elif element == "":
                                        c += 1
                                    else:
                                        outputfunction("ValueError: The character "+"'"+str(element)+"'"+"in Player1.txt is not valid character for game!\n")
                                        print("ValueError: The character "+"'"+str(element)+"'"+"in Player1.txt is not valid character for game!\n")
                                        raise ValueError
                                r += 1
                            elif len(a) < 10:
                                outputfunction(f"IndexError: for a line in Player1.txt file has less character!\n")
                                print(f"IndexError: for a line in Player1.txt file has less character!\n")
                                raise IndexError
                            else:
                                outputfunction(f"IndexError: for a line in Player1.txt file has less character!\n")
                                print(f"IndexError: for a line in Player1.txt file has less character!\n")
                                raise IndexError
                        r = 0
                        for line in player2txtlines:
                            a = line.rstrip("\n").split(";")
                            c = 1
                            if len(a) == 10:
                                for element in a:
                                    if element == "B":
                                        c += 1
                                        player2B += 1
                                    elif element == "C":
                                        try:
                                            if a[c] == "C" and a[c + 1] == "C" and a[c + 2] == "C" and a[c + 3] == "C":
                                                player2boats["C1"] = f"{letterlist[c-1]}{r+1},{letterlist[c]}{r+1},{letterlist[c+1]}{r+1},{letterlist[c+2]}{r+1},{letterlist[c+3]}{r+1}"
                                                c += 1
                                                player2C += 1
                                            else:
                                                raise IndexError
                                        except IndexError:
                                            try:
                                                if player2txtlines[r + 1].rstrip("\n").split(";")[c - 1] == "C" and player2txtlines[r + 2].rstrip("\n").split(";")[c - 1] == "C" and player2txtlines[r + 3].rstrip("\n").split(";")[c - 1] == "C" and player2txtlines[r + 4].rstrip("\n").split(";")[c - 1] == "C":
                                                    player2boats["C1"] = f"{letterlist[c - 1]}{r + 1},{letterlist[c - 1]}{r + 2},{letterlist[c - 1]}{r + 3},{letterlist[c - 1]}{r + 4},{letterlist[c - 1]}{r + 5}"
                                                    c += 1
                                                    player2C += 1
                                                else:
                                                    raise IndexError
                                            except IndexError:
                                                c += 1
                                                player2C += 1
                                                continue
                                    elif element == "P":
                                        c += 1
                                        player2P += 1
                                    elif element == "S":
                                        try:
                                            if a[c] == "S" and a[c + 1] == "S":
                                                player2boats["S1"] = f"{letterlist[c - 1]}{r + 1},{letterlist[c]}{r + 1},{letterlist[c + 1]}{r + 1}"
                                                c += 1
                                                player2S += 1
                                            else:
                                                raise IndexError
                                        except IndexError:
                                            try:
                                                if player2txtlines[r + 1].rstrip("\n").split(";")[c - 1] == "S" and player2txtlines[r + 2].rstrip("\n").split(";")[c - 1] == "S":
                                                    player2boats["S1"] = f"{letterlist[c - 1]}{r + 1},{letterlist[c - 1]}{r + 2},{letterlist[c - 1]}{r + 3}"
                                                    c += 1
                                                    player2S += 1
                                                else:
                                                    raise IndexError
                                            except IndexError:
                                                c += 1
                                                player2S += 1
                                                continue
                                    elif element == "D":
                                        try:
                                            if a[c] == "D" and a[c + 1] == "D":
                                                player2boats["D1"] = f"{letterlist[c - 1]}{r + 1},{letterlist[c]}{r + 1},{letterlist[c + 1]}{r + 1}"
                                                c += 1
                                                player2D += 1
                                            else:
                                                raise IndexError
                                        except IndexError:
                                            try:
                                                if player2txtlines[r + 1].rstrip("\n").split(";")[c - 1] == "D" and player2txtlines[r + 2].rstrip("\n").split(";")[c - 1] == "D":
                                                    player2boats["D1"] = f"{letterlist[c - 1]}{r + 1},{letterlist[c - 1]}{r + 2},{letterlist[c - 1]}{r + 3}"
                                                    c += 1
                                                    player2D += 1
                                                else:
                                                    raise IndexError
                                            except IndexError:
                                                c += 1
                                                player2D += 1
                                                continue
                                    elif element == "":
                                        c += 1
                                    else:
                                        print("ValueError: The character "+"'"+str(element)+"'"+"in Player2.txt is not valid character for game!\n")
                                        outputfunction("ValueError: The character "+"'"+str(element)+"'"+"in Player2.txt is not valid character for game!\n")
                                        raise ValueError
                                r += 1
                            elif len(a) < 10:
                                print(f"IndexError: for a line in Player2.txt file has less character!\n")
                                outputfunction(f"IndexError: for a line in Player2.txt file has less character!\n")
                                raise IndexError
                            else:
                                print(f"IndexError: for a line in Player2.txt file has more character!\n")
                                outputfunction(f"IndexError: for a line in Player2.txt file has more character!\n")
                                raise IndexError
                        if len(player1boats) == 9 and len(player2boats) == 9:
                            if (player1B,player1P,player1C,player1S,player1D) == (8,8,5,3,3) and (player2B,player2P,player2C,player2S,player2D) == (8,8,5,3,3):
                                player1moves = open(player1in,"r").readline().rstrip("\n").split(";")[:-1]
                                player2moves = open(player2in,"r").readline().rstrip("\n").split(";")[:-1]
                                for number in range(1,11):
                                    for word in letterlist:
                                        Table1[str(word)+"-"+str(number)]="-"
                                for number in range(1,11):
                                    for word in letterlist:
                                        Table2[str(word)+"-"+str(number)]="-"
                                multidictionary1 = {"C1":"-","B1":"-,-","D1":"-","S1":"-","P1":"-,-,-,-"}
                                multidictionary2 = {"C1":"-","B1":"-,-","D1":"-","S1":"-","P1":"-,-,-,-"}
                                index = 0
                                index1 = 0
                                index2 = 0
                                index3 = 0
                                index4 = 0
                                print("Battle of Ships Game\n")
                                outputfunction("Battle of Ships Game\n")
                                for move in player1moves:
                                  try:
                                    if len(move.split(",")) < 2:
                                        outputfunction(f"IndexError: The player1 move '{move}' index is less than two!")
                                        print(f"IndexError: The player1 move '{move}' index is less than two!")
                                        raise IndexError
                                    elif len(move.split(",")) >2:
                                        raise ValueError
                                    for element in move.split(","):
                                        if element == "":
                                            outputfunction(f"IndexError: The player1 move '{move}' is not valid!")
                                            print(f"IndexError: The player1 move '{move}' is not valid!")
                                            raise IndexError
                                    int(move.split(",")[0])
                                    if int(move.split(",")[0]) in numberlist:
                                        if move.split(",")[1] in letterlist:
                                            pass
                                        else:
                                            outputfunction(f"AssertionError: The player1 move '{move}' is not valid!")
                                            print(f"AssertionError: The player1 move '{move}' is not valid!")
                                            raise AssertionError
                                    else:
                                        outputfunction(f"AssertionError: The player1 move '{move}' is not valid!")
                                        print(f"AssertionError: The player1 move '{move}' is not valid!")
                                        raise AssertionError
                                    print("Player1's Move\n")
                                    outputfunction("\nPlayer1's Move\n\n")
                                    print("Round : "+str(Round),end="\t\t\t")
                                    outputfunction("Round : "+str(Round)+"\t\t\t\t\t")
                                    print("Grid Size: 10x10\n")
                                    outputfunction("Grid Size: 10x10\n\n")
                                    print("Player1's Hidden Board\t\tPlayer2's Hidden Board")
                                    outputfunction("Player1's Hidden Board\t\tPlayer2's Hidden Board\n")
                                    Tableprinter()
                                    print("Carrier     "+str(multidictionary1["C1"]),end="\t\t\t")
                                    outputfunction("\nCarrier     "+str(multidictionary1["C1"])+"\t\t\t\t")
                                    print("Carrier     "+str(multidictionary2["C1"]))
                                    outputfunction("Carrier     "+str(multidictionary2["C1"]))
                                    print("Battleship  "+str(multidictionary1["B1"].split(",")[0])+" "+str(multidictionary1["B1"].split(",")[1]),end="\t\t\t")
                                    outputfunction("\n"+"Battleship  "+str(multidictionary1["B1"].split(",")[0])+" "+str(multidictionary1["B1"].split(",")[1])+"\t\t\t\t")
                                    print("Battleship  "+str(multidictionary2["B1"].split(",")[0])+" "+str(multidictionary2["B1"].split(",")[1]))
                                    outputfunction("Battleship  "+str(multidictionary2["B1"].split(",")[0])+" "+str(multidictionary2["B1"].split(",")[1]))
                                    print("Destroyer   "+str(multidictionary1["D1"]),end="\t\t\t")
                                    outputfunction("\n"+"Destroyer   "+str(multidictionary1["D1"])+"\t\t\t\t")
                                    print("Destroyer   "+str(multidictionary2["D1"]))
                                    outputfunction("Destroyer   "+str(multidictionary2["D1"]))
                                    print("Submarine   "+str(multidictionary1["S1"]),end="\t\t\t")
                                    outputfunction("\n"+"Submarine   "+str(multidictionary1["S1"])+"\t\t\t\t")
                                    print("Submarine   "+str(multidictionary2["S1"]))
                                    outputfunction("Submarine   "+str(multidictionary2["S1"]))
                                    print("Patrol Boat "+str(multidictionary1["P1"].split(",")[0])+" "+str(multidictionary1["P1"].split(",")[1])+" "+str(multidictionary1["P1"].split(",")[2])+" "+str(multidictionary1["P1"].split(",")[3]),end="\t\t")
                                    outputfunction("\n"+"Patrol Boat "+str(multidictionary1["P1"].split(",")[0])+" "+str(multidictionary1["P1"].split(",")[1])+" "+str(multidictionary1["P1"].split(",")[2])+" "+str(multidictionary1["P1"].split(",")[3])+"\t\t\t")
                                    print("Patrol Boat "+str(multidictionary2["P1"].split(",")[0])+" "+str(multidictionary2["P1"].split(",")[1])+" "+str(multidictionary2["P1"].split(",")[2])+" "+str(multidictionary2["P1"].split(",")[3]))
                                    outputfunction("Patrol Boat "+str(multidictionary2["P1"].split(",")[0])+" "+str(multidictionary2["P1"].split(",")[1])+" "+str(multidictionary2["P1"].split(",")[2])+" "+str(multidictionary2["P1"].split(",")[3]))
                                    print("\nEnter your move: "+str(move)+"\n")
                                    outputfunction("\n\nEnter your move: "+str(move)+"\n\n")
                                    movement = str(move.split(",")[1])+"-"+str(move.split(",")[0])
                                    for boat in player2boats:
                                        if str(move.split(",")[1])+str(move.split(",")[0]) in player2boats[boat].split(","):
                                            Table2[movement] = "X"
                                            if len(player2boats[boat].split(",")) >= 2:
                                                a = player2boats[boat].split(",")
                                                a.remove(str(move.split(",")[1])+str(move.split(",")[0]))
                                                player2boats[boat] = ",".join(a)
                                            else:
                                                player2boats[boat] = " "
                                                Boatletter = boat[:1]
                                                if str(Boatletter)+"1" == "B1":
                                                    llist = multidictionary2[str(Boatletter) + "1"].split(",")
                                                    llist[index3] = "X"
                                                    multidictionary2[str(Boatletter) + "1"] = ",".join(llist)
                                                    index3 += 1
                                                elif str(Boatletter)+"1" == "P1":
                                                    llist = multidictionary2[str(Boatletter) + "1"].split(",")
                                                    llist[index4] = "X"
                                                    multidictionary2[str(Boatletter) + "1"] = ",".join(llist)
                                                    index4 += 1
                                                else:
                                                    multidictionary2[str(Boatletter) + "1"] = "X"
                                        else:
                                            continue
                                    if Table2[movement] == "X":
                                        pass
                                    else:
                                        Table2[movement] = "O"
                                    if len(move.split(",")) < 2:
                                        outputfunction(f"IndexError: The player1 move '{move}' index is less than two!")
                                        print(f"IndexError: The player1 move '{move}' index is less than two!")
                                        raise IndexError
                                    elif len(move.split(",")) >2:
                                        raise ValueError
                                    for element in move.split(","):
                                        if element == "":
                                            outputfunction(f"IndexError: The player1 move '{move}' is not valid!")
                                            print(f"IndexError: The player1 move '{move}' is not valid!")
                                            raise IndexError
                                    int(move.split(",")[0])
                                    if int(move.split(",")[0]) in numberlist:
                                        if move.split(",")[1] in letterlist:
                                            pass
                                        else:
                                            outputfunction(f"AssertionError: The player1 move '{move}' is not valid!")
                                            print(f"AssertionError: The player1 move '{move}' is not valid!")
                                            raise AssertionError
                                    else:
                                        outputfunction(f"AssertionError: The player1 move '{move}' is not valid!")
                                        print(f"AssertionError: The player1 move '{move}' is not valid!")
                                        raise AssertionError
                                  except ValueError:
                                    outputfunction(f"ValuerError: The player1 move '{move}' is not valid!")
                                    print(f"ValuerError: The player1 move '{move}' is not valid!")
                                    continue
                                  except IndexError:
                                    continue
                                  except AssertionError:
                                    continue
                                  while True:
                                      try:
                                        if len(player2moves[index].split(",")) < 2:
                                            outputfunction(f"IndexError: The player2 move '{move}' index is less than two!")
                                            print(f"IndexError: The player2 move '{move}' index is less than two!")
                                            raise IndexError
                                        elif len(player2moves[index].split(",")) >2:
                                            raise ValueError
                                        for element in player2moves[index].split(","):
                                            if element == "":
                                                outputfunction(f"IndexError: The player2 move '{move}' is not valid!")
                                                print(f"IndexError: The player2 move '{move}' is not valid!")
                                                raise IndexError
                                        int(player2moves[index].split(",")[0])
                                        if int(player2moves[index].split(",")[0]) in numberlist:
                                            if player2moves[index].split(",")[1] in letterlist:
                                                pass
                                            else:
                                                outputfunction(f"AssertionError: The player2 move '{move}' is not valid!")
                                                print(f"AssertionError: The player2 move '{move}' is not valid!")
                                                raise AssertionError
                                        else:
                                            outputfunction(f"AssertionError: The player2 move '{move}' is not valid!")
                                            print(f"AssertionError: The player2 move '{move}' is not valid!")
                                            raise AssertionError
                                        print("Player2's Move\n")
                                        outputfunction("Player2's Move\n\n")
                                        print("Round : " + str(Round), end="\t\t\t")
                                        outputfunction("Round : " + str(Round)+"\t\t\t\t\t")
                                        print("Grid Size: 10x10\n")
                                        outputfunction("Grid Size: 10x10\n\n")
                                        print("Player1's Hidden Board\t\tPlayer2's Hidden Board")
                                        outputfunction("Player1's Hidden Board\t\tPlayer2's Hidden Board\n")
                                        Tableprinter()
                                        print("Carrier     " + str(multidictionary1["C1"]), end="\t\t\t")
                                        outputfunction("\nCarrier     " + str(multidictionary1["C1"]) + "\t\t\t\t")
                                        print("Carrier     " + str(multidictionary2["C1"]))
                                        outputfunction("Carrier     " + str(multidictionary2["C1"]))
                                        print("Battleship  " + str(multidictionary1["B1"].split(",")[0]) + " " + str(multidictionary1["B1"].split(",")[1]),end="\t\t\t")
                                        outputfunction("\n" + "Battleship  " + str(multidictionary1["B1"].split(",")[0]) + " " + str(multidictionary1["B1"].split(",")[1]) + "\t\t\t\t")
                                        print("Battleship  " + str(multidictionary2["B1"].split(",")[0]) + " " + str(multidictionary2["B1"].split(",")[1]))
                                        outputfunction("Battleship  " + str(multidictionary2["B1"].split(",")[0]) + " " + str(multidictionary2["B1"].split(",")[1]))
                                        print("Destroyer   " + str(multidictionary1["D1"]), end="\t\t\t")
                                        outputfunction("\n" + "Destroyer   " + str(multidictionary1["D1"]) + "\t\t\t\t")
                                        print("Destroyer   " + str(multidictionary2["D1"]))
                                        outputfunction("Destroyer   " + str(multidictionary2["D1"]))
                                        print("Submarine   " + str(multidictionary1["S1"]), end="\t\t\t")
                                        outputfunction("\n" + "Submarine   " + str(multidictionary1["S1"]) + "\t\t\t\t")
                                        print("Submarine   " + str(multidictionary2["S1"]))
                                        outputfunction("Submarine   " + str(multidictionary2["S1"]))
                                        print("Patrol Boat " + str(multidictionary1["P1"].split(",")[0]) + " " + str(multidictionary1["P1"].split(",")[1]) + " " + str(multidictionary1["P1"].split(",")[2]) + " " + str(multidictionary1["P1"].split(",")[3]), end="\t\t")
                                        outputfunction("\n" + "Patrol Boat " + str(multidictionary1["P1"].split(",")[0]) + " " + str(multidictionary1["P1"].split(",")[1]) + " " + str(multidictionary1["P1"].split(",")[2]) + " " + str(multidictionary1["P1"].split(",")[3]) + "\t\t\t")
                                        print("Patrol Boat " + str(multidictionary2["P1"].split(",")[0]) + " " + str(multidictionary2["P1"].split(",")[1]) + " " + str(multidictionary2["P1"].split(",")[2]) + " " + str(multidictionary2["P1"].split(",")[3]))
                                        outputfunction("Patrol Boat " + str(multidictionary2["P1"].split(",")[0]) + " " + str(multidictionary2["P1"].split(",")[1]) + " " + str(multidictionary2["P1"].split(",")[2]) + " " + str(multidictionary2["P1"].split(",")[3]))
                                        print("\nEnter your move: " + str(player2moves[index]) + "\n")
                                        outputfunction("\n\nEnter your move: " + str(player2moves[index]) + "\n")
                                        movement2 = str(player2moves[index].split(",")[1])+"-"+str(player2moves[index].split(",")[0])
                                        for boat in player1boats:
                                            if str(player2moves[index].split(",")[1])+str(player2moves[index].split(",")[0]) in player1boats[boat].split(","):
                                                Table1[movement2] = "X"
                                                if len(player1boats[boat].split(",")) >= 2:
                                                    a = player1boats[boat].split(",")
                                                    a.remove(str(player2moves[index].split(",")[1])+str(player2moves[index].split(",")[0]))
                                                    player1boats[boat] = ",".join(a)
                                                else:
                                                    Boatletter = boat[:1]
                                                    player1boats[boat] = " "
                                                    if str(Boatletter)+"1" == "B1":
                                                        llist = multidictionary1[str(Boatletter)+"1"].split(",")
                                                        llist[index1] = "X"
                                                        multidictionary1[str(Boatletter)+"1"]= ",".join(llist)
                                                        index1 +=1
                                                    elif str(Boatletter)+"1" == "P1":
                                                        llist = multidictionary1[str(Boatletter)+"1"].split(",")
                                                        llist[index2] = "X"
                                                        multidictionary1[str(Boatletter)+"1"]= ",".join(llist)
                                                        index2 += 1
                                                    else:
                                                        multidictionary1[str(Boatletter)+"1"]="X"
                                                    counter1 = 0
                                                    counter2 = 0
                                                    for element in multidictionary1:
                                                        for coordinate in multidictionary1[element].split(","):
                                                            if coordinate == "X":
                                                                counter1 += 1
                                                    if counter1 == 9:
                                                        for element in multidictionary2:
                                                            if multidictionary2[element] == "X":
                                                                counter2 += 1
                                                        if counter2 == 9:
                                                            print("It is a Draw!\n\nFinal Information\n")
                                                            outputfunction("It is a Draw!\n\nFinal Information\n\n")
                                                            print("Player1's Board\t\t\tPlayer2's Board")
                                                            outputfunction("Player1's Board\t\t\t\tPlayer2's Board\n")
                                                            Tableprinter()
                                                            print("Carrier     " + str(multidictionary1["C1"]),end="\t\t\t")
                                                            outputfunction("\nCarrier     " + str(multidictionary1["C1"])+"\t\t\t\t")
                                                            print("Carrier     " + str(multidictionary2["C1"]))
                                                            outputfunction("Carrier     " + str(multidictionary2["C1"])+"\n")
                                                            print("Battleship  " + str(multidictionary1["B1"].split(",")[0]) + " " + str(multidictionary1["B1"].split(",")[1]), end="\t\t\t")
                                                            outputfunction("Battleship  " + str(multidictionary1["B1"].split(",")[0]) + " " + str(multidictionary1["B1"].split(",")[1])+"\t\t\t\t")
                                                            print("Battleship  " + str(multidictionary2["B1"].split(",")[0]) + " " + str(multidictionary2["B1"].split(",")[1]))
                                                            outputfunction("Battleship  " + str(multidictionary2["B1"].split(",")[0]) + " " + str(multidictionary2["B1"].split(",")[1])+"\n")
                                                            print("Destroyer   " + str(multidictionary1["D1"]),end="\t\t\t")
                                                            outputfunction("Destroyer   " + str(multidictionary1["D1"])+"\t\t\t\t")
                                                            print("Destroyer   " + str(multidictionary2["D1"]))
                                                            outputfunction("Destroyer   " + str(multidictionary2["D1"])+"\n")
                                                            print("Submarine   " + str(multidictionary1["S1"]),end="\t\t\t")
                                                            outputfunction("Submarine   " + str(multidictionary1["S1"])+"\t\t\t\t")
                                                            print("Submarine   " + str(multidictionary2["S1"]))
                                                            outputfunction("Submarine   " + str(multidictionary2["S1"])+"\n")
                                                            print("Patrol Boat " + str(multidictionary1["P1"].split(",")[0]) + " " + str(multidictionary1["P1"].split(",")[1]) + " " + str(multidictionary1["P1"].split(",")[2]) + " " + str(multidictionary1["P1"].split(",")[3]),end="\t\t")
                                                            outputfunction("Patrol Boat " + str(multidictionary1["P1"].split(",")[0]) + " " + str(multidictionary1["P1"].split(",")[1]) + " " + str(multidictionary1["P1"].split(",")[2]) + " " + str(multidictionary1["P1"].split(",")[3])+"\t\t\t")
                                                            print("Patrol Boat " + str(multidictionary2["P1"].split(",")[0]) + " " + str(multidictionary2["P1"].split(",")[1]) + " " + str(multidictionary2["P1"].split(",")[2]) + " " + str(multidictionary2["P1"].split(",")[3]))
                                                            outputfunction("Patrol Boat " + str(multidictionary2["P1"].split(",")[0]) + " " + str(multidictionary2["P1"].split(",")[1]) + " " + str(multidictionary2["P1"].split(",")[2]) + " " + str(multidictionary2["P1"].split(",")[3])+"\n")
                                                            break
                                                        else:
                                                            for boat in player2boats:
                                                                boatword = boat[:1]
                                                                if player2boats[boat] != " ":
                                                                    for element in Table2:
                                                                       if str(element.split("-")[0])+str(element.split("-")[1]) in player2boats[boat].split(","):
                                                                           Table2[element] = f"{boatword}"
                                                            print("Player2 Wins!\n\nFinal Information\n")
                                                            outputfunction("Player2 Wins!\n\nFinal Information\n\n")
                                                            print("Player1's Board\t\t\tPlayer2's Board")
                                                            outputfunction("Player1's Board\t\t\t\tPlayer2's Board\n")
                                                            Tableprinter()
                                                            print("Carrier     " + str(multidictionary1["C1"]),end="\t\t\t")
                                                            outputfunction("\nCarrier     " + str(multidictionary1["C1"]) + "\t\t\t\t")
                                                            print("Carrier     " + str(multidictionary2["C1"]))
                                                            outputfunction("Carrier     " + str(multidictionary2["C1"]) + "\n")
                                                            print("Battleship  " + str(multidictionary1["B1"].split(",")[0]) + " " + str(multidictionary1["B1"].split(",")[1]), end="\t\t\t")
                                                            outputfunction("Battleship  " + str(multidictionary1["B1"].split(",")[0]) + " " + str(multidictionary1["B1"].split(",")[1]) + "\t\t\t\t")
                                                            print("Battleship  " + str(multidictionary2["B1"].split(",")[0]) + " " + str(multidictionary2["B1"].split(",")[1]))
                                                            outputfunction("Battleship  " + str(multidictionary2["B1"].split(",")[0]) + " " + str(multidictionary2["B1"].split(",")[1]) + "\n")
                                                            print("Destroyer   " + str(multidictionary1["D1"]),end="\t\t\t")
                                                            outputfunction("Destroyer   " + str(multidictionary1["D1"]) + "\t\t\t\t")
                                                            print("Destroyer   " + str(multidictionary2["D1"]))
                                                            outputfunction("Destroyer   " + str(multidictionary2["D1"]) + "\n")
                                                            print("Submarine   " + str(multidictionary1["S1"]),end="\t\t\t")
                                                            outputfunction("Submarine   " + str(multidictionary1["S1"]) + "\t\t\t\t")
                                                            print("Submarine   " + str(multidictionary2["S1"]))
                                                            outputfunction("Submarine   " + str(multidictionary2["S1"]) + "\n")
                                                            print("Patrol Boat " + str(multidictionary1["P1"].split(",")[0]) + " " + str(multidictionary1["P1"].split(",")[1]) + " " + str(multidictionary1["P1"].split(",")[2]) + " " + str(multidictionary1["P1"].split(",")[3]),end="\t\t")
                                                            outputfunction("Patrol Boat " + str(multidictionary1["P1"].split(",")[0]) + " " + str(multidictionary1["P1"].split(",")[1]) + " " + str(multidictionary1["P1"].split(",")[2]) + " " + str(multidictionary1["P1"].split(",")[3]) + "\t\t\t")
                                                            print("Patrol Boat " + str(multidictionary2["P1"].split(",")[0]) + " " + str(multidictionary2["P1"].split(",")[1]) + " " + str(multidictionary2["P1"].split(",")[2]) + " " + str(multidictionary2["P1"].split(",")[3]))
                                                            outputfunction("Patrol Boat " + str(multidictionary2["P1"].split(",")[0]) + " " + str(multidictionary2["P1"].split(",")[1]) + " " + str(multidictionary2["P1"].split(",")[2]) + " " + str(multidictionary2["P1"].split(",")[3]) + "\n")
                                                            break
                                                    else:
                                                        for element in multidictionary2:
                                                            for coordinate in multidictionary2[element].split(","):
                                                                if  coordinate == "X":
                                                                    counter2 += 1
                                                        if counter2 == 9:
                                                            for boat in player1boats:
                                                                boatword = boat[:1]
                                                                if player1boats[boat] != " ":
                                                                    for element in Table1:
                                                                       if str(element.split("-")[0])+str(element.split("-")[1]) in player1boats[boat].split(","):
                                                                           Table1[element] = f"{boatword}"
                                                            print("Player1 Wins!\n\nFinal Information\n")
                                                            outputfunction("Player1 Wins!\n\nFinal Information\n\n")
                                                            print("Player1's Board\t\t\tPlayer2's Board")
                                                            outputfunction("Player1's Board\t\t\t\tPlayer2's Board\n")
                                                            Tableprinter()
                                                            print("Carrier     " + str(multidictionary1["C1"]),end="\t\t\t")
                                                            outputfunction("\nCarrier     " + str(multidictionary1["C1"]) + "\t\t\t\t")
                                                            print("Carrier     " + str(multidictionary2["C1"]))
                                                            outputfunction("Carrier     " + str(multidictionary2["C1"]) + "\n")
                                                            print("Battleship  " + str(multidictionary1["B1"].split(",")[0]) + " " + str(multidictionary1["B1"].split(",")[1]), end="\t\t\t")
                                                            outputfunction("Battleship  " + str(multidictionary1["B1"].split(",")[0]) + " " + str(multidictionary1["B1"].split(",")[1]) + "\t\t\t\t")
                                                            print("Battleship  " + str(multidictionary2["B1"].split(",")[0]) + " " + str(multidictionary2["B1"].split(",")[1]))
                                                            outputfunction("Battleship  " + str(multidictionary2["B1"].split(",")[0]) + " " + str(multidictionary2["B1"].split(",")[1]) + "\n")
                                                            print("Destroyer   " + str(multidictionary1["D1"]),end="\t\t\t")
                                                            outputfunction("Destroyer   " + str(multidictionary1["D1"]) + "\t\t\t\t")
                                                            print("Destroyer   " + str(multidictionary2["D1"]))
                                                            outputfunction("Destroyer   " + str(multidictionary2["D1"]) + "\n")
                                                            print("Submarine   " + str(multidictionary1["S1"]),end="\t\t\t")
                                                            outputfunction("Submarine   " + str(multidictionary1["S1"]) + "\t\t\t\t")
                                                            print("Submarine   " + str(multidictionary2["S1"]))
                                                            outputfunction("Submarine   " + str(multidictionary2["S1"]) + "\n")
                                                            print("Patrol Boat " + str(multidictionary1["P1"].split(",")[0]) + " " + str(multidictionary1["P1"].split(",")[1]) + " " + str(multidictionary1["P1"].split(",")[2]) + " " + str(multidictionary1["P1"].split(",")[3]),end="\t\t")
                                                            outputfunction("Patrol Boat " + str(multidictionary1["P1"].split(",")[0]) + " " + str(multidictionary1["P1"].split(",")[1]) + " " + str(multidictionary1["P1"].split(",")[2]) + " " + str(multidictionary1["P1"].split(",")[3]) + "\t\t\t")
                                                            print("Patrol Boat " + str(multidictionary2["P1"].split(",")[0]) + " " + str(multidictionary2["P1"].split(",")[1]) + " " + str(multidictionary2["P1"].split(",")[2]) + " " + str(multidictionary2["P1"].split(",")[3]))
                                                            outputfunction("Patrol Boat " + str(multidictionary2["P1"].split(",")[0]) + " " + str(multidictionary2["P1"].split(",")[1]) + " " + str(multidictionary2["P1"].split(",")[2]) + " " + str(multidictionary2["P1"].split(",")[3]) + "\n")
                                                            break
                                                        else:
                                                            counter2 = 0
                                                            break
                                            else:
                                                continue
                                        if Table1[movement2] == "X":
                                            pass
                                        else:
                                            Table1[movement2] = "O"
                                        Round += 1
                                        index += 1
                                        break
                                      except ValueError:
                                          index += 1
                                          outputfunction(f"ValuerError: The player2 move '{move}' is not valid!")
                                          print(f"ValuerError: The player2 move '{move}' is not valid!")
                                          continue
                                      except IndexError:
                                          index +=1
                                          continue
                                      except AssertionError:
                                          index +=1
                                          continue
                            else:
                                outputfunction("kaBOOM: run for your life!\n")
                                print("kaBOOM: run for your life!\n")
                        else:
                            outputfunction("kaBOOM: run for your life!\n")
                            print("kaBOOM: run for your life!\n")


                    except IndexError:
                        pass
                    except ValueError:
                        pass
                except IOError:
                    outputfunction(f"IOError: input file {player2in} is not reachable.\n")
                    print(f"IOError: input file {player2in} is not reachable.\n")
            except IOError:
                try:
                    open(player2in,"r")
                    outputfunction(f"IOError: input file {player1in} is not reachable.\n")
                    print(f"IOError: input file {player1in} is not reachable.\n")
                except IOError:
                    outputfunction(f"IOError: input files {player1in},{player2in} are not reachable.\n")
                    print(f"IOError: input files {player1in},{player2in} are not reachable.\n")
        except IOError:
            try:
                open(player1in,"r")
                try:
                    open(player2in,"r")
                    outputfunction(f"IOError: input file {player2txt} is not reachable.\n")
                    print(f"IOError: input file {player2txt} is not reachable.\n")
                except:
                    outputfunction(f"IOError: input files {player2txt},{player2in} are not reachable.\n")
                    print(f"IOError: input files {player2txt},{player2in} are not reachable.\n")
            except IOError:
                try:
                    open(player2in,"r")
                    outputfunction(f"IOError: input files {player2txt},{player1in} are not reachable.\n")
                    print(f"IOError: input files {player2txt},{player1in} are not reachable.\n")
                except IOError:
                    outputfunction(f"IOError: input files {player2txt},{player1in},{player2in} are not reachable.\n")
                    print(f"IOError: input files {player2txt},{player1in},{player2in} are not reachable.\n")
    except IOError:
        try:
            open(player2txt,"r")
            try:
                open(player1in,"r")
                try:
                    open(player2in,"r")
                    outputfunction(f"IOError: input file {player1txt} is not reachable.\n")
                    print(f"IOError: input file {player1txt} is not reachable.\n")
                except IOError:
                    outputfunction(f"IOError: input files {player1txt},{player2in} are not reachable.\n")
                    print(f"IOError: input files {player1txt},{player2in} are not reachable.\n")
            except IOError:
                try:
                    open(player2in,"r")
                    outputfunction(f"IOError: input files {player1txt},{player1in} are not reachable.\n")
                    print(f"IOError: input files {player1txt},{player1in} are not reachable.\n")
                except IOError:
                    outputfunction(f"IOError: input files {player1txt},{player1in},{player2in} are not reachable.\n")
                    print(f"IOError: input files {player1txt},{player1in},{player2in} are not reachable.\n")
        except IOError:
            try:
                open(player1in,"r")
                try:
                    open(player2in,"r")
                    outputfunction(f"IOError: input files {player1txt},{player2txt} are not reachable.\n")
                    print(f"IOError: input files {player1txt},{player2txt} are not reachable.\n")
                except IOError:
                    outputfunction(f"IOError: input files {player1txt},{player2txt},{player2in} are not  reachable.\n")
                    print(f"IOError: input files {player1txt},{player2txt},{player2in} are not  reachable.\n")
            except IOError:
                try:
                    open(player2in,"r")
                    outputfunction(f"IOError: input files {player1txt},{player2txt},{player1in} are not reachable.\n")
                    print(f"IOError: input files {player1txt},{player2txt},{player1in} are not reachable.\n")
                except IOError:
                    outputfunction(f"IOError: input files {player1txt},{player2txt},{player1in},{player2in} are not reachable.\n")
                    print(f"IOError: input files {player1txt},{player2txt},{player1in},{player2in} are not reachable.\n")
except IndexError:
    outputfunction("IndexError: number of input files less1 than expected.\n")
    print("IndexError: number of input files less1 than expected.\n")
