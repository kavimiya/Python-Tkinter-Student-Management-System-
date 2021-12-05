import tkinter as tk
from tkinter import Widget, ttk

win = tk.Tk()
win.geometry("1350x700+0+0")
win.title("Student Management System")

#Background Color
win.config(bg="lightgray")

#Top Menu 

title_label = tk.Label(
  win, 
  text="Student Management System",
  font=("Arial", 20, "bold"),
  padx=15,
  pady=15, 
  border=0, 
  relief=tk.GROOVE, 
  bg="teal",
  foreground="white"
)
title_label.pack(side=tk.TOP, fill=tk.X)

#Left Menu

detail_frame = tk.LabelFrame(
  win, text="Student Records", 
  font=("Arial", 14), 
  bg="lightgray", 
  foreground="black",
  relief=tk.GROOVE
)
detail_frame.place(x=40, y=90, width=420, height=570)


#Data Frame

data_frame = tk.Frame(
  win,  
  bg="teal",
  relief=tk.GROOVE
)
data_frame.place(x=490, y=98, width=830, height=565)

#Variables
id = tk.StringVar()
name = tk.StringVar()
gender = tk.StringVar()
age = tk.StringVar()
enroll_date = tk.StringVar()
midterm = tk.StringVar()
final = tk.StringVar()
gpa = tk.StringVar()


#Label with Entry

id_lab = tk.Label(
  detail_frame, 
  text="ID:", 
  font=("Arial", 16), 
  bg="lightgray", 
  foreground="black"
)
id_lab.place(x=20, y=15)

#entry
id_ent = tk.Entry(
  detail_frame, 
  bd=1,
  font=("arial", 16), 
  bg="white", 
  foreground="black"
)
id_ent.place(x=110, y=17, width=250, height=30)

#2
name_lab = tk.Label(
  detail_frame, 
  text="Name:", 
  font=("Arial", 16), 
  bg="lightgray", 
  foreground="black"
)
name_lab.place(x=20, y=65)

#entry
name_ent = tk.Entry(
  detail_frame, 
  bd=1,
  font=("arial", 16), 
  bg="white", 
  foreground="black"
)
name_ent.place(x=110, y=65, width=250, height=30)

#3
gen_lab = tk.Label(
  detail_frame, 
  text="Gender:", 
  font=("Arial", 16), 
  bg="lightgray", 
  foreground="black"
)
gen_lab.place(x=20, y=113)

#entry
gen_ent = ttk.Combobox(
  detail_frame, 
  font=("arial", 16), 
)
gen_ent["values"] = ("Male", "Female", "others")
gen_ent.place(x=110, y=113, width=250, height=30)

#4
age_lab = tk.Label(
  detail_frame, 
  text="Age:", 
  font=("Arial", 16), 
  bg="lightgray", 
  foreground="black"
)
age_lab.place(x=20, y=161)

#entry
age_ent = tk.Entry(
  detail_frame, 
  bd=1,
  font=("arial", 16), 
  bg="white", 
  foreground="black"
)
age_ent.place(x=110, y=161, width=250, height=30)

#5
ent_lab = tk.Label(
  detail_frame, 
  text="En-date:", 
  font=("Arial", 16), 
  bg="lightgray", 
  foreground="black"
)
ent_lab.place(x=20, y=209)

#entry
ent_ent = tk.Entry(
  detail_frame, 
  bd=1,
  font=("arial", 16), 
  bg="white", 
  foreground="black"
)
ent_ent.place(x=110, y=209, width=250, height=30)

#6
mid_lab = tk.Label(
  detail_frame, 
  text="Midterm:", 
  font=("Arial", 16), 
  bg="lightgray", 
  foreground="black"
)
mid_lab.place(x=20, y=257)

#entry
mid_ent = tk.Entry(
  detail_frame, 
  bd=1,
  font=("arial", 16), 
  bg="white", 
  foreground="black"
)
mid_ent.place(x=110, y=257, width=250, height=30)

