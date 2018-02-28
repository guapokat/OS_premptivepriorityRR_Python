class Instruction:

    def __init__(self):
        self.instructionName = 0
        self.arrivalTime = 0
        self.priority = 0
        self.burstDuration = 0

class personalMethods:

    def __init__(self):
        self.numberOfInstructions = 0
        self.minOut = 0
        self.maxOut = 250
        self.outputString = ""
        self.cpuCounter = 0

    def exit(self):
        print("\n\nExiting script")
        exit()

    # Returns the number of CPU instructions as a class with appropriate parameters
    def processInput(self, userFileName) -> [Instruction]:
        instructions = []
        index = 0
        with open(userFileName + ".txt", "r") as f:
            self.numberOfInstructions = f.readline()
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

    def preemptive(self, arrOfInstructions):
        arrivalTimes = []
        burstTimes = []
        for instruction in arrOfInstructions:
            arrivalTimes.append(instruction.arrivalTime)
            burstTimes.append(instruction.burstDuration)
        self.maxOut = max(arrivalTimes) + max(burstTimes)
        self.determineNextInstruction(arrivalTimes)

    def determineNextInstruction(self, arrayOfInstructions) -> (int, int):
        arrivalTimesArray = []
        priorityArray = []
        for time in arrayOfInstructions:
            arrivalTimesArray.append(time.arrivalTime)
            priorityArray.append(time.priority)
        print("\narrivalTimesArray[] is : ", arrivalTimesArray)
        print("priorityArray[] is : ", priorityArray)
        val, atIndex = min((val, atIndex) for (atIndex, val) in enumerate(arrivalTimesArray))
        self.minOut = val

        print("value is: ", val)
        print("atIndex: ", atIndex)
        print()

        return (val, atIndex)

    def fire(self, Instruction, quartus) -> int:
        burstDuration = int(Instruction.burstDuration)
        if int(Instruction.burstDuration) <= quartus:
            for x in range (1, int(Instruction.burstDuration)):
                print("ins(",Instruction.instructionName,")", end='')
                burstDuration -= 1
                self.cpuCounter += 1
            print("completed")

        else:
            for x in range (0, quartus):
                self.outputString += ("ins(" + str(Instruction.instructionName) + ") | ")
                # print("ins(",Instruction.instructionName,")", end=' | ')
                print(self.outputString)
                burstDuration -= 1
                self.cpuCounter += 1
        return burstDuration


if __name__ == '__main__':
    #INITIALIZE
    myInstruction = Instruction()
    personalMethods = personalMethods()
    quartus = 2
    instructions = []
    queue = []

    #USER INPUT
    while True:
        # grabbing user input, hopefully they don't enter a wrong filename...will crash
        #userAction = input("Please enter the .txt file name you would like to open ('E' to exit): ") **********CHANGE BACK TO THIS****
        userAction = "Input"
        #EXIT
        '''
        if userAction == 'E' or userAction == 'e':
            personalMethods.exit()
        #FILEIN
        elif len(userAction) > 0:
            personalMethods.processInput(userAction)
        #INVALID
        else:
            print("Not a valid input")
        '''
        instructions = personalMethods.processInput(userAction)

        for x in range (0, int(personalMethods.numberOfInstructions)):
            index, doNextIntRepresentaiton = personalMethods.determineNextInstruction(instructions)
            newBurstDuration = personalMethods.fire(instructions[doNextIntRepresentaiton], quartus)
            if newBurstDuration != 0:
                instructions[doNextIntRepresentaiton].burstDuration = newBurstDuration
                queue.append(instructions[doNextIntRepresentaiton])
                print("\ninstruction(",instructions[doNextIntRepresentaiton].instructionName,") moved to queue", end='')
                print("\nQueue is now: ")
                for q in queue:
                    print("ins(",q.instructionName,") with remaining burst time --> ",q.burstDuration," and PRIORITY --> ",q.priority)
                instructions.remove(instructions[doNextIntRepresentaiton])

        print("The CPU counter is at: ", personalMethods.cpuCounter)
        personalMethods.exit()
