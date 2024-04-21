from tkinter import *

PINK = "#e2979c"
CYAN= "cyan"

BLUE="#001B79"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer =None
count=0
pause=False




def reset_timer():
    global reps, count, text_mark,pause
    text_mark=""
    pause=False
    reps=0
    count=0
    window.after_cancel(timer)
    action.config(text="Timer",fg=YELLOW)
    canvas.itemconfig(time_text,text="00:00")
    checkmark.config(text="")
    



def pause_funct():
    global pause
    pause=not pause 
    return button_clicked.set(pause)


def start_timer():
    global reps, count, pause 
    reps+=1
    
    work_sec=WORK_MIN*60
    short_b=SHORT_BREAK_MIN*60
    long_break=LONG_BREAK_MIN*60
    
    if reps==8:
        count=long_break
        action.config(text="Long break",fg=YELLOW)
        
    elif reps%2 ==0  :
        count=short_b
        action.config(text="Short break",fg=PINK)
         
    else:
        count=work_sec
        action.config(text="Work hard",fg=CYAN)
        
    
    
        
    count_down()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down():
    global count,text_mark,pause,timer
    
    minute=int(count/60)
    sec= count%60
    if minute < 10 and sec<10:
        canvas.itemconfig(time_text,text=f"0{minute}:0{sec}")
        
    elif minute<10:
        canvas.itemconfig(time_text,text=f"0{minute}:{sec}")
    
    elif sec<10:
        canvas.itemconfig(time_text,text=f"{minute}:0{sec}")
    else:
        canvas.itemconfig(time_text,text=f"{minute}:{sec}")
    
    if count>0:
        if button_clicked.get():
            count-=1
            timer=window.after(1000,count_down)
            count+=1
        else:
            count-=1
            timer=window.after(1000,count_down)
        
    else :
        start_timer()
        if reps%2==0:
            text_mark+="✓"
            checkmark.config(text=text_mark)
    






window=Tk()
window.title("Pomodora counter")

window.config(background=BLUE,padx=100,pady=50)

canvas=Canvas(width=200,height=224,background=BLUE)
pomodoro_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=pomodoro_img)
canvas.config(highlightthickness=0)
time_text=canvas.create_text(108,130,text="00:00",font=(FONT_NAME,35,"bold"),fill="white")
canvas.grid(column=1,row=1)

#title label

action=Label(text="Timer", font=(FONT_NAME,25,"bold"),fg=YELLOW,background=BLUE)
action.grid(column=1,row=0)


#Start button

start_b=Button(text="Start",activebackground="green",command=start_timer)
start_b.config(width=10,highlightthickness=0)
start_b.grid(column=0,row=2)

#pause button
button_clicked = BooleanVar()
pause_button=Button(text="Pause",width=10,highlightthickness=0,command=pause_funct)
pause_button.grid(column=1,row=2)

#reset button

reset_b=Button(text="Reset",activebackground="red",command=reset_timer)
reset_b.config(width=10,highlightthickness=0)
reset_b.grid(column=2,row=2)

#check label
text_mark=""
checkmark=Label(text="",fg=YELLOW,bg=BLUE,font=(FONT_NAME,20,"bold"))
checkmark.grid(column=1,row=3)




window.mainloop()