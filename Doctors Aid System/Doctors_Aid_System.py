lineslist = []                #That list includes every line into the input file.
patientsname = []             #That list includes the patients name in the system.
patientsinfo = []             #That list includes the patients information in the system.

def f_saveoutput(x):                                             #This function opens output file with write format and write the results of the functions into that output file line by line.
    saveoutput = open("doctors_aid_outputs.txt", "a")
    saveoutput.write(x)
    saveoutput.close()


def f_readinput():                                                #This function opens input file with read format and read the every line and appends them into the lineslist.
    readinput = open("doctors_aid_inputs.txt", "r")
    lineslist.append((open("doctors_aid_inputs.txt", "r").readlines()))
    readinput.close()


def f_create(line):
    linesplit = line.split(", ")                  #Splits the line to take every patient information as a string
    linesplit[0] = linesplit[0].split(" ")[1]     #It changes every [0] index to delete the command into the that index
    if linesplit[0] in patientsname:              #Checks for is the patient already registered in the system
        f_saveoutput("Patient " + linesplit[0] + " cannot be recorded due to duplication.\n")  #It gives an error message if patient is already registered. It directs to f_saveoutput function.
    else:
        patientsname.append(linesplit[0])
        patientsinfo.append(linesplit[0:])                                                     #It appends patient name and information and it directs to f_saveoutput function.
        f_saveoutput("Patient " + linesplit[0] + " is recorded.\n")


def f_remove(line):
    linesplit = line.split(" ")                        #Splits the name to take a name and command as a string
    linesplit[0] = linesplit[1][:-1]                   #To delete the "\n" in the string I used [:-1] and set the index[0] as a given name
    if linesplit[0] in patientsname:                   #If given name is in the system it searches the patientsinfo list and remove it.
        for i in patientsinfo:
            if linesplit[0] == i[0]:                   #[0] indexs are representing names. If it matchs the names, it removes every information about that patient.
                patientsinfo.remove(i)
                patientsname.remove(linesplit[0])
                f_saveoutput("Patient " + linesplit[0] + " is removed.\n")
                break
    else:                                                                                 #If given name is not in the system ıt directs to f_saveoutput function to write an error message.
        f_saveoutput("Patient " + linesplit[0] + " cannot be removed due to absence.\n")


def f_probability(line):
    linesplit = line.split(" ")
    linesplit[0] = linesplit[1][:-1]
    if linesplit[0] in patientsname:
        for i in patientsinfo:
            if linesplit[0] == i[0]:
                incidence = int(i[3].split("/")[0]) / int(i[3].split("/")[1])              #i[3] represents disease incidence
                probability = incidence / (1.0 - float(i[1]) + incidence)                  #The formula for calculating probability
                f_saveoutput("Patient " + linesplit[0] + " has a probability of " + str(probability * 100.0) + "%" + " of having " + i[2] + ".\n")
                break
    else:
        f_saveoutput("Probability for " + linesplit[0] + " cannot be calculated due to absence.\n")


def f_recommendation(line):
    linesplit = line.split(" ")
    linesplit[0] = linesplit[1][:-1]
    if linesplit[0] in patientsname:
        for i in patientsinfo:
            if linesplit[0] == i[0]:
                incidence = int(i[3].split("/")[0]) / int(i[3].split("/")[1])
                probability = incidence / (1.0 - float(i[1]) + incidence)            #Calculating probability again because it is out of the global scope.
                treatment = float(i[5])
                if treatment > probability:                                          #Comparing treatment and probability
                    f_saveoutput("System suggest " + linesplit[0] + " NOT to have the treatment.\n")
                else:
                    f_saveoutput("System suggest " + linesplit[0] + " to have the treatment.\n")
                break
    else:
        f_saveoutput("Recommendation for " + linesplit[0] + " cannot be calculated due to absence.\n")


def f_list(line):
    f_saveoutput("Patient Diagnosis   Disease         Disease     Treatment       Treatment\n")
    f_saveoutput("Name    Accuracy    Name            Incidence   Name            Risk\n")
    f_saveoutput("-------------------------------------------------------------------------\n")
    for i in patientsinfo:        #It searches patientsinfo list
        treatmentpercent = str(int(float(i[5]) * 100)) + "%"       #For showing treatment risk with percent string format
        diagnosisaccuracypercent = str(float(i[1]) * 100) + "%"    #For showing diagnosis accuracy with percent string format
        f_saveoutput(i[0] + " " * (8 - len(i[0])) + diagnosisaccuracypercent + " " * (12 - len(diagnosisaccuracypercent)) + i[2] + " " * (16 - len(i[2])) + i[3] + " " * (12 - len(i[3])) + i[4] + " " * (16 - len(i[4])) + treatmentpercent + "\n") #I count the all spaces and make it with spaces. Using tab is another solution but thats okay too.


f_readinput()

for line in lineslist[0]:              #we are chechking every index into the lineslist.
    linesplit = line.split(" ")        #we are spliting the terms in that index.
    if linesplit[0] == "create":
        f_create(line)
    elif linesplit[0] == "probability":
        f_probability(line)
    elif linesplit[0] == "recommendation":                    #we are looking command names to call a proper function.
        f_recommendation(line)
    elif linesplit[0] == "list\n":
        f_list(line)
    elif linesplit[0] == "remove":
        f_remove(line)
    else:                                                       #If the program didn't find, it writes an error message.
        f_saveoutput("Invalid comment detected!\n")

#Muzaffer Berke Savaş    
