import tkinter as tk
from tkinter import filedialog

import skin_randomizer

window = tk.Tk()
window.title("osu! skin randomizer")
window.resizable(False, False)

directory_path = tk.StringVar()
info_text = tk.StringVar()
hit_checkbox_var = tk.BooleanVar(value=True)
score_checkbox_var = tk.BooleanVar(value=True)
judgement_checkbox_var = tk.BooleanVar(value=True)
follow_checkbox_var = tk.BooleanVar(value=True)
last_job = ""


def randomize():
    global last_job
    if last_job != "":
        window.after_cancel(last_job)
        info_text.set("")
    try:
        skin_randomizer.randomize(directory_path.get(), not hit_checkbox_var.get(),
                                  not score_checkbox_var.get(),
                                  not judgement_checkbox_var.get(),
                                  not follow_checkbox_var.get())
        info_text.set("Successfully created random skin!")
    except Exception as e:
        info_text.set(e)
    last_job = window.after(2000, info_text.set, "")


def browse_directory():
    global directory_path
    directory_path.set(filedialog.askdirectory())


directory_path_instructions = tk.Label(window, text="Location of !osu skins directory:")
directory_path_button = tk.Button(window, text="Browse...", command=browse_directory)
directory_path_entry = tk.Entry(window, textvariable=directory_path, width=30)
same_hit_numbers_checkbox = tk.Checkbutton(window, text="Use hit-numbers from same skin", variable=hit_checkbox_var)
same_score_numbers_checkbox = tk.Checkbutton(window, text="Use score-numbers from same skin", variable=score_checkbox_var)
same_judgement_checkbox = tk.Checkbutton(window, text="Use 300s, 100s, and 50s from same skin", variable=judgement_checkbox_var)
same_follow_checkbox = tk.Checkbutton(window, text="Use follow points from same skin", variable=follow_checkbox_var)
randomize_button = tk.Button(window, text="Create randomized skin", command=randomize)
info_label = tk.Label(window, textvariable=info_text)

directory_path_instructions.grid(sticky="W", columnspan=2)
directory_path_button.grid(sticky="W", row=1, column=1)
directory_path_entry.grid(sticky="W", row=1, column=0)
same_hit_numbers_checkbox.grid(sticky="W", columnspan=2)
same_score_numbers_checkbox.grid(sticky="W", columnspan=2)
same_judgement_checkbox.grid(sticky="W", columnspan=2)
same_follow_checkbox.grid(sticky="W", columnspan=2)
randomize_button.grid(columnspan=2)
info_label.grid(sticky="W", columnspan=2)

window.mainloop()
