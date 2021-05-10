# importing the tkinter module

import tkinter

root = tkinter.Tk()   # creating a window
root.title("Temperature Converter")   # naming the recently created window
root.geometry("1200x700")   # setting the size of the window
root.config(bg="tan")   # setting the background color for the window

# creating the Celsius to Fahrenheit LabelFrame

l1 = tkinter.LabelFrame(root,
                        text="Celsius to Fahrenheit",
                        font="sans-serif",
                        bg="blue",
                        fg="black",
                        bd=6,
                        padx=20,
                        pady=20)

l1.grid(row=2, column=0)      # positioning the l1 in the window

# creating the Entry for Celsius to Fahrenheit Frame

e1 = tkinter.Entry(l1,
                   state="disable")

e1. grid(row=4, column=0)    # positioning the e1 in the window


# defining function responsible for setting the state for Celsius
def cel_active():
    e2.configure(state='disable')
    e1.configure(state="normal")


# creating a button that when clicked will invoke the state of Celsius to Fahrenheit and calling the cel_active()

btn_active = tkinter.Button(root,
                            text="Active -Celsius to Fahrenheit",
                            font="sans-serif",
                            bg="light blue",
                            fg="black",
                            bd=5,
                            command=cel_active)

btn_active.grid(row=6, column=0)    # positioning the btn_active in the window


l2 = tkinter.LabelFrame(root,
                        text="Fahrenheit to Celsius",
                        font="sans-serif",
                        bg="red",
                        fg="black",
                        bd=6,
                        padx=20,
                        pady=20)

l2.grid(row=2, column=5)     # positioning the l2 in the window

e2 = tkinter.Entry(l2,
                   state="disable")

e2.grid(row=4, column=5)     # positioning the e2 in the window


# defining function responsible for setting the state for Fahrenheit

def far_active():
    e1.configure(state="disable")
    e2.configure(state="normal")


# creating a button that when clicked will invoke the state of Fahrenheit to Celsius and calling the far_active()

btn_active1 = tkinter.Button(root,
                             text="Active -Fahrenheit to Celsius",
                             font="sans-serif",
                             bg="orange",
                             fg="black",
                             bd=3,
                             command=far_active)

btn_active1.grid(row=6, column=5)    # positioning the btn_active1 in the window


# defining function that will exit/ close the window/ program

def close():
    root.destroy()


# creating exit button which and calling the close()

exit_btn = tkinter.Button(text="Exit Program",
                          font="sans-serif",
                          bg="black",
                          fg="red",
                          bd=5,
                          command=close)

exit_btn.place(x=50, y=300)   # positioning the exit_btn in the window


# defining function for converting celsius to fahrenheit

def convert_c():
    if e1["state"] == "normal" and e1.get() != "":
        celsius = float(e1.get())
        fahrenheit = (celsius*9/5)+32
        result_entry.insert(0, str(fahrenheit))


# defining function for converting fahrenheit to celsius

def convert_f():
    if e2["state"] == "normal" and e2.get() != "":
        fahrenheit = float(e2.get())
        celsius = (fahrenheit-32)*5/9
        result_entry.insert(0, celsius)


# creating the action button for converting Celsius to Fahrenheit

result_btn = tkinter.Button(root,
                            text="Convert C-F",
                            font="sans-serif",
                            bg="blue",
                            fg="light blue",
                            bd=5,
                            command=convert_c)

result_btn.grid(row=7, column=2, pady=30, padx=60)  # positioning the result_btn in the window


# creating the action button for converting Fahrenheit to Celsius and calling the convert_f()

result_btn2 = tkinter.Button(root,
                             text="Convert F-C",
                             font="sans-serif",
                             bg="red",
                             fg="orange",
                             bd=5,
                             command=convert_f)

result_btn2.grid(row=7, column=4, pady=30, padx=60)   # positioning the result_btn2 in the window


# creating the result_entry or output entry

result_entry = tkinter.Entry(root,
                             bg="yellow",
                             fg="black",
                             bd=5)

result_entry.place(x=300,
                   y=250,
                   width=300,
                   height=60)   # positioning the Entry in the window


# defining function that will delete the figure in the Entry box/ input box

def clear():
    e1.delete(0)
    e2.delete(0)
    result_entry.delete(0)


# creating the Clear button and calling the clear()

clear_btn = tkinter.Button(root,
                           font="sans-serif",
                           bg="green",
                           fg="white",
                           text="Clear",
                           bd=4,
                           command=clear)

clear_btn.place(x=50, y=250)     # positioning the clear_btn in the window

# starting the app

root.mainloop()
