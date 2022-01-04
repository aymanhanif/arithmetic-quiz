from tkinter import *  # The TkInter module within the Python library is imported into the file
import random  # The random functions within the Python library are imported into the file


global y, counter, quizScore, answers, questions, operations, score, file, qShuffle, lines, wAdd, wSub, wMulti, wDiv


file = open("Results.txt","r") # Opens the 'Results' file in a read format to the variable 'file'
lines = file.readlines()# creates a list, 'lines', where each value in the list is the values of each line in the 'Results' file
score = int(lines[0])# sets the variable 'score' to have the value stored on the first line of the 'Results' file

wAdd = 0 # The number of incorrect addition questions is set to 0
wSub = 0 # The number of incorrect subtraction questions is set to 0
wMulti = 0 # The number of incorrect multiplication questions is set to 0
wDiv = 0 # The number of incorrect division questions is set to 0

global targetNeeded # A global variable, 'targetNeeded', is created
targetNeeded = False # the value of this global variable is set to 'False'

y = 0 # The value of the variable 'y', which holds the value of which index in the questions list the program is on, is set to 0 as default
counter = 0 # The value of the variable 'counter' for the number of questions is set to 0 as default
quizScore = 0 # The value of the variable 'quizScore' is set to 0 as default 

questions = ["","","","","","","","","",""] # An empty list of 10 elements is created, this will later be filled with questions
answers = ["","","","","","","","","",""] # An empty list of 10 elements is created, this will later be filled with corresponding answers
operations = ["","","","","","","","","",""] # An empty list of 10 elements is creates, this will be filled with corresponding operations


## Menu GUI ##
    
global mainOpen # The function 'mainOpen' is declared as a global function
def mainOpen(): # A function, 'mainOpen', is defined taking in no parameters
    global qShuffle # The variable 'qShuffle' is declared as a global variable
    qShuffle = False # The value of 'qShuffle' is set to 'False' as default
    global mainWindow # The variable 'mainWindow' is declared as a global variable
    global exitFlag # The variable 'mainWindow' is declared as a global variable
    exitFlag = False # The value of 'exitFlag' is set to 'False' as default

    mainWindow = Tk() # The variable 'mainWindow' opens a new TkInter window
    mainWindow.geometry("300x240") # The dimensions of this window are set to 300x240
    mainWindow.configure(background='white') # The background colour of the window is set to white
    mainWindow.title("Arithmetic Quiz") # The tile of the window is set to 'Arithmetic Quiz'

    title = Label(mainWindow, text="Welcome to the Arithmetic Quiz!") # A label, 'title', is created with the text 'Welcome to the Arithmetic Quiz'
    title.configure(background='white') # The background colour of this label is set to white
    title.pack() # This title is packed in the the window

    selection = Label(mainWindow, text="Please select a quiz.") # A label, 'selection', is created with the text 'Please select a quiz.'
    selection.configure(background='white') # The background colour of this label is set to white
    selection.pack() # This label is packed in the window underneath the previous widget

    topFrame = Frame(mainWindow) # This divides the main window into 2 sections, the top and bottom frame
    topFrame.pack(side = TOP) # 'topFrame' is assigned to the top side of the window
    topFrame.configure(background='white') # The background colour of this frame is set to white

    bottomFrame = Frame(mainWindow) # This divides the main window into 2 sections, the top and bottom frame
    bottomFrame.pack(side = BOTTOM) # 'bottomFrame' is assigned to the bottom side of the window
    bottomFrame.configure(background='white') # The background colour of this frame is set to white

    add = Button(topFrame, text="Addition Quiz", font="Calibri 11", fg="red", command = lambda: addition(score, questions, answers), width = 15, height = 1) # A button, 'add' is created set to run the 'addition' function with the stated parameters
    sub = Button(topFrame, text="Subtraction Quiz", font="Calibri 11", fg="blue", command = lambda: subtraction(score, questions, answers), width = 15, height = 1) # A button, 'sub' is created set to run the 'subtraction' function with the stated parameters
    multi = Button(topFrame, text="Multiplication Quiz", font="Calibri 11", fg="green", command = lambda: multiplication(score, questions, answers), width = 15, height = 1) # A button, 'multi' is created set to run the 'multiplication' function with the stated parameters
    div = Button(topFrame, text="Division Quiz", font="Calibri 11", fg="orange", command = lambda: division(score, questions, answers), width = 15, height = 1) # A button, 'div' is created set to run the 'division' function with the stated parameters
    shuffle = Button(topFrame, text="Shuffle Quiz", font="Calibri 11", fg="purple", command = lambda: Shuffle(questions, operations, answers), width = 15, height = 1) # A button, 'shuffle' is created set to run the 'Shuffle' function with the stated parameters
    stats = Button(topFrame, text="Statistics", font="Calibri 11", fg="black", command = statistics, width = 15, height = 1) # A button, 'stats' is created set to run the 'statistics' function
    mainExit = Button(topFrame, text="Exit", font="Calibri 11", fg="red", command = lambda: quit(), width = 8, height = 1) # A button, 'mainExit' is created set to run the 'quit()' function that exists within Python

    add.grid(row=0, column=0, sticky=E, padx=5, pady=3) # The 'add' button is placed in a grid layout in the first row and first column
    sub.grid(row=0, column=1, sticky=W, padx=5, pady=3) # The 'sub' button is placed in a grid layout in the first row and second column
    multi.grid(row=1, column=0, sticky=E, padx=5, pady=3) # The 'multi' button is placed in a grid layout in the second row and first column
    div.grid(row=1, column=1, sticky=W, padx=5, pady=3) # The 'div' button is placed in a grid layout in the second row and second column
    shuffle.grid(row=2, columnspan = 2, padx=5, pady=3) # The 'shuffle' button is placed in a grid layout in the third row and across the two columns
    stats.grid(row=3, columnspan = 2, pady=3) # The 'stats' button is placed in a grid layout in the fourth row and across the two columns
    mainExit.grid(row=4, columnspan = 2, pady=5) # The 'mainExit' button is placed in a grid layout in the fifth row and across the two columns

    mainWindow.mainloop()

