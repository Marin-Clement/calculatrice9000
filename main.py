from tkinter import *

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


def update_history_display():
    global expression
    history_display.delete(0, END)
    for expression, result in history:
        history_display.insert(END, expression + " = " + result)
    history_display.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=history_display.yview)


root = Tk()

root.configure(background="grey")
root.title("Calculator")
root.geometry("270x300")

equation = StringVar()

expression_field = Entry(root, textvariable=equation, width=21)
expression_field.grid(columnspan=4, ipadx=70)

button0 = Button(root, text=' 0 ', fg=button_color2, bg=button_color,  command=lambda: press(0), height=1, width=7)
button0.grid(row=5, column=0)

button1 = Button(root, text=' 1 ', fg=button_color2, bg=button_color,  command=lambda: press(1), height=1, width=7)
button1.grid(row=2, column=0)

button2 = Button(root, text=' 2 ', fg=button_color2, bg=button_color, command=lambda: press(2), height=1, width=7)
button2.grid(row=2, column=1)

button3 = Button(root, text=' 3 ', fg=button_color2, bg=button_color, command=lambda: press(3), height=1, width=7)
button3.grid(row=2, column=2)

button4 = Button(root, text=' 4 ', fg=button_color2, bg=button_color, command=lambda: press(4), height=1, width=7)
button4.grid(row=3, column=0)

button5 = Button(root, text=' 5 ', fg=button_color2, bg=button_color, command=lambda: press(5), height=1, width=7)
button5.grid(row=3, column=1)

button6 = Button(root, text=' 6 ', fg=button_color2, bg=button_color, command=lambda: press(6), height=1, width=7)
button6.grid(row=3, column=2)

button7 = Button(root, text=' 7 ', fg=button_color2, bg=button_color, command=lambda: press(7), height=1, width=7)
button7.grid(row=4, column=0)

button8 = Button(root, text=' 8 ', fg=button_color2, bg=button_color, command=lambda: press(8), height=1, width=7)
button8.grid(row=4, column=1)

button9 = Button(root, text=' 9 ', fg=button_color2, bg=button_color, command=lambda: press(9), height=1, width=7)
button9.grid(row=4, column=2)

plus = Button(root, text=' + ', fg=button_color2, bg=button_color, command=lambda: press("+"), height=1, width=7)
plus.grid(row=2, column=3)

minus = Button(root, text=' - ', fg=button_color2, bg=button_color, command=lambda: press("-"), height=1, width=7)
minus.grid(row=3, column=3)

multiply = Button(root, text=' * ', fg=button_color2, bg=button_color, command=lambda: press("*"), height=1, width=7)
multiply.grid(row=4, column=3)

divide = Button(root, text=' / ', fg=button_color2, bg=button_color, command=lambda: press("/"), height=1, width=7)
divide.grid(row=5, column=3)

equal = Button(root, text=' = ', fg=button_color2, bg=button_color, command=equalpress, height=1, width=7)
equal.grid(row=5, column=2)

clear = Button(root, text='Clear', fg=button_color2, bg=button_color, command=clear, height=1, width=7)
clear.grid(row=5, column=1)

Decimal= Button(root, text='.', fg=button_color2, bg=button_color, command=lambda: press('.'), height=1, width=7)
Decimal.grid(row=6, column=0)

history_display = Listbox(root,)
history_display.grid(row=8, column=0, columnspan=4, ipadx=100, pady=10)

scrollbar = Scrollbar(history_display)
scrollbar.pack(side=RIGHT, fill='both')

root.mainloop()
