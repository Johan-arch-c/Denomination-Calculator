import tkinter as tk

def check_strength():
    password = entry.get()
    length = len(password)

    if length == 0:
        result_label.config(text="Please enter a password", fg="black")
    elif length < 6:
        result_label.config(text="Weak Password", fg="red")
    elif length < 10:
        result_label.config(text="Medium Password", fg="orange")
    else:
        result_label.config(text="Strong Password", fg="green")

window = tk.Tk()
window.title("Password Strength Checker")
window.geometry("350x200")

title_label = tk.Label(window, text="Password Strength Checker App", font=("Arial", 14))
title_label.pack(pady=10)

entry_label = tk.Label(window, text="Enter Password:")
entry_label.pack()

entry = tk.Entry(window, show="*", width=30)
entry.pack(pady=5)

check_button = tk.Button(window, text="Check Strength", command=check_strength)
check_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack()

window.mainloop()