## Question Generators ##
def addition(score, questions, answers): # A function, 'addition', is defined taking the stated parameters
    mainWindow.destroy() # The main menu window is closed by the program
    x = 0 # The value of the question generation counter, 'x', is set to 0
    while(x < 10): # The program enters a loop so long as 'x' is less than 10
        if score >= 50: # if the value of 'score' is greater than or equal to 50
            a = random.randint(1,250) # a random number between 1 and 250 will be generated and stored as 'a'
            b = random.randint(1,250) # a random number between 1 and 250 will be generated and stored as 'b'
        elif score >= 40: # if the value of 'score' is greater than or equal to 40
            a = random.randint(1,200)# a random number between 1 and 200 will be generated and stored as 'a'
            b = random.randint(1,200)# a random number between 1 and 200 will be generated and stored as 'b'
        elif score >= 30: # if the value of 'score' is greater than or equal to 30
            a = random.randint(1,150)# a random number between 1 and 150 will be generated and stored as 'a'
            b = random.randint(1,150)# a random number between 1 and 150 will be generated and stored as 'b'
        else: # if none of the prior conditions were met
            a = random.randint(1,100)# a random number between 1 and 100 will be generated and stored as 'a'
            b = random.randint(1,100)# a random number between 1 and 100 will be generated and stored as 'b'


        question = (str(a) + " + " + str(b) + ":") # a string, 'question', is formed, making an addition question with the numebers 'a' and 'b' 
        questions[x]=(question) # this string is stored at index 'x' in the 'questions' list
        
        answer = (a+b) # an integer, 'answer', is generated by adding the values of 'a' and 'b'
        answers[x] = (answer) # this integer is stored at index 'x' in the 'answers' list

        x += 1 # the value of 'x' is incremented by 1
  
    template(questions, answers) # the 'template' function is run with the stated parameters


