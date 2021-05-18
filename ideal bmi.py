# Likho Kapesi

# A Program that takes an individuals weight, height, age and gender
# to determine their BMI and Ideal BMI.

from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox

# Creation of the window that displays the info.
root = Tk()
root.title("Ideal BMI Calculator")
root.geometry("900x700")
root.config(bg="DodgerBlue4")


def calc_bmi(weight, height):
    result = weight / (height / 100) ** 2
    bmi_result.insert(0, round(result, 2))


def calc_ideal_bmi():
    bmi = 0
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    gender = gender_combobox.get().lower()
    calc_bmi(weight, height)

    if gender == "male":
        result = 0.5 * weight / ((height / 100) ** 2) + 11.5
        bmi = round(result, 2)
        print(bmi)
        ideal_bmi_result.insert(0, round(result, 2))

        return bmi
    elif gender == "female":
        age = int(age_entry.get())
        result = 0.5 * weight / ((height / 100) ** 2) + 0.03 + age + 11
        bmi = round(result, 2)
        print(bmi)
        ideal_bmi_result.insert(0, round(result, 2))

        return bmi
    else:
        messagebox.showinfo('Return', "no gender was chosen")

    print(bmi)

    if bmi > 0:
        print(bmi)
        show_message(bmi)


def show_message(bmi):
    if bmi < 18:
        messagebox.showinfo('Return', 'Underweight')
    elif bmi >= 18 and bmi< 25:
        messagebox.showinfo('Return', 'Normal')
    elif bmi >= 25 and bmi< 30:
         messagebox.showinfo('Return', 'Overweight')
    else:
        messagebox.showinfo('Return', 'Obese')


def close_program():
    msg_box = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application', icon='warning')
    if msg_box == 'yes':
        root.destroy()
    else:
        messagebox.showinfo('Return', 'You will now return to the application screen')


def clear_everything():
    weight_entry.delete(0, END)
    height_entry.delete(0, END)
    age_entry.delete(0, END)
    gender_combobox.delete(0, END)
    bmi_result.delete(0, END)
    ideal_bmi_result.delete(0, END)


# The Ideal BMI calculator's Heading

head = Label(root, text="Ideal Body Mass Index", fg="white", bg="black")
head.place(x=225, y=30)
sub_head = Label(root, text="Calculator", fg="white", bg="black")
sub_head.place(x=260, y=50)


# The frame containing the space you need to input
# your information.

# The frame

input_data = LabelFrame(root, fg="blue", bg="gold", text="Enter your Age, Gender, Weight(kg), Height(cm)", width=350, height=155)
input_data.place(x=125, y=125)

# Weight entry

label_1 = Label(input_data, text="Weight:", fg="blue")
label_1.place(x=10, y=30)
weight_entry = Entry(input_data, bg="white", width=15)
weight_entry.place(x=63, y=30)
kg = Label(input_data, text="in kg", fg="blue")
kg.place(x=190, y=30)

# Height entry

label_2 = Label(input_data, text="Height:", fg="blue")
label_2.place(x=10, y=60)
height_entry = Entry(input_data, bg="white", width=15)
height_entry.place(x=63, y=60)
cm = Label(input_data, text="in cm", fg="blue")
cm.place(x=190, y=60)

# Gender entry

label_3 = Label(input_data, text="Gender:", fg="blue")
label_3.place(x=10, y=90)
gender_combobox = Combobox(input_data, values=("Male", "Female"), width=15)
gender_combobox.place(x=63, y=90)

# Age entry

label_4 = Label(input_data, text="Age:", fg="blue")
label_4.place(x=243, y=40)
age_entry = Entry(input_data, bg="white", width=3, state="normal")
age_entry.place(x=283, y=40)

# BMI button

bmi_button = Button(root, text="Calculate your ideal body mass index", command=calc_ideal_bmi, fg="blue")
bmi_button.place(x=155, y=290)

# BMI result

label_5 = Label(root, text="BMI:", fg="blue")
label_5.place(x=80, y=350)
bmi_result = Entry(root, state="normal", bg="red", fg="white", width=15)
bmi_result.place(x=115, y=350)

# Ideal BMI result

label_6 = Label(root, text="Ideal-BMI:", fg="blue")
label_6.place(x=280, y=350)
ideal_bmi_result = Entry(root, state="normal", bg="red", fg="white", width=15)
ideal_bmi_result.place(x=355, y=350)

# Exit button

exit_program = Button(root, text="EXIT", bg="red", fg="black", command=close_program)
exit_program.place(x=390, y=390)

# Clear button

clear = Button(root, text="CLEAR", fg='lime', bg="blue", command=clear_everything)
clear.place(x=140, y=390)

# start app

root.mainloop()
