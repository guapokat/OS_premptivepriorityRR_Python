'''
Homework3
By Virgil Martinez
completed 28 feb 2018
www.virgilmartinez.com
'''


class Instruction:

    def __init__(self):
        self.instructionName = 0
        self.arrivalTime = 0
        self.priority = 0
        self.burstDuration = 0


class personalMethods:

    def __init__(self):
        self.numberOfInstructions = 0
        self.outputString = ""
        self.cpuCounter = 0
        self.minArrivaltime = 0
        self.queue = []
        self.quantum = 2
        self.entireBurstDuration = 0
        self.instructionTurnAroundTimes = []
        self.instructionTurnAroundNames = []

    def exit(self):
        print("\n\nExiting script")
        exit()

    # Returns the number of CPU instructions as a class with appropriate parameters
    def processInput(self, userFileName) -> [Instruction]:
        instructions = []
        index = 0
        with open(userFileName + ".txt", "r") as f:
            # first line is number of instructions
            self.numberOfInstructions = f.readline()
            print("number of instructions: ", self.numberOfInstructions)
            for line in f:
                individualNumbers = line.split()
                tempInstruction = Instruction()
                tempInstruction.instructionName = index
                index += 1
                tempInstruction.arrivalTime = individualNumbers[0]
                tempInstruction.priority = individualNumbers[1]
                tempInstruction.burstDuration = individualNumbers[2]
                instructions.append(tempInstruction)
        return instructions

    def determineNextInstruction(self, arrayOfInstructions, queue) -> (int, int):
        arrivalTimesArray = []
        priorityArray = []
        instructionName = -1
        self.queue = queue

        for time in arrayOfInstructions:
            arrivalTimesArray.append(time.arrivalTime)
            priorityArray.append(time.priority)
        if arrivalTimesArray:
            val, atIndex = min((val, atIndex) for (atIndex, val) in enumerate(arrivalTimesArray))
            for q in queue:
                if q.arrivalTime < val:
                    theInstructionName = q.instructionName
                if instructionName >= 0:
                    for a in range(0, len(arrayOfInstructions)):
                        if arrayOfInstructions[a].instructionName == instructionName:
                            atIndex = a
                            val = arrayOfInstructions[a].burstDuration
        else:
            val = queue[0].burstDuration
            atIndex = queue[0].instructionName

        return (val, atIndex)

    def fire(self, Instruction) -> int:
        burstDuration = int(Instruction.burstDuration)
        checkThis = int(self.minArrivaltime) + (
                int(self.quantum) * int(self.numberOfInstructions))
        print("starting at cpu time: ", self.minArrivaltime)
        if int(Instruction.burstDuration) <= self.quantum:
            for x in range(0, int(Instruction.burstDuration)):
                self.outputString += ("ins(" + str(Instruction.instructionName) + ") | ")
                # print("ins(",Instruction.instructionName,")", end=' | ')
                print(self.outputString)
                burstDuration -= 1
                self.cpuCounter = int(self.cpuCounter) + 1
            print("Instruction ", Instruction.instructionName, " completed")
        else:
            for x in range(0, self.quantum):
                self.outputString += ("ins(" + str(Instruction.instructionName) + ") | ")
                # print("ins(",Instruction.instructionName,")", end=' | ')
                print(self.outputString)
                burstDuration -= 1
                self.cpuCounter = int(self.cpuCounter) + 1
        print("Ending at cpu time: ", (self.cpuCounter))
        print()
        return burstDuration

    def orderQueue(self, queue) -> []:
        self.queue = sorted(queue, key=lambda queue: queue.priority)
        return self.queue

    def startingCPUTime(self, instructions):
        arrivalTimesArray = []
        for time in instructions:
            arrivalTimesArray.append(time.arrivalTime)
        val, atIndex = min((val, atIndex) for (atIndex, val) in enumerate(arrivalTimesArray))
        self.minArrivaltime = val
        self.cpuCounter = val

    def checkEntireBurstDuration(self, inst):
        sum = 0
        for i in inst:
            sum += int(i.burstDuration)
        self.entireBurstDuration = sum

    def takeFromQueueNowAndFinish(self):

        for q in range(0, len(self.queue)):
            print("Beginning at CPU cycle: ", self.minArrivaltime)
            for x in range(0, self.queue[q].burstDuration):
                self.outputString += ("ins(" + str(self.queue[q].instructionName) + ") | ")
                # print("ins(",Instruction.instructionName,")", end=' | ')
                print(self.outputString)
                self.queue[q].burstDuration -= 1
                self.cpuCounter = int(self.cpuCounter) + 1
                if self.queue[q].burstDuration == 0:
                    print(("ins(" + str(self.queue[q].instructionName) + ") has completed at: " + str(
                        self.cpuCounter) + " CPU cycles."))
                    print()
                    self.instructionTurnAroundNames.append(self.queue[q].instructionName)
                    self.instructionTurnAroundTimes.append(self.cpuCounter)
            print("Ending at CPU cycle ", self.cpuCounter)
            print()

    def finishUp(self):
        average = 0
        sum = 0
        print("TURNAROUND TIMES: ")
        for i in range(0, len(self.instructionTurnAroundNames)):
            print("Instruction ", self.instructionTurnAroundNames[i], " took ",
                  (int(self.instructionTurnAroundTimes[i]) - int(self.minArrivaltime)), " CPU cycles.")
            sum += (self.instructionTurnAroundTimes[i] - int(self.minArrivaltime))
        average = sum / len(self.instructionTurnAroundTimes)
        print("The average Turnaround time is: ", average)


