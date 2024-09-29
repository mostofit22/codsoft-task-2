import tkinter as tk

def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operation = var.get()

    result = None
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero"

    label_result.config(text=f"Result: {result}")

def reset_fields():
    entry1.delete(0,tk.END)
    entry2.delete(0,tk.END)


# Create the main window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x400")
# Create labels and entry fields
label1 = tk.Label(window, text="Enter the first number:")
label1.grid(row=0, column=0)
entry1 = tk.Entry(window)
entry1.grid(row=0, column=1)

label2 = tk.Label(window, text="Enter the second number:")
label2.grid(row=1, column=0)
entry2 = tk.Entry(window)
entry2.grid(row=1, column=1)

# Create radio buttons for operation choices
var = tk.StringVar()
radio_add = tk.Radiobutton(window, text="+", variable=var, value="+")
radio_add.grid(row=2, column=0)
radio_subtract = tk.Radiobutton(window, text="-", variable=var, value="-")
radio_subtract.grid(row=2, column=1)
radio_multiply = tk.Radiobutton(window, text="*", variable=var, value="*")
radio_multiply.grid(row=3, column=0)
radio_divide = tk.Radiobutton(window, text="/", variable=var, value="/")
radio_divide.grid(row=3, column=1)

# Create a button to calculate
button_calculate = tk.Button(window, text="Calculate", command=calculate)
button_calculate.grid(row=4, columnspan=2)

reset_button=tk.Button(window,text="reset",command=reset_fields)
reset_button.grid(row=6,columnspan=2)

# Create a label to display the result
label_result = tk.Label(window, text="Result:")
label_result.grid(row=5, columnspan=2)

window.mainloop()