def subtraction(score, questions, answers): # A function, 'subtraction', is defined taking the stated parameters
    mainWindow.destroy() # The main menu window is closed by the program
    x = 0 # The value of the question generation counter, 'x', is set to 0
    while(x < 10): # The program enters a loop so long as 'x' is less than 10
        a = 2 # The value of 'a' is set to 2 as default
        b = 3 # The value of 'b' is set to 3 as default
        if score >= 50: # if the value of 'score' is greater than or equal to 50
            while a < b: # the program enteres a loop where so long as 'b' is greater than 'a'
                a = random.randint(1,250) # a random number between 1 and 250 will be generated and stored as 'a'
                b = random.randint(1,250) # a random number between 1 and 250 will be generated and stored as 'b'
        elif score >= 40: # if the value of 'score' is greater than or equal to 40
            while a < b: # the program enteres a loop where so long as 'b' is greater than 'a'
                a = random.randint(1,200) # a random number between 1 and 200 will be generated and stored as 'a'
                b = random.randint(1,200) # a random number between 1 and 200 will be generated and stored as 'b'
        elif score >= 30: # if the value of 'score' is greater than or equal to 30
            while a < b: # the program enteres a loop where so long as 'b' is greater than 'a'
                a = random.randint(1,150) # a random number between 1 and 150 will be generated and stored as 'a'
                b = random.randint(1,150) # a random number between 1 and 150 will be generated and stored as 'b'
        else: # if none of the prior conditions were met
            while a < b: # the program enteres a loop where so long as 'b' is greater than 'a'
                a = random.randint(1,10) # a random number between 1 and 100 will be generated and stored as 'a'
                b = random.randint(1,10) # a random number between 1 and 100 will be generated and stored as 'b'

        question = (str(a) + " - " + str(b) + ":") #  a string, 'question', is formed, making a subtraction question with the numebers 'a' and 'b'
        questions[x] = (question) # this string is stored at index 'x' in the 'questions' list

        answer = (a-b) # an integer, 'answer', is generated by subtracting the values of 'a' and 'b'
        answers[x] = (answer) # this integer is stored at index 'x' in the 'answers' list

        x += 1 # the value of 'x' is incremented by 1
    
    template(questions,answers) # the 'template' function is run with the stated parameters

           
def multiplication(score, questions, answers): # A function, 'multiplication', is defined taking the stated parameters
    mainWindow.destroy() # The main menu window is closed by the program
    x = 0 # The value of the question generation counter, 'x', is set to 0
    while(x < 10): # The program enters a loop so long as 'x' is less than 10
        if score >= 50:# if the value of 'score' is greater than or equal to 50
            a = random.randint(1,12) # a random number between 1 and 12 will be generated and stored as 'a'
            b = random.randint(1,12) # a random number between 1 and 12 will be generated and stored as 'b'
        elif score >= 40: # if the value of 'score' is greater than or equal to 40
            a = random.randint(1,10) # a random number between 1 and 10 will be generated and stored as 'a'
            b = random.randint(1,10) # a random number between 1 and 10 will be generated and stored as 'a'
        elif score >= 30: # if the value of 'score' is greater than or equal to 30
            a = random.randint(1,7) # a random number between 1 and 7 will be generated and stored as 'a'
            b = random.randint(1,7) # a random number between 1 and 7 will be generated and stored as 'a'
        else: # if none of the prior conditions were met
            a = random.randint(1,5) # a random number between 1 and 5 will be generated and stored as 'a'
            b = random.randint(1,5) # a random number between 1 and 5 will be generated and stored as 'a'

        question = (str(a) + " x " + str(b) + ":") #  a string, 'question', is formed, making a multiplication question with the numebers 'a' and 'b'
        questions[x] = (question) # this string is stored at index 'x' in the 'questions' list

        answer = (a*b) # an integer, 'answer', is generated by multiplying the values of 'a' and 'b'
        answers[x] = (answer) # this integer is stored at index 'x' in the 'answers' list

        x += 1 # the value of 'x' is incremented by 1
    
        
    template(questions, answers) # the 'template' function is run with the stated parameters


