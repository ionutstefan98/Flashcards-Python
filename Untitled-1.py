from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from typing import MappingView
from tkinter import colorchooser
import json
import os



questions = [""]
answers = [""]


curr_question_ind = 0
curr_answer_ind = 0



collectionInstance = True

# CARDS AND LEARNING FUNCTIONS
def cards_collection():
    
    questions.append(questionBar.get())
    answers.append(answerBar.get())
    questionBar.delete(0, END)
    answerBar.delete(0, END)



def stopCollection():
    collectionInstance = False
    print(questions)
    print(answers)


def learning_state():
    
    curr_question.set(questions[curr_question_ind])


def show_answer():
    
    curr_answer.set(answers[curr_answer_ind])

def next_question():
    global curr_question_ind
    global curr_answer_ind

    curr_question_ind += 1
    curr_answer_ind += 1

    curr_question.set(questions[curr_question_ind])
    curr_answer.set("")

def reset():
    global curr_question_ind
    global curr_answer_ind

    curr_question_ind = 0
    curr_answer_ind = 0

    

def bye():
    pass

# MENU BAR FUNCTIONS

def menu_open():
    global questions
    global answers 

    with open("questions.json", "r") as f:
        questions = json.load(f)

    with open("answers.json", "r") as f:
        answers = json.load(f)

def menu_save():

    deck_location = filedialog.asksaveasfile(defaultextension=".json", filetypes=[("JSON File", ".json"), 
                                                                                    ("Text file", ".txt"), 
                                                                                    ("Logo file", ".logo"), 
                                                                                    ("All files", ".*"), 
                                                                                    ("HTML File", ".html")])

    
    #with open("testQ.json", "w") as f:
     #   json.dump(questions, f, indent=2)
        
    #with open("testA.json", "w") as f:
     #   json.dump(answers, f, indent=2)

def window_colorchooser():

    color = colorchooser.askcolor()
    hexColor = color[1]

    window.config(bg=hexColor)
    welcomeLabel.config(bg=hexColor)
    textbar_frame.config(bg=hexColor)
    t1buttons_frame.config(bg=hexColor)
    questionBar_label.config(bg=hexColor)
    answerBar_label.config(bg=hexColor)
    newcards_tab.config(bg=hexColor)
    learning_tab.config(bg=hexColor)
    questionText_label.config(bg=hexColor)
    learning_buttonframe.config(bg=hexColor)
    answerText_label.config(bg=hexColor)
    learning_frame.config(bg=hexColor)

def font_colorchooser():
    color = colorchooser.askcolor()
    hexColor = color[1]

    welcomeLabel.config(fg=hexColor)
    questionBar_label.config(fg=hexColor)
    answerBar_label.config(fg=hexColor)





window = Tk()
window.title("Flashy")
window.geometry("640x480")
notebook = ttk.Notebook(window)


#TABS
newcards_tab = Frame(notebook)
learning_tab = Frame(notebook)
decks_tab = Frame(notebook)

notebook.add(newcards_tab, text="Add New Cards")
notebook.add(learning_tab, text="Learn")
notebook.add(decks_tab, text="Decks")

notebook.pack(expand=True, fill="both")

menubar = Menu(window)

#NEW CARDS TAB
#--------------------------------------------------------------------------------------------------------------------------
welcomeLabel = Label(newcards_tab, 
                     text="Welcome!", 
                     padx=5, 
                     pady=10, 
                     font=("Arial", 12, "bold"))
welcomeLabel.pack()

#TEXT BARS
textbar_frame = Frame(newcards_tab)
textbar_frame.pack()

#QUESTION TEXTBAR
questionBar_label = Label(textbar_frame, text="Question:", font=("Arial", 12, "bold"))
questionBar_label.grid(column=0, row=0)
questionBar = Entry(textbar_frame, font=("Arial", 11, "italic"), width=60)
questionBar.grid(column=1, row=0, pady=5)

#ANSWER TEXTBAR
answerBar_label = Label(textbar_frame, text="Answer:", font=("Arial", 12, "bold"))
answerBar_label.grid(column=0, row=1)
answerBar = Entry(textbar_frame, font=("Arial", 11, "italic"), width=60)
answerBar.grid(column=1, row=1)

#BUTTONS
t1buttons_frame = Frame(newcards_tab)
t1buttons_frame.pack(pady=8)

newCardsBut = Button(t1buttons_frame, text="Add new cards", width=15, command=cards_collection)
newCardsBut.grid(column=0, row=0)

openFileBut = Button(t1buttons_frame, text="Open a set", width=15, command=menu_open)
openFileBut.grid(column=1, row=1, pady=10)

stopCollectionBut = Button(t1buttons_frame, text="Stop", width=15, command=stopCollection)
stopCollectionBut.grid(column=2, row=0,)

startlearningBut = Button(t1buttons_frame, text="Start Learning", width=15, command=learning_state)
startlearningBut.grid(column=1, row=0, padx=10)
#------------------------------------------------------------------------------------------------------------------


#LEARNING TAB
#------------------------------------------------------------------------------------------------------------------

#LEARNING STATE UI

curr_question = StringVar()
curr_answer = StringVar()

learning_frame = Frame(learning_tab)
learning_frame.pack(pady=10)

questionText_label = Label(learning_frame, 
                            text="Question:", 
                            font=("Arial", 12, "bold"))
questionText_label.grid(column=0, row=0)

questionText = Label(learning_frame, 
                    bg="white", 
                    font=("Arial", 12, "italic"), 
                    fg="black",
                    textvariable=curr_question, 
                    width=50, 
                    bd=1, 
                    relief=SUNKEN)
questionText.grid(column=1, row=0)

answerText_label = Label(learning_frame, 
                        text="Answer:", 
                        font=("Arial", 12, "bold"))
answerText_label.grid(column=0, row=1)

answerText = Label(learning_frame, 
                        bg="white", 
                        font=("Arial", 12, "italic"),
                        textvariable=curr_answer, 
                        width=50, 
                        bd=1, 
                        relief=SUNKEN)
answerText.grid(column=1, row=1, pady=10)


learning_buttonframe = Frame(learning_tab)
learning_buttonframe.pack()

showanswerBut = Button(learning_buttonframe, text="Show Answer", command=show_answer)
showanswerBut.grid(column=1, row=3)

nextquestionBut = Button(learning_buttonframe, text="Next Question", command=next_question)
nextquestionBut.grid(column=2, row=3, padx=15)

resetBut = Button(learning_buttonframe, text="Reset", command=reset)
resetBut.grid(column=3, row=3, pady=15)

#------------------------------------------------------------------------------------------------------------------

#DECKS TAB





window.config(menu = menubar)

# FILE MENU
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)


filemenu.add_command(label="Open", command=menu_open)
filemenu.add_command(label="Save", command=menu_save)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=quit)

# EDIT MENU

editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editMenu)

editMenu.add_command(label="Placeholder", command=window_colorchooser)


# PREFERENCES MENU

prefMenu = Menu(menubar, tearoff=0)
colorScheme = Menu(prefMenu, tearoff=0)
menubar.add_cascade(label="Preferences", menu=prefMenu)
prefMenu.add_cascade(label="Color Scheme", menu=colorScheme)

colorScheme.add_command(label="Background Color", command=window_colorchooser)
colorScheme.add_command(label="Font Color", command=font_colorchooser)


prefMenu.add_command(label="Placeholder")








window.mainloop()