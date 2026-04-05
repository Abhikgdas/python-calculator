import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Abhik's Calculator")
root.geometry("320x450")
root.configure(bg="#1e1e1e")

# Display
entry = tk.Entry(root, width=16, font=("Arial", 24), bd=0, bg="#252525", fg="white", justify="right")
entry.pack(pady=20, padx=10, ipady=10)

# Functions
def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Button style
btn_bg = "#333333"
btn_fg = "white"
btn_active = "#ff004f"

# Button layout
buttons = [
    ["7","8","9","/"],
    ["4","5","6","*"],
    ["1","2","3","-"],
    ["0",".","=","+"]
]

# Create buttons
for row in buttons:
    frame = tk.Frame(root, bg="#1e1e1e")
    frame.pack(expand=True, fill="both")

    for btn in row:
        if btn == "=":
            action = calculate
        else:
            action = lambda x=btn: click(x)

        tk.Button(frame, text=btn, font=("Arial", 16), bg=btn_bg, fg=btn_fg,
                  activebackground=btn_active, activeforeground="white",
                  bd=0, command=action).pack(side="left", expand=True, fill="both", padx=5, pady=5)

# Clear button
tk.Button(root, text="C", font=("Arial", 16), bg="#ff004f", fg="white",
          bd=0, command=clear).pack(fill="both", padx=10, pady=10)

root.mainloop()