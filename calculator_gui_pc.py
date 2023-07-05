# SIMPLE CALCULATOR GUI USING TKINTER PACKAGE.

# Importing the necessary libraries.
import tkinter as tk

# Initializing the graphical interphase.
root = tk.Tk()
root.title("MyCalc")
root.geometry("400x443")


# Creating the text window where the numbers and operators are going to be displayed.
text_result = tk.Text(root, height=2, width=22, font=("Arial", 24))
text_result.grid(columnspan=5)

# A calculation string, at first it's empty.
calculation = ""


# Creating a function that displays the appropriate symbol, number or operator.
def add_to_calculation(symbol):
    # "calculation" string needs to be a global variable so that we can manipulate it inside the function.
    global calculation
    calculation += str(symbol)
    # Delete the contents of text_result window.
    text_result.delete(1.0, "end")
    # Insert the correct "calculation" string in the text_result window.
    text_result.insert(1.0, calculation)


# Creating a function that is used to compute the final result each of the operations.
def evaluate_calculation():
    # "calculation" string needs to be a global variable so that we can manipulate it inside the function.
    global calculation
    # Handling exceptions.
    # If there is no exception.
    try:
        result = str(eval(calculation))
        calculation = ""
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    # If it appears to be an exception.
    except:
        clear_field()
        text_result.insert(1.0, "Error")


# Creating a function that is used to clear the contents of the text window.
def clear_field():
    # "calculation" string needs to be a global variable so that we can manipulate it inside the function.
    global calculation
    calculation = ""
    # Delete the contents of text_result window.
    text_result.delete(1.0, "end")


# Creating a function that is used to delete the last character of the text window.
def delete_calculation():
    # "calculation" string needs to be a global variable so that we can manipulate it inside the function.
    global calculation
    calculation = calculation[:-1]
    # Delete the contents of text_result window.
    text_result.delete(1.0, "end")
    # Insert the correct "calculation" string in the text_result window.
    text_result.insert(1.0, calculation)


# Creating the appropriate buttons for our calculator, using lambda expressions.
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), height=2, width=8, font=("Arial", 14))
btn_1.grid(row=2, column=1)

btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), height=2, width=8, font=("Arial", 14))
btn_2.grid(row=2, column=2)

btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), height=2, width=8, font=("Arial", 14))
btn_3.grid(row=2, column=3)

btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), height=2, width=8, font=("Arial", 14))
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), height=2, width=8, font=("Arial", 14))
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), height=2, width=8, font=("Arial", 14))
btn_6.grid(row=3, column=3)

btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), height=2, width=8, font=("Arial", 14))
btn_7.grid(row=4, column=1)

btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), height=2, width=8, font=("Arial", 14))
btn_8.grid(row=4, column=2)

btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), height=2, width=8, font=("Arial", 14))
btn_9.grid(row=4, column=3)

btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), height=2, width=8, font=("Arial", 14))
btn_0.grid(row=5, column=2)

btn_comma = tk.Button(root, text=".", command=lambda: add_to_calculation("."), height=2, width=8, font=("Arial", 14))
btn_comma.grid(row=1, column=3)

btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), height=2, width=8, font=("Arial", 14))
btn_plus.grid(row=2, column=4)

btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), height=2, width=8, font=("Arial", 14))
btn_minus.grid(row=3, column=4)

btn_mult = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), height=2, width=8, font=("Arial", 14))
btn_mult.grid(row=4, column=4)

btn_div = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), height=2, width=8, font=("Arial", 14))
btn_div.grid(row=5, column=4)

btn_open = tk.Button(root, text="(", command=lambda: add_to_calculation(")"), height=2, width=8, font=("Arial", 14))
btn_open.grid(row=5, column=1)

btn_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), height=2, width=8, font=("Arial", 14))
btn_close.grid(row=5, column=3)

btn_equals = tk.Button(root, text="=", command=evaluate_calculation, height=2, width=17, font=("Arial", 14))
btn_equals.grid(row=6, column=3, columnspan=2)

btn_clear = tk.Button(root, text="C", command=clear_field, height=2, width=17, font=("Arial", 14))
btn_clear.grid(row=6, column=1, columnspan=2)

btn_del = tk.Button(root, text="Del", command=delete_calculation, height=2, width=8, font=("Arial", 14))
btn_del.grid(row=1, column=4)

# Run the tkinter event loop.
root.mainloop()
