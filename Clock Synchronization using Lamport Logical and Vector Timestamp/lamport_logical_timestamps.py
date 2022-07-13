import sys
import pprint    # to prettify our dictionary

processList =[]
logicalClock = {}
TimeStamp = {}

def addProcess():
    pName = input("Enter Processes Name seperated by space: ")
    processList = pName.split()
    for process in processList:
        logicalClock[process] = 0

def sendMessage(t):
    eName = input("Enter the Event which will receive the message: ")
    pName = input("Enter the process on which this event will occur: ")
    if t > logicalClock[pName]:
        logicalClock[pName] = t
    TimeStamp[eName] = logicalClock[pName] + 1
    logicalClock[pName] += 1

def addEvent():
    pName = input("Enter the Process for which you want to add an event: ")
    eName = input("Enter Event Name: ")
    eType = input("Enter the type of event(normal/message): ")
    if eType == "normal":
        TimeStamp[eName] = logicalClock[pName] + 1
        logicalClock[pName] += 1
    if eType == "message":
        TimeStamp[eName] = logicalClock[pName] + 1
        logicalClock[pName] += 1
        sendMessage(TimeStamp[eName])

def display():
    print("-"*20)
    pprint.pprint(TimeStamp)


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
