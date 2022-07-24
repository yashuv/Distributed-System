import sys
import pprint

processList =[]
vectorClock = {}
TimeStamp = {}

def addProcess():
    global processList
    pName = input("Enter Processes Name seperated by space: ")
    processList = pName.split()
    for process in processList:
        vectorClock[process] = [0] * len(processList)

def sendMessage(t):
    eName = input("Enter the Event which will receive the message: ")
    pName = input("Enter the process on which this event will occur: ")
    pval = int(pName[-1])
    for i in range(len(processList)):
        # print('(vectorClock[',pName,'][',i,'], t[',i,']) =', '(',vectorClock[pName][i],', ', t[i],')')
        vectorClock[pName][i] = max(vectorClock[pName][i], t[i])

    vectorClock[pName][pval-1] += 1
    vec = vectorClock[pName].copy()
    TimeStamp.update({eName:vec})
    

def addEvent():
    pName = input("Enter the Process for which you want to add an event: ")
    eName = input("Enter Event Name: ")
    eType = input("Enter the type of event(normal/message): ")
    pval = int(pName[-1])

    vectorClock[pName][pval-1] += 1

    vec = vectorClock[pName].copy() 

    if eType == "normal" or eType == "n" or eType == "N":
        TimeStamp.update({eName:vec})

    if eType == "message" or eType == "m" or eType == "M":
        TimeStamp.update({eName:vec})
        sendMessage(TimeStamp[eName])
    

def display():
    print("-"*20)
    pprint.pprint(TimeStamp)
    print("-"*20)


if __name__ == "__main__":
    addProcess()
    while(1):
        print("-"*20)
        print("1.ADD EVENT\n2.DISPLAY TIMESTAMP\n3.EXIT")
        print("-"*20)
        n = int(input("Enter your choice: "))
        if n==1:
            addEvent()
        elif n==2:
            display()
        else:
            sys.exit("BYE")
