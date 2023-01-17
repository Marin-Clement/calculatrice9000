from tkinter import *

import customtkinter

expression = ""
history = []

button_color = 'black'
button_color2 = 'white'


def press(num):
    global expression

    expression = expression + str(num)

    equation.set(expression)


def equalpress():
    try:

        global expression

        total = str(eval(expression))

        equation.set(total)

        add_to_history(expression, total)

        expression = total
    except:

        equation.set(" error ")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


def add_to_history(expression, result):
    history.append((expression, result))
    update_history_display()


def clear_history():
    global history
    history = []
    update_history_display()


def update_history_display():
    global expression
    history_display.delete(0, END)
    for expression, result in history:
        history_display.insert(END, expression + " = " + result)
    history_display.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=history_display.yview)


root = Tk()
root.resizable(False, False)
root.configure(background='LightSkyBlue2')
root.title("Calculator")
root.geometry("400x450")

equation = StringVar()

expression_field = customtkinter.CTkEntry(master=root, textvariable=equation, width=360, height=50, corner_radius=100, fg_color='white', border_color='LightSkyBlue3', text_color='black', font=('Roboto', 25))
expression_field.grid(columnspan=10, pady=10, padx=20)

sqrt = customtkinter.CTkButton(master=root, text=" √ ", command=lambda: press("**0.5"), height=10, width=10, font=('Roboto', 30), corner_radius=50, fg_color='LightSkyBlue2', hover_color='grey', text_color='white')
sqrt.grid(row=1, column=0)
sqr = customtkinter.CTkButton(master=root, text=" x^2 ", command=lambda: press("**2"), height=10, width=10, font=('Roboto', 30), corner_radius=50, fg_color='LightSkyBlue2', hover_color='grey', text_color='white')
sqr.grid(row=1, column=1)

on = customtkinter.CTkButton(master=root, text=" 1/x ", command=lambda: press("1/"), height=10, width=10, font=('Roboto', 30), corner_radius=50, fg_color='LightSkyBlue2', hover_color='grey', text_color='white')
on.grid(row=1, column=2)

button0 = customtkinter.CTkButton(master=root, text=" 0 ", command=lambda: press(0), height=10, width=10, font=('Roboto', 30), corner_radius=50, fg_color='LightSkyBlue2', hover_color='grey', text_color='white')
button0.grid(row=5, column=0)

button1 = customtkinter.CTkButton(master=root, text=" 1 ", command=lambda: press(1), height=10, width=10, font=('Roboto', 30), corner_radius=50, fg_color='LightSkyBlue2', hover_color='grey', text_color='white')
button1.grid(row=2, column=0)

button2 = customtkinter.CTkButton(master=root, text=" 2 ", command=lambda: press(2), height=10, width=10, font=('Roboto', 30), corner_radius=50, fg_color='LightSkyBlue2', hover_color='grey', text_color='white')
button2.grid(row=2, column=1)

button3 = customtkinter.CTkButton(master=root, text=" 3 ", command=lambda: press(3), height=10, width=10, font=('Roboto', 30), corner_radius=50, fg_color='LightSkyBlue2', hover_color='grey', text_color='white')
button3.grid(row=2, column=2)

button4 = customtkinter.CTkButton(master=root, text=" 4 ", command=lambda: press(4), height=10, width=10, font=('Roboto', 30), corner_radius=50, fg_color='LightSkyBlue2', hover_color='grey', text_color='white')
button4.grid(row=3, column=0)

button5 = customtkinter.CTkButton(master=root, text=" 5 ", command=lambda: press(5), height=10, width=10, font=('Roboto', 30), corner_radius=50, fg_color='LightSkyBlue2', hover_color='grey', text_color='white')
button5.grid(row=3, column=1)

button6 = customtkinter.CTkButton(master=root, text=" 6 ", command=lambda: press(6), height=10, width=10, font=('Roboto', 30), corner_radius=50, fg_color='LightSkyBlue2', hover_color='grey', text_color='white')
button6.grid(row=3, column=2)

button7 = customtkinter.CTkButton(master=root, text=" 7 ", command=lambda: press(7), height=10, width=10, font=('Roboto', 30), corner_radius=50, fg_color='LightSkyBlue2', hover_color='grey', text_color='white')
button7.grid(row=4, column=0)

button8 = customtkinter.CTkButton(master=root, text=" 8 ", command=lambda: press(8), height=10, width=10, font=('Roboto', 30), corner_radius=50, fg_color='LightSkyBlue2', hover_color='grey', text_color='white')
button8.grid(row=4, column=1)

button9 = customtkinter.CTkButton(master=root, text=" 9 ", command=lambda: press(9), height=10, width=10, font=('Roboto', 30), corner_radius=50, fg_color='LightSkyBlue2', hover_color='grey', text_color='white')
button9.grid(row=4, column=2)

plus = customtkinter.CTkButton(master=root, text=" + ", command=lambda: press("+"), height=10, width=10, font=('Roboto', 30), corner_radius=50, fg_color='LightSkyBlue2', hover_color='grey', text_color='white')
plus.grid(row=2, column=3)

minus = customtkinter.CTkButton(master=root, text=" - ", command=lambda: press("-"), height=10, width=10, font=('Roboto', 30), corner_radius=50, fg_color='LightSkyBlue2', hover_color='grey', text_color='white')
minus.grid(row=3, column=3)

multiply = customtkinter.CTkButton(master=root, text=" * ", command=lambda: press("*"), height=10, width=10, font=('Roboto', 30), corner_radius=50, fg_color='LightSkyBlue2', hover_color='grey', text_color='white')
multiply.grid(row=4, column=3)

divide = customtkinter.CTkButton(master=root, text=" / ", command=lambda: press("/"), height=10, width=10, font=('Roboto', 30), corner_radius=50, fg_color='LightSkyBlue2', hover_color='grey', text_color='white')
divide.grid(row=5, column=3)

equal = customtkinter.CTkButton(master=root, text=" = ", command=equalpress, height=10, width=10, font=('Roboto', 30), corner_radius=50, fg_color='LightSkyBlue2', hover_color='grey', text_color='white')
equal.grid(row=5, column=2)

clear = customtkinter.CTkButton(master=root, text=" Clear ", command=clear, height=10, width=10, font=('Roboto', 30), corner_radius=50, fg_color='LightSkyBlue2', hover_color='grey', text_color='white')
clear.grid(row=5, column=1)

Decimal = customtkinter.CTkButton(master=root, text=" . ", command=lambda: press("."), height=10, width=10, font=('Roboto', 30), corner_radius=50, fg_color='LightSkyBlue2', hover_color='grey', text_color='white')
Decimal.grid(row=6, column=0)

history_display = Listbox(root, font=('Roboto', 15))
history_display.grid(row=7, column=0, columnspan=4, ipadx=100, pady=5)

scrollbar = Scrollbar(history_display)
scrollbar.pack(side=RIGHT, fill='both')

clear_history = customtkinter.CTkButton(master=root, text="Clear History", command=clear_history, height=10, width=10, font=('Roboto', 15), corner_radius=50, fg_color='LightSkyBlue2', hover_color='grey', text_color='white')
clear_history.grid(row=7, column=4)

root.mainloop()