if __name__ == '__main__':
    # INITIALIZE
    myInstruction = Instruction()
    personalMethods = personalMethods()
    instructions = []
    queue = []

    # USER INPUT
    while True:
        quantumAmount = input("Please enter a quantum amount: ")
        try:
            iffy = int(quantumAmount)
        except ValueError:
            print("That's not a number, try again.")
        if len(quantumAmount) > 0:
            personalMethods.quantum = int(quantumAmount)
        else:
            print("Not a valid input")
        userAction = input("Please enter the .txt file name you would like to open ('E' to exit): ")
        if userAction == 'E' or userAction == 'e':
            personalMethods.exit()
        elif len(userAction) > 0:
            personalMethods.processInput(userAction)
        else:
            print("Not a valid input")
        instructions = personalMethods.processInput(userAction)
        personalMethods.startingCPUTime(instructions)
        personalMethods.checkEntireBurstDuration(instructions)
        for x in range(0, int(personalMethods.numberOfInstructions)):
            index, doNextIntRepresentaiton = personalMethods.determineNextInstruction(instructions, queue)
            newBurstDuration = personalMethods.fire(instructions[doNextIntRepresentaiton])
            if newBurstDuration != 0:
                instructions[doNextIntRepresentaiton].burstDuration = newBurstDuration
                queue.append(instructions[doNextIntRepresentaiton])
                print("\ninstruction(", instructions[doNextIntRepresentaiton].instructionName, ") moved to queue",
                      end='')
                print("\n\nQUEUE INFORMATION: ")
                print("Queue is now: ")
                for q in queue:
                    print("ins(", q.instructionName, ") with remaining burst time --> ", q.burstDuration,
                          " and PRIORITY --> ", q.priority)
                queue = personalMethods.orderQueue(queue)
                print("Queue reordered by priority: ")
                for q in queue:
                    print("ins(", q.instructionName, ")", end=' ')
                print()
                print()
                instructions.remove(instructions[doNextIntRepresentaiton])
            else:
                personalMethods.instructionTurnAroundNames.append(instructions[doNextIntRepresentaiton].instructionName)
                personalMethods.instructionTurnAroundTimes.append(personalMethods.cpuCounter)
                instructions.remove(instructions[doNextIntRepresentaiton])

        personalMethods.takeFromQueueNowAndFinish()
        personalMethods.finishUp()
        personalMethods.exit()