def division(score, questions, answers): # A function, 'division', is defined taking the stated parameters
    mainWindow.destroy() # The main menu window is closed by the program
    x = 0 # The value of the question generation counter, 'x', is set to 0
    while(x < 10): # The program enters a loop so long as 'x' is less than 10
        a = 2 # The value of 'a' is set to 2 as default
        b = 3 # The value of 'b' is set to 3 as default
        if score >= 50: # if the value of 'score' is greater than or equal to 50
            while a % b != 0 or a > (b*12):# the program enteres a loop where so long as the modulus of a/b is not 0 or the value of a exceeds the answer to b*12
                a = random.randint(1,144) # a random number between 1 and 144 will be generated and stored as 'a'
                b = random.randint(1,12) # a random number between 1 and 12 will be generated and stored as 'b'
        elif score >= 40: # if the value of 'score' is greater than or equal to 40
            while a % b != 0 or a > (b*12): # the program enteres a loop where so long as the modulus of a/b is not 0 or the value of a exceeds the answer to b*12
                a = random.randint(1,100) # a random number between 1 and 100 will be generated and stored as 'a'
                b = random.randint(1,12) # a random number between 1 and 10 will be generated and stored as 'b'
        elif score >=30: # if the value of 'score' is greater than or equal to 30
            while a % b != 0 or a > (b*12): # the program enteres a loop where so long as the modulus of a/b is not 0 or the value of a exceeds the answer to b*12
                a = random.randint(1,49) # a random number between 1 and 49 will be generated and stored as 'a'
                b = random.randint(1,12) # a random number between 1 and 7 will be generated and stored as 'b'
        else: # if none of the prior conditions were met
            while a % b != 0 or a > (b*12): # the program enteres a loop where so long as the modulus of a/b is not 0 or the value of a exceeds the answer to b*12
                a = random.randint(1,25) # a random number between 1 and 25 will be generated and stored as 'a'
                b = random.randint(1,12) # a random number between 1 and 5 will be generated and stored as 'b'

        question = (str(a) + " ÷ " + str(b) + ":") # a string, 'question', is formed, making a division question with the numebers 'a' and 'b'
        questions[x] = (question) # this string is stored at index 'x' in the 'questions' list

        answer = (a//b) # an integer, 'answer', is generated by dividing the values of 'a' and 'b' and taking the integer answer
        answers[x] = (answer) # this integer is stored at index 'x' in the 'answers' list

        x += 1 # the value of 'x' is incremented by 1


    template(questions, answers) # the 'template' function is run with the stated parameters



def Shuffle(questions, operations, answers): #  A function, 'division', is defined taking the stated parameters
    global qShuffle # The variable 'qShuffle' is declared as a global variable
    qShuffle = True # The value of this variable is set to 'True'
    
    global lastScore # The variable 'lastScore' is declared as a global variable
    lastScore = int(lines[2]) # the variable takes the value from the third line of the 'Results' file
    recentScore = int(lines[3]) # the variable takes the value from the fourth line of the 'Results' file
    lastScore = recentScore # the 'lastScore' variable is overwritten with the value of the 'recentScore' variable

    mainWindow.destroy() # The main menu window is closed by the program

    global exitFlag # The variable 'exitFlag' is declared as a global variable
    exitFlag = True # The value of this variable is set to 'True' as the mainWindow has been closed

    ops = ("+", "-", "x", "÷") # A list of operations is formed under the variable name 'ops'
    x = 0 # The value of the question generation counter, 'x', is set to 0

    while(x < 10): # The program enters a loop so long as 'x' is less than 10
        operation=random.choice(ops) # the variable, 'operation', takes a random choice from the elements of the list 'ops'
        operations[x] = (operation) # this operation is stored at index 'x' in the 'operations' list

        if operation == "+": # if the chosen operation was addition, the number generation module of the addition function is carried out
            if score >= 50: #
                a = random.randint(1,250) #
                b = random.randint(1,250) #
            elif score >= 40: #
                a = random.randint(1,200) #
                b = random.randint(1,200) #
            elif score >= 30: #
                a = random.randint(1,15) #
                b = random.randint(1,150) #
            else: #
                a = random.randint(1,100) #
                b = random.randint(1,100) #

            answer = (a+b) #
            answers[x] = (answer) # the answer is generated and stored as usual


        elif operation == "-": # if the chosen operation was subtraction, the number generation module of the subtraction function is carried out
            a = 2 #
            b = 3 # 
            if score >= 50: #
                while a < b: #
                   a = random.randint(1,250) #
                   b = random.randint(1,250) #
            elif score >= 40: #
                while a < b: #
                    a = random.randint(1,200) #
                    b = random.randint(1,200) #
            elif score >= 30: #
                while a < b: #
                    a = random.randint(1,150) #
                    b = random.randint(1,150) #
            else: #
                while a < b: #
                    a = random.randint(1,100) #
                    b = random.randint(1,100) #

            answer = (a-b) #
            answers[x] = (answer) # the answer is generated and stored as usual


        elif operation == "x": # if the chosen operation was multiplication, the number generation module of the multiplication function is carried out
            if score >= 50: #
                a = random.randint(1,12) #
                b = random.randint(1,12) #
            elif score >= 40: #
                a = random.randint(1,10) #
                b = random.randint(1,10) #
            elif score >= 30: #
                a = random.randint(1,7) #
                b = random.randint(1,7) #
            else:#
                a = random.randint(1,5) #
                b = random.randint(1,5) #

            answer = (a*b) #
            answers[x] = (answer) # the answer is generated and stored as usual


        elif operation == "÷": # if the chosen operation was division, the number generation module of the division function is carried out
            a = 2 #
            b = 3 #
            if score >= 50: #
                while a % b != 0 or a > (b*12): #
                   a = random.randint(1,144) #
                   b = random.randint(1,12) #
            elif score >= 40: #
                while a % b != 0 or a > (b*12): #
                    a = random.randint(1,100) #
                    b = random.randint(1,12) #
            elif score >=30: #
                while a % b != 0 or a > (b*12): #
                    a = random.randint(1,49) #
                    b = random.randint(1,12) #
            else: #
                while a % b != 0 or a > (b*12): #
                    a = random.randint(1,25) #
                    b = random.randint(1,12) #

            answer = (a//b) #
            answers[x] = (answer) # the answer is generated and stored as usual


        question = (str(a) + " " + (operation) + " " + str(b) + ":") # a string is formed by taking the value of 'a' and 'b' and placing the value of 'operation' in between to form a question
        questions[x]=(question) # This string is stored at index 'x' in the 'questions' list

        x += 1 # the value of 'x' is incremented by 1
        
    
    template(questions, answers) # the 'template' function is run with the stated parameters

    return qShuffle # the changed value of the variable 'qShuffle' is returned by the function
    


## Template GUI ##
def template(questions, answers): # A function, 'template', is defined taking the stated parameters, this will display the first screen of any quiz
    global root # the variable 'root' is made global
    root = Tk() # 'root' opens a new TkInter window
    root.geometry("250x190") # The dimensions of this window are set to 250x190
    root.configure(background='white') # The background colour of the window is set to white 
    root.title("Quiz") # The title of the window is set to say 'Quiz'
    root.grid_columnconfigure(0, weight = 1) # Each column is given a buffer zone of 1 unit of space
    root.grid_rowconfigure(0, weight = 1) # Each row is given a buffer zone of 1 unit of space

    
    global qNum, qName, qResponse, qScore # The stated variables are declared as global variables 
    qNum = Label (root, text = ("Question 1"), font="Calibri 15") # A label, 'qNum', is created with the text 'Question 1' 
    qNum.configure(background='white') # The background of this label is set to be white
    qNum.grid(row = 0, columnspan = 2, pady = 5, sticky = N) # This label is added to a grid layout in the first row


    qName = Label(root, text =(questions[0]), font ="Calibri 12") # A label, 'qName', is created, containing the question stored in index 0 of 'questions' i.e. the first question
    qName.configure(background='white') # The background of this label is set to be white
    qName.grid(row = 1, columnspan = 2, pady = 5) # This label is added to the grid layout in the second row
        
    global AnswerBox # The variable 'AnswerBox' is declared as a global variable
    AnswerBox = Entry(root, width=10,background='white') # An entry box, 'AnswerBox', is created within the 'root' window with the background colour being white
    AnswerBox.grid(row = 2, columnspan = 2, pady = 5) # This is added to the grid layout in the third row

    global submit # the variable 'submit' is declared as a global variable
    submit = Button(root, text="Submit", font="Calibri 11", fg="orange", command = lambda: Submit(answers,(AnswerBox.get()), score),width = 5, height = 1) # A button, 'submit', is created, holding the command to carry out the 'Submit' function with the stated parameters
    submit.grid(row = 3, pady = 2) # This is added to the grid layout in the fourth row

    submit.config(state=DISABLED) # The 'submit' button is set to be disabled by default, meaning the user cannot interact with it
    global validPresence # the function 'validPresence' is declared as a global function
    def validPresence(key): # A function, 'validPresence' is defined taking the stated parameters
        submit.config(state=NORMAL) # The function changes the state of the submit button to normal, allowing the user to interact with it
    AnswerBox.bind("<Key>", validPresence) # The function is called when any key has been pressed in the 'AnswerBox', such that they cannoy press the button until they enter an answer 
    
    qResponse = Label (root, text = (" ")) # A label, 'qResponse', is created holding no value as the user has not answered any questions at this point
    qResponse.configure(background='white') # The background colour of this label is set to be white
    qResponse.grid(row = 4, pady = 1) # This is added to the grid layout in the fifth row


    qScore = Label(root, text = "Score: " + str(quizScore) + " out of 10") # A label, 'qScore', is created showing the users current score using the variable 'quizScore' 
    qScore.configure(background='white') # The background colour of this label is set to be white
    qScore.grid(row = 5, pady = 5) # This is added to the grid layout in the sixth row
              
    root.mainloop() # The mainloop command stops the window from closing until the user decides to close it



## Submit Function ##
def Submit(answers, x, score): # A function, 'division', is defined taking the stated parameters
    validInteger = x.isnumeric() # a variable, 'validInteger', is created and checks whether the value 'x', which is the users inputted answer to the question in this function, is an integer
    if validInteger == True: # if the value of 'validInteger' is 'True'
    
        global counter, y, quizScore, qNum # the stated variables are set as global variables
        counter += 1 # the variable 'counter' is incremented by 1
        AnswerBox.delete(0, END) # the entry box, 'AnswerBox' is cleared

        global wAdd, wSub, wMulti, wDiv # the stated variables are set as global variables
    
        if counter != 11: # the program enters a branch where if the value of 'counter' is not equal to 11
            if((answers[y])) == int(x): # the program enters another branch where it checks if the users answer is the same as the correct answer, if it is
                y += 1 # the value of 'y' is incremented by 1

                score += 1 # the value of 'score' is incremented by 1
                quizScore += 1 # the value of 'quizScore' is incremented by 1
                qScore.config(background='white', text = "Score: " + str(quizScore) + " out of 10") # the label 'qScore' is changed to hold the updated score
                qResponse.config(background='white', text = ("Well done you got it correct!"),font="Calibri 10") # the label 'qResponse' is updated to inform the user they got the answer correct
            else: # if the users answer is not the same as the correct answer
                y += 1 # the value of 'y' is incremented by 1
        
                qResponse.config(background='white', text = ("Sorry you got it wrong!"),font="Calibri 10") # the label 'qResponse' is updated to inform the user they got the answer incorrect

                if operations[y-1] == "+": # if the operation of the last question, which was answered incorrectly, was addition
                    wAdd += 1 # the value of 'wAdd' is incremented by 1
                elif operations[y-1] == "-": # if the operation of the last question, which was answered incorrectly, was subtraction
                    wSub += 1 # the value of 'wSub' is incremented by 1
                elif operations[y-1] == "x": # if the operation of the last question, which was answered incorrectly, was multiplication
                    wMulti += 1 # the value of 'wMulti' is incremented by 1
                elif operations[y-1] == "÷": # if the operation of the last question, which was answered incorrectly, was division
                    wDiv += 1 # the value of 'wDiv' is incremented by 1
            
        
            if y == 10: # the program enters another branch where if the value of y is equal to 10, such that the end of the quiz has been reached
                AnswerBox.destroy() # the entry box for the user to enter their answers in disappears
                qPlaceHolder = Label(root, text = (" "), background='white') # a place holder label, with a blank value, is created
                qPlaceHolder.grid(row = 2, columnspan = 2, pady = 5) # this is placed where the Answer would usually go
                qNum.config(background='white', text = (" "), font="Calibri 15") # the label 'qNum' is made blank so it is essentially removed without changing the rest of the layout
                qName.config(background='white', text =("End of Quiz."), font ="Calibri 12") # the label 'qName' is made blank so it is essentially removed without changing the rest of the layout
                submit.config (text="Quit", font="Calibri 11", fg="orange", command = lambda: Quit(y),width = 5, height = 1) # the 'submit' button now says 'Quit' and holds the command to the 'Quit' function

            else: # if y is not equal to 10
                qNum.config(background='white', text = ("Question " + str(y+1)), font="Calibri 15") # The 'qNum' label is updated with the next question number
                qName.config(background='white', text =(questions[y]), font ="Calibri 12") # The 'qName' label is updated with the next question
                submit.config(state=DISABLED) # The 'submit' buttons state is set to disabled so that the user cannot click it
                AnswerBox.bind("<Key>", validPresence) # The condition for the 'validPresence' function to be carried out is specified and applied to the 'AnswerBox'
    else: # if the user's input is not valid i.e. is not an integer
        AnswerBox.delete(0, END) # the entry box for the user to enter their answers in disappears
        submit.config(state=DISABLED) # The 'submit' buttons state is set to disabled so that the user cannot click it



## Statistics Function ##
def statistics(): # A function, 'statistics', is defined taking in no parameters
    if exitFlag == False: # The program enters a branch where is the value of 'exitFlag' is 'False', such that the main menu window has not been closed
        mainWindow.destroy() # The program will close the 'mainWindow' i.e. the main menu
    
    global root # The variable 'root' is declared as a global variable
    root = Tk() # 'root' opens a new TkInter window 
    root.geometry("250x270") # The dimensions of this window are set to 250x270
    root.configure(background='white') # The background colour of this window is set to white
    root.title("Stats") # The title of this window is set to 'Stats'
    root.grid_columnconfigure(0, weight = 1) # Each column is given a buffer zone of 1 unit of space 
    root.grid_rowconfigure(0, weight = 1) # Each row is given a buffer zone of 1 unit of space

    file = open('Results.txt','r') # The file 'Results' is open in a read format
    lines = file.readlines() # creates a list, 'lines', where each value in the list is the values of each line in the 'Results' file

    title = Label(root, background ='white', text = "Statistics", font = "Calibri 14") # A label, 'title', is created with the text 'Statistics'
    title.grid(row = 0, columnspan = 2, pady = 1, sticky = N) # This is added to a grid layout in the first row

    sScore = Label(root, background ='white', text = "Overall Score: " + lines[0]) # A label, 'sScore', is created with the text 'Overall Score:' followed by the value stored in the first line of the 'Results' file
    sScore.grid(row = 1, columnspan = 2, pady = 1, sticky = N) # This is added to the grid layout in the second row
    
    sHighScore = Label(root, background ='white', text = "High Score: " + lines[1]) # A label, 'sHighScore', is created with the text 'High Score:' followed by the value stored in the second line of the 'Results' file 
    sHighScore.grid(row = 2, columnspan = 2, pady = 1, sticky = N) # This is added to the grid layout in the third row
    
    sLastScore = Label(root, background ='white', text = "Last Score: " + lines[2]) # A label, 'sLastScore', is created with the text 'Last Score:' followed by the value stored in the third line of the 'Results' file 
    sLastScore.grid(row = 3, columnspan = 2, pady = 1, sticky = N) # This is added to the grid layout in the fourth row
    
    sRecentScore = Label(root, background ='white', text = "Recent Score: " + lines[3]) # A label, 'sRecentScore', is created with the text 'Recent Score:' followed by the value stored in the fourth line of the 'Results' file
    sRecentScore.grid(row = 4, columnspan = 2, pady = 1, sticky = N) # This is added to the grid layout in the fifth row

    if targetNeeded == True: # The program enters a branch where is the value of the variable 'targetNeeded' is 'True', such that the user has got a question wrong
        sTarget = Label(root, background ='white',text = "Your target is to focus on the " + lines[4] + "quiz.") # A label, 'sTarget', is created with the text 'Your target is to focus on the' followed by the value stored in the fifth line of the 'Results' file 'quiz'
    else: # if the value of 'targetNeeded' is 'False', such that the user has not got anything wrong
        sTarget = Label(root, background ='white', text = "Well done! You have no target!") # A label, 'sTarget', is created with the text 'Well done! You have no target!'
    sTarget.grid(row = 5, columnspan = 2, pady = 1, sticky = N) # This is added to the grid layout in the sixth row

    sExit = Button(root, text="Exit", font="Calibri 11", fg="orange", width = 5, height = 1 ) # A button, 'sExit', is created with no command assigned to it as this will be determined by whether or not the user has played a quiz or not
    sExit.grid(row = 6, columnspan = 2, pady = 3, sticky = N) #

    if qShuffle == True: # The program enters a branch where if the value of 'qShuffle' is 'True', such that the user has played a shuffle quiz
        sExit.config(command= lambda: quit()) # the command assigned to 'sExit' is set to be the 'quit()' function that exists within Python
    else: # if the value of 'qShuffle' is 'False', such that the user has not played a shuffle quiz
        sExit.config(command = lambda: exitStats()) # the command assigned to 'sExit' is set to be the 'exitStats' function

    root.mainloop() # The mainloop command stops the window from closing until the user decides to close it



## Quit Function ##
def Quit(y): # A function, 'Quit', is defined taking in the stated parameters
    #root.destroy() # The window opened under the 'root' variable is closed

    global qShuffle
    if qShuffle == True: # The program enters a branch where is the value of 'qShuffle' is 'True', such that the user has played a shuffle quiz
        global highScore, lastScore, recentScore # The stated variables are declared as global variables
        highScore = int(lines[1]) # The variable 'highScore' takes the value stored in the second line of the 'Results' file
        recentScore = int(quizScore) # The variable 'recentScore' taked the value stored in the variable 'quizScore'

        global score # The variable 'score' is declared as a global variable
        score += int(quizScore) # The variable 'score' is incremented by the value stored in the variable 'quizScore'

        if recentScore > highScore: # The program enters a branch where if the value of 'recentScore' is greater than the value of 'highScore', such that the users latest score is the new highest score they have achieved
            highScore = recentScore # The value of 'highScore' is set to the value of 'recentScore'
        
        file = open( 'Results.txt', 'w' ) # A new file named 'Results' is created in a write format to the variable 'file'
        file.write( repr(score) + '\n') # The value of 'score' is written to the first line
        file.write( repr(highScore) + '\n' ) # The value of 'highScore' is written to the second line
        file.write( repr(lastScore) + '\n' ) # The value of 'lastScore' is written to the third line
        file.write( repr(recentScore) + '\n' ) # The value of 'recentScore' is written to the fourth line
        
        incorrect = [wAdd,wSub,wMulti,wDiv] # A variable, 'incorrect', is defined containing a list of the variables 'wAdd', 'wSub', 'wMulti' and 'wAdd'
        global target # The variable 'target' is declared as a global variable
        weakest = incorrect.index(max(incorrect)) # A variable, 'weakest', is defined taking the index value of the highest value in the 'incorrect' list, such that it takes the index of the worst performing topic

        if (max(incorrect)) == 0: # The program enters a branch where if the highest number of questions the user got incorrect in any topic is 0 i.e. they got nothing incorrect
            global targetNeeded # the variable 'targetNeeded' is declared as a global variable
            targetNeeded = False # the value of 'targetNeeded' is set to 'False'
            target = 0 # the value of 'target' is set to 0
        else: # if the highest number of questions the user has got incorrect is not 0, such that they have got something incorrect 
            targetNeeded = True # the value of 'targetNeeded' is set to 'True'
            if weakest == 0: # The program enters a branch where if the value of 'weakest' is 0, therefore being the first index meaning the weakest topic was addition
                target = "addition" # The value of 'target' is set to 'addition'
            elif weakest == 1: # if the value of 'weakest' is 1, therefore being the second index meaning the weakest topic was subtraction
                target = "subtraction" # The value of 'target' is set to 'subtraction'
            elif weakest == 2: # if the value of 'weakest' is 2, therefore being the third index meaning the weakest topic was multiplication 
                target = "multiplication" # The value of 'target' is set to 'multiplication'
            elif weakest == 3: # if the value of 'weakest' is 3, therefore being the fourth index meaning the weakest topic was division
                target = "division" # The value of 'target' is set to 'division'
        
        file.write( repr(target) + '\n' ) # The value of 'target' is written to the fifth line
        
        file.close() # The 'Results' file is saved and closed
    
        statistics() # The program runs the 'statistics' function, opening the statistics window

    quit() # This ends the program and is run if the value of 'qShuffle' is 'False', such that the user has not just completed a shuffle quiz



def exitStats(): # A function, 'exitStats', is defined taking in no parameters
    root.destroy() # The window opened under the variable 'root' is closed
    mainOpen() # The function 'mainOpen' is run, opening the main menu


## Run Program ##
mainOpen()
