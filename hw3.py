class Instruction:

    def __init__(self):
        self.arrivalTime = 0
        self.priority = 0
        self.burstDuration = 0

class personalMethods:

    def exit(self):
        print("Exiting script")
        exit()

    def processInput(self, userFileName) -> [Instruction]:
        instructions = []
        tempData = []
        numberOfInstructions = 0
        with open(userFileName + ".txt", "r") as f:
            # number of instructions is first line (just for verifying array length)
            numberOfInstructions = f.readline()

            for line in f:
                print("line is: ")
                print(line)
                print("Individual numbers are: ")
                individualNumbers = line.split()
                print(individualNumbers)
                tempInstruction = Instruction()
                tempInstruction.arrivalTime = individualNumbers[0]
                tempInstruction.priority = individualNumbers[1]
                tempInstruction.burstDuration = individualNumbers[2]

        print("Number of Instructions: ",numberOfInstructions)
        exit()

if __name__ == '__main__':
    #INITIALIZE
    myInstruction = Instruction()
    personalMethods = personalMethods()

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
        personalMethods.processInput(userAction)
