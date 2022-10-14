from tkinter import *
window=Tk()

# add widgets here

window.title('Intrest Calculator')
window.geometry("380x400")
window.configure(bg='lightcyan')

#function for button
   
def calculate_intrest():
    p=float(principal_label.get())
    r=float(rate_label.get())
    t=float(time_label.get())
    i=(p*r*t)/100
    intrest=round(i,2)
    
    result_label.destroy()

    msg=""
    
    
    
    output_message=Label(result_frame,text=name_label+", your intrest is"+str(intrest)+" and "+msg, bg = "lightcyan", font=("Calibri", 12), width=42)
    output_message.place(x=20,y=40)
    output_message.pack()

app_label=Label(window, text="BMI CALCULATOR", fg = "black", bg = "lightcyan", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

name_label=Label(window, text="Your Name", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
name_label.place(x=20, y=90)

username=Entry(window, text="", bd=2, width=22)
username.place(x=150, y=92)

principal_label=Label(window, text="Enter pricipal", fg = "black", bg = "lightcyan", font=("Calibri", 12))
principal_label.place(x=20, y=140)

principal_entry=Entry(window, text="", bd=2, width=15)
principal_entry.place(x=150, y=142)

rate_label=Label(window, text="Enter rate", fg = "black", bg = "lightcyan", font=("Calibri", 12))
rate_label.place(x=20, y=185)

rate_entry=Entry(window, text="", bd=2, width=15)
rate_entry.place(x=150, y=187)

time_label=Label(window, text="Enter time", fg = "black", bg = "lightcyan", font=("Calibri", 12))
time_label.place(x=20, y=185)

time_entry=Entry(window, text="", bd=2, width=15)
time_entry.place(x=150, y=187)

calculate_button=Button(window,text="CALCULATE",fg = "black", bg = "cyan",bd=4,command=calculate_intrest)
calculate_button.place(x=20,y=250)

result_frame = LabelFrame(window,text="Result", bg = "lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()


window.mainloop()
