import tkinter as tk
from tkinter import messagebox

def analyze_behavior():
    try:
        social = int(social_var.get())
        planning = int(planning_var.get())
        stress = int(stress_var.get())
        decisions = int(decision_var.get())
    except ValueError:
        messagebox.showerror("Error", "Please answer all questions.")
        return

    result = []

    if social >= 4:
        result.append("You are outgoing and enjoy being around people.")
    else:
        result.append("You are more reserved and prefer quiet or smaller settings.")

    if planning >= 4:
        result.append("You are organized and like planning ahead.")
    else:
        result.append("You are more spontaneous and flexible.")

    if stress >= 4:
        result.append("You stay calm and handle pressure well.")
    else:
        result.append("You may feel stress easily and need time to recharge.")

    if decisions >= 4:
        result.append("You make decisions confidently and quickly.")
    else:
        result.append("You prefer to think carefully before making decisions.")

    final_result = "\n".join(result)
    messagebox.showinfo("Your Behavior Report", final_result)

root = tk.Tk()
root.title("Behavior Checker App")
root.geometry("500x420")
root.config(bg="#f4f4f4")

title = tk.Label(root, text="Behavior Checker", font=("Arial", 18, "bold"), bg="#f4f4f4")
title.pack(pady=10)

subtitle = tk.Label(
    root,
    text="Answer each question from 1 to 5\n1 = Low / 5 = High",
    font=("Arial", 11),
    bg="#f4f4f4"
)
subtitle.pack(pady=5)

frame = tk.Frame(root, bg="#f4f4f4")
frame.pack(pady=10)

questions = [
    "How social are you?",
    "How much do you like planning?",
    "How well do you handle stress?",
    "How confident are you in decisions?"
]

social_var = tk.StringVar()
planning_var = tk.StringVar()
stress_var = tk.StringVar()
decision_var = tk.StringVar()

vars_list = [social_var, planning_var, stress_var, decision_var]

for i, question in enumerate(questions):
    tk.Label(frame, text=question, font=("Arial", 11), bg="#f4f4f4", anchor="w").grid(row=i, column=0, padx=10, pady=10, sticky="w")
    tk.Entry(frame, textvariable=vars_list[i], width=10).grid(row=i, column=1, padx=10, pady=10)

btn = tk.Button(root, text="Check My Behavior", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=analyze_behavior)
btn.pack(pady=20)

root.mainloop()
