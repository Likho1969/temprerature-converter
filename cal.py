# importing tkinter module
from tkinter import *

root = Tk()  # creating window
root.title("Ideal BMI")   # naming window
root.geometry("1000x800")  # setting window size
root.config(bg="blue")      # setting window background color


label_text = StringVar()
clicked = StringVar()


# defining actual BMI function
def bmi_calculator():
    bmi = float(weight_entry.get()) / (float(Height_entry.get()) / 100)*2
    label_text.set("%0.2f" % bmi)

    if bmi < 18:
        return "your underweight "
    elif bmi >= 18 and 25:
        return "normal"
    elif bmi >= 25 < 30:
        return "overweight"
    else:
        return "Obese"


# defining the male ideal bmi
def male_ideal_bmi(*args):
    male_ideal = float(0.5 * weight_entry.get() / (float(Height_entry.get() / 100)))**2 + 11.5
    label_text.set("%0.2f" % male_ideal_bmi)


def female_ideal_bmi(*args):
    female_ideal = float(0.5 * weight_entry.get() / float(Height_entry.get() / 100))**2 + 0.03 * float(age_entry.get()) + 11
    label_text.set("%0.2f" % female_ideal_bmi)


def clear():
    weight_entry.delete(0, END)
    Height_entry.delete(0, END)
    age_entry.delete(0, END)


def close():
    return root.destroy()


frame_1 = Frame(root, width=100, highlightbackground='black', highlightthickness=2)
frame_1.grid(row=0, column=0, padx=20, pady=20, ipadx=20, ipady=20)
weight_label = Label(frame_1, text="Weight:")
height_label = Label(frame_1, text="height:")
kilograms_label = Label(frame_1, text="kilograms")
cm_label = Label(frame_1, text="CM")
gender_label = Label(frame_1, text="Gender:")
age_label = Label(frame_1, text="Age")
drop = OptionMenu(frame_1, clicked, "Male", "Female")

weight_entry = Entry(frame_1)
Height_entry = Entry(frame_1)
age_entry = Entry(frame_1)

weight_label.grid(row=3, column=0)
weight_entry.grid(row=3, column=2)
kilograms_label.grid(row=3, column=3)
height_label.grid(row=5, column=0)
Height_entry.grid(row=5, column=2)
cm_label.grid(row=5, column=3)
gender_label.grid(row=6, column=0)
drop.grid(row=6, column=2)
age_label.grid(row=6, column=4)
age_entry.grid(row=6, column=5)

calculate_button = Button(root, text="calculate your ideal Body Mass Index", width=50, command=bmi_calculator)
calculate_button.grid(row=7, column=0, sticky=W+E+N+S)
add = Label(root, text="", textvariable=label_text).grid(row=8, column=1, sticky=W)

BMI_label = Label(root, text="BMI:")
BMI_label.grid(row=8, column=0)
Ideal_label = Label(root, text="ideal :")
Ideal_label.grid(row=8, column=2)

clear = Button(root, text="clear", command=clear)
clear.grid(row=10, column=0)

exit_button = Button(root, text="exit program", command=close)
exit_button.grid(row=10, column=2)

root.mainloop()
