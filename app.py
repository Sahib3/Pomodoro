from tkinter import *
from PIL import ImageTk, Image
import time
from playsound import playsound

window = Tk()
window.title("Animodoro")
window.config(padx=100,pady=50)


timer_label = Label(text='Animodoro Timer',font=("Arial",15))
timer_label.grid(column=1,row=0)

canvas = Canvas(height=300,width=250)
back_img = ImageTk.PhotoImage(Image.open("killua.jpg"))
canvas.create_image(100,100,image=back_img)
timer_text = canvas.create_text(150,250,font=("Arial",15))
canvas.grid(column=1,row=1)


Start = Button(text="Start",font=("Arial",15),command=lambda:timer()).place(x=50,y=340)
Break = Button(text="Break",font=("Arial",15),command=lambda:Break()).place(x=120,y=340)


def timer():
    total_time = 1 * 60
    
    while total_time:
        mins = total_time // 60
        secs = total_time % 60
        output = '{:02d}:{:02d}'.format(mins,secs)
        print(" ",output, end="\r")
        time.sleep(1)
        total_time -=1
    print("Break time ")
    playsound('alarm.mp3')
    
def Break():
    total_time = 1 * 60
    
    while total_time:
        mins = total_time // 60
        secs = total_time % 60
        output = '{:02d}:{:02d}'.format(mins,secs)
        print(" ",output, end="\r")
        time.sleep(1)
        total_time -=1
    print("Work time ")
    playsound('alarm.mp3')
    

    

    

window.mainloop()

        




