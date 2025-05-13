import tkinter as tk
from tkinter import font

# --- Global Variables ---
expression = "" # To store the current expression string

# --- Functions for Calculator Logic ---

def press(num_or_op):
    """
    This function is called when a number or operator button is pressed.
    It appends the pressed item to the global 'expression' string
    and updates the display.
    """
    global expression
    expression = expression + str(num_or_op)
    equation.set(expression) # Update the StringVar linked to the Entry widget

def equal_press():
    """
    This function is called when the '=' button is pressed.
    It tries to evaluate the 'expression' string and displays the result.
    Handles errors like division by zero or syntax errors.
    """
    global expression
    try:
        # eval() can be a security risk if you're evaluating untrusted input.
        # For a simple calculator, it's generally acceptable.
        # For more robust applications, consider parsing the expression manually.
        total = str(eval(expression))
        equation.set(total)
        expression = total # Store the result for further calculations
    except ZeroDivisionError:
        equation.set("Error: Div by 0")
        expression = ""
    except SyntaxError:
        equation.set("Error: Syntax")
        expression = ""
    except Exception as e:
        equation.set("Error")
        print(f"An unexpected error occurred: {e}") # Log the error to console
        expression = ""

def clear():
    """
    This function is called when the 'C' (Clear) button is pressed.
    It resets the 'expression' string and clears the display.
    """
    global expression
    expression = ""
    equation.set("")

# --- GUI Setup ---
if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    root.title("Simple Calculator")
    root.geometry("320x480") # Adjust size as needed
    root.resizable(False, False) # Make the window non-resizable
    root.configure(bg="#f0f0f0") # Light grey background

    # StringVar to hold the text in the entry field
    equation = tk.StringVar()

    # Define a nice font
    default_font = font.Font(family="Arial", size=18)
    button_font = font.Font(family="Arial", size=16, weight="bold")

    # Entry field for display
    # Make it read-only so users can only input via buttons
    display_field = tk.Entry(root, textvariable=equation, font=default_font, bd=10,
                             insertwidth=2, width=14, borderwidth=4, justify='right',
                             readonlybackground="white", state='readonly')
    display_field.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=10)

    # Frame for buttons to group them
    button_frame = tk.Frame(root, bg="#f0f0f0")
    button_frame.grid(row=1, column=0, columnspan=4, padx=5, pady=5)

    # --- Define Buttons ---
    # Button texts and their grid positions (row, column)
    # (text, row, col, columnspan, command_func, *args_for_command)
    # Using lambda to pass arguments to the press function
    buttons = [
        ('7', 0, 0, lambda: press(7)),
        ('8', 0, 1, lambda: press(8)),
        ('9', 0, 2, lambda: press(9)),
        ('/', 0, 3, lambda: press('/')),

        ('4', 1, 0, lambda: press(4)),
        ('5', 1, 1, lambda: press(5)),
        ('6', 1, 2, lambda: press(6)),
        ('*', 1, 3, lambda: press('*')),

        ('1', 2, 0, lambda: press(1)),
        ('2', 2, 1, lambda: press(2)),
        ('3', 2, 2, lambda: press(3)),
        ('-', 2, 3, lambda: press('-')),

        ('C', 3, 0, clear),
        ('0', 3, 1, lambda: press(0)),
        ('=', 3, 2, equal_press),
        ('+', 3, 3, lambda: press('+')),
    ]

    # Create and place buttons in the grid
    for (text, r, c, cmd) in buttons:
        if text in ['/', '*', '-', '+', '=']:
            bg_color = "#ff9500" # Orange for operators and equals
            fg_color = "white"
        elif text == 'C':
            bg_color = "#d4d4d2" # Light grey for Clear
            fg_color = "black"
        else:
            bg_color = "#505050" # Dark grey for numbers
            fg_color = "white"

        button = tk.Button(button_frame, text=str(text), font=button_font,
                           fg=fg_color, bg=bg_color,
                           command=cmd, height=2, width=4, relief="raised", bd=3)
        button.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

    # Configure row/column weights for button_frame so they expand
    for i in range(4): # 4 rows of buttons
        button_frame.grid_rowconfigure(i, weight=1)
    for i in range(4): # 4 columns of buttons
        button_frame.grid_columnconfigure(i, weight=1)


    # Start the GUI event loop
    root.mainloop()