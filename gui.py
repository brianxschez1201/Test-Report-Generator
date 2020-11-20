from tkinter import *
from tkcalendar import *
from datetime import datetime

#_______________________________________________________________________________
# Root widget (window)

root = Tk()
root.geometry("400x480")
root.resizable(width=False, height=False)

#_______________________________________________________________________________
# Page variable

page = 1

#_______________________________________________________________________________
# Data

name = None
id = None
grade = None
date = None
test_type = None

#_______________________________________________________________________________

# Utility and button click methods

def nextButtonClick():

    global page

    if page == 2:

        global name, id, grade, date, test_type

        name = name_entry.get()
        id = id_entry.get()
        grade = clicked_grade.get()
        date = date_picker.get_date()
        test_type = clicked_test.get()

    clear(root)

    if page == 1:
        pageTwo()

    page += 1

def getCurDate_DYM():
    today = datetime.today()

    cur_year = int(today.strftime("%y"))
    cur_month = int(today.strftime("%m"))
    cur_day = int(today.strftime("%d"))

    return (cur_year, cur_month, cur_day)

def clear(root):
    slaves = root.grid_slaves()
    for slave in slaves:
        slave.destroy()

#_______________________________________________________________________________
# Widget definitions

# Page 1...

welcome_label1 = Label(root, text="Welcome!")
welcome_label2 = Label(root, text="You will be prompted to enter some info.")
welcome_label3 = Label(root, text="After that, you will have access to a virtual bubblesheet to submit your answers.")
next_button = Button(root, text="Next", command=nextButtonClick)



# Page 2...

# *** Add please_enter label later ***
name_label = Label(root, text="Student name:")
id_label = Label(root, text="Student ID:")
grade_label = Label(root, text="Grade:")
date_label = Label(root, text="Test Date:")
test_label = Label(root, text="Test Type:")

name_entry = Entry(root)

id_entry = Entry(root)

GRADE_LEVELS = [
"<Grade unselected>",
"8",
"9",
"10",
"11",
"12"
]
clicked_grade = StringVar(root)
clicked_grade.set("<Grade unselected>")
grade_dropdown = OptionMenu(root, clicked_grade, *GRADE_LEVELS)

cur_date = getCurDate_DYM()
cur_year = cur_date[0]
cur_month = cur_date[1]
cur_day = cur_date[2]
date_picker = Calendar(root, selectmode="day", year=cur_year, month=cur_month, day=cur_day)

TEST_TYPES = [
"<Test type unselected>",
"SAT",
"ACT",
"HSPT"
]
clicked_test = StringVar(root)
clicked_test.set("<Test type unselected>")
test_dropdown = OptionMenu(root, clicked_test, *TEST_TYPES)

next_button = Button(root, text="Next", command=nextButtonClick)

#_______________________________________________________________________________
# Pages

def pageOne():

    # Widget placement

    welcome_label1.grid(row=0, column=0, padx=10,pady=10)
    welcome_label2.grid(row=1, column=0, padx=10,pady=10)
    welcome_label3.grid(row=2, column=0, padx=10,pady=10)
    next_button.grid(row=3, column=0, padx=10,pady=10)

def pageTwo():

    # Widget placement

    name_label.grid(sticky="E", row=0, column=0, padx=10,pady=10)
    id_label.grid(sticky="E", row=1, column=0, padx=10,pady=10)
    grade_label.grid(sticky="E", row=2, column=0, padx=10,pady=10)
    date_label.grid(sticky="E", row=3, column=0, padx=10,pady=10)
    test_label.grid(sticky="E", row=5, column=0, padx=10,pady=10)

    name_entry.grid(sticky="W", row=0, column=1, padx=10,pady=10)
    id_entry.grid(sticky="W", row=1, column=1, padx=10,pady=10)
    grade_dropdown.grid(sticky="W", row=2, column=1, padx=10,pady=10)
    date_picker.grid(sticky="W", row=4, column=1, padx=10,pady=10)
    test_dropdown.grid(sticky="W", row=5, column=1, padx=10,pady=10)
    next_button.grid(row=6, column=0, padx=10,pady=10)

#_______________________________________________________________________________
# Execution

pageOne()

#while(page == 1):
#    continue

#_______________________________________________________________________________
# Event loop

root.mainloop()