#7
fin_lab = tk.Label(
  detail_frame, 
  text="Final:", 
  font=("Arial", 16), 
  bg="lightgray", 
  foreground="black"
)
fin_lab.place(x=20, y=305)

#entry
fin_ent = tk.Entry(
  detail_frame, 
  bd=1,
  font=("arial", 16), 
  bg="white", 
  foreground="black"
)
fin_ent.place(x=110, y=305, width=250, height=30)

#8
gpa_lab = tk.Label(
  detail_frame, 
  text="GPA:", 
  font=("Arial", 16), 
  bg="lightgray", 
  foreground="black"
)
gpa_lab.place(x=20, y=353)

#entry
gpa_ent = tk.Entry(
  detail_frame, 
  bd=1,
  font=("arial", 16), 
  bg="white", 
  foreground="black"
)
gpa_ent.place(x=110, y=353, width=250, height=30)

#Buttons

btn_frame = tk.Frame(
  detail_frame,
  bg="lightgray",
  bd=0,
  relief=tk.GROOVE
)
btn_frame.place(x=40, y=400, width=310, height=130)

#Add Button
add_btn = tk.Button(
  btn_frame,
  bg="teal",
  foreground="white",
  text="Add",
  bd=2,
  font=("Arial", 13), width=15
)
add_btn.grid(row=0, column=0, padx=2, pady=2)

#Update Button
update_btn = tk.Button(
  btn_frame,
  bg="teal",
  foreground="white",
  text="Update",
  bd=2,
  font=("Arial", 13), width=15
)
update_btn.grid(row=0, column=1, padx=2, pady=2)

#Print Button
print_btn = tk.Button(
  btn_frame,
  bg="teal",
  foreground="white",
  text="Print",
  bd=2,
  font=("Arial", 13), width=15
)
print_btn.grid(row=1, column=0, padx=2, pady=2)

#Calculate Button
cal_btn = tk.Button(
  btn_frame,
  bg="teal",
  foreground="white",
  text="Calculate",
  bd=2,
  font=("Arial", 13), width=15
)
cal_btn.grid(row=1, column=1, padx=2, pady=2)

#Save Button
save_btn = tk.Button(
  btn_frame,
  bg="teal",
  foreground="white",
  text="Save",
  bd=2,
  font=("Arial", 13), width=15
)
save_btn.grid(row=2, column=0, padx=2, pady=2)

#Delete Button
delete_btn = tk.Button(
  btn_frame,
  bg="teal",
  foreground="white",
  text="Delete",
  bd=2,
  font=("Arial", 13), width=15
)
delete_btn.grid(row=2, column=1, padx=2, pady=2)

#Database frame 

main_frame = tk.Frame(
  data_frame,
  bg="teal",
  bd=2,
  relief=tk.GROOVE
)
main_frame.pack(fill=tk.BOTH, expand=True)

y_scroll = tk.Scrollbar(main_frame, orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL)

#Treeview database

student_table = ttk.Treeview(main_frame, columns=(
  "ID", "Name", "Gender", "Age", "Enroll date", "Midterm", "Final", "GPA"
), yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)

y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

student_table.heading("ID", text="ID")
student_table.heading("Name", text="Name")
student_table.heading("Gender", text="Gender")
student_table.heading("Age", text="Age")
student_table.heading("Enroll date", text="Enroll date")
student_table.heading("Midterm", text="Midterm")
student_table.heading("Final", text="Final")
student_table.heading("GPA", text="GPA")

student_table["show"] = "headings"

student_table.column("ID", width=100)
student_table.column("Name", width=100)
student_table.column("Gender", width=100)
student_table.column("Age", width=100)
student_table.column("Enroll date", width=100)
student_table.column("Midterm", width=100)
student_table.column("Final", width=100)
student_table.column("GPA",  width=100)


student_table.pack(fill=tk.BOTH, expand=True)






win.mainloop()