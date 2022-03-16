from tkinter import*

root=Tk()
root.title("REGISTRATION FORM")
root.geometry("500x500") #width x height

label_0=Label(root, text="Registration Form", width=20, font=("bold",20), fg='#0000FF')
label_0.place(x=80, y=50)

label_1=Label(root, text="Full Name", width=20, font=("bold",15), fg='red')
label_1.place(x=80, y=130)

entry_1=Entry(root, bg='yellow', fg='red')
entry_1.place(x=240, y=130)

label_2=Label(root, text="Email", width=20, font=("bold",15), fg='red')
label_2.place(x=68, y=180)

entry_2=Entry(root, bg='aqua', fg='blue')
entry_2.place(x=240, y=180)

label_3=Label(root, text='Gender', width=20, font=("bold", 15), fg='red')
label_3.place(x=70, y=230)

var=IntVar()
Radiobutton(root, text="Male", padx=5, variable=var, value=1).place(x=235, y=230)
Radiobutton(root, text="Female", padx=20, variable=var, value=2).place(x=300, y=230)



root.mainloop()