from tkinter import *
from random import randint
class player:
    runs=0
    rc=0
    bat=0
    strike=0
    def plus():
        player.strike=1
        player.runs=player.runs+player.rc
class ai:
    runs=0
    rc=0
    bat=0
    strike=0
    def plus():
        ai.runs=ai.runs+ai.rc
def settarget(y):
    global turn
    global target
    target=y+1
    turn=2
    trgt=Label(window,text = 'Target = {}'.format(target), fg='blue', font=("Helvetica", 20))
    trgt.place(x=450, y=260)

def win(x):
    winner =x
    winn=Label(window,text = 'WON by {}'.format(winner), fg='green', font=("Helvetica", 20))
    winn.place(x=250, y=260)
def out(x):
    outt=Label(window,text = '{} out'.format(x), fg='red', font=("Helvetica", 20))
    outt.place(x=250, y=260)
def reset():
    global target
    global turn
    a.runs=0
    a.rc=0
    p.rc=0
    p.runs=0
    target=-1
    turn=0
target=-1
p=player
a=ai
turn=1
def check():
    if(a.rc!=p.rc):
        return True
    return False

def air():
    a.rc=randint(1,6)
    if a.bat==turn:
        if target>0:
            if check() is True:
                a.plus()
                if a.runs >= target:
                    win('AI')   
                    deleteall()
            else:
                out('AI')  
                deleteall()
        elif check() is True:
            a.plus()
        else:
            out('AI')
            settarget(a.runs)
    elif p.bat==turn:
        if check() is False:
            out('USER')
def _user(a):
    p.rc=a
    air()
    if p.bat==turn:
        if target>0:
            if check() is True:
                p.plus()
                if p.runs >= target:
                    win('USER')
                    deleteall()
            else:
                if player.strike==1:
                    deleteall()
                else:
                    player.strike=1
        elif check() is True:
            p.plus()
        else:
            out('USER')
            settarget(p.runs)
    display()
def deleteall():
    Button1.destroy()
    Button2.destroy()
    Button3.destroy()
    Button4.destroy()
    Button5.destroy()
    Button6.destroy()
    restartbutton=Button(window,text='EXIT',command=restart)
    restartbutton.place(x=100,y=200)
def restart():
    root.destroy()
    
    
def display():
    aiscorel=Label(window,text = 'AI SCORE = {}'.format(a.runs), fg='blue', font=("Helvetica", 20))
    aiscorel.place(x=450, y=10)
    aicurrent=Label(window, text=a.rc, fg='blue', font=("Helvetica", 50))
    aicurrent.place(x=450, y=100)
    aiscorel=Label(window,text = 'USER SCORE = {}'.format(p.runs), fg='red', font=("Helvetica", 20))
    aiscorel.place(x=50, y=10)
    aicurrent=Label(window, text=p.rc, fg='red', font=("Helvetica", 50))
    aicurrent.place(x=50, y=100)
    lbl=Label(window, text="Player one", fg='red', font=("Helvetica", 16))
    lbl.place(x=50, y=50)
    lbl2=Label(window, text="Player two", fg='blue', font=("Helvetica", 16))
    lbl2.place(x=450, y=50)
aitotal = 0
aic = 0
userc=0
usertotal=0
root=Tk()
window = Frame(root,height=500,width=800)
Button1=Button(window,text="1", command=lambda: _user(1))
Button1.place(x=50,y=200)
Button2=Button(window,text="2", command=lambda: _user(2))
Button2.place(x=70,y=200)
Button3=Button(window,text="3", command=lambda: _user(3))
Button3.place(x=90,y=200)
Button4=Button(window,text="4", command=lambda: _user(4))
Button4.place(x=110,y=200)
Button5=Button(window,text="5", command=lambda: _user(5))
Button5.place(x=130,y=200)
Button6=Button(window,text="6", command=lambda: _user(6))
Button6.place(x=150,y=200)
lbl=Label(window, text="Player one", fg='red', font=("Helvetica", 16))
lbl.place(x=50, y=50)
lbl2=Label(window, text="Player two", fg='blue', font=("Helvetica", 16))
lbl2.place(x=450, y=50)

uc=0
tossscreen= Frame(root,height=500,width=500)
def heads():
    global uc
    hdlble=Label(tossscreen,text="Slected : Heads")
    hdlble.place(x=200,y=100)
    tossbtn.place(x=200,y=150)
    uc=1
    hds.destroy()
    tls.destroy()
def tails():
    global uc
    tlslble=Label(tossscreen,text="Slected : Tails")
    tlslble.place(x=200,y=100)
    tossbtn.place(x=200,y=150)
    uc=2
    hds.destroy()
    tls.destroy()
def BATTING():
    a.bat=2
    p.bat=1
    play.place(x=200,y=300)

def BOWLING():
    a.bat=1
    p.bat=2
    play.place(x=200,y=300)

def toss():
    global uc
    t= randint(1,2)
    if t==1:
        tshlble=Label(tossscreen,text="Heads")
        tshlble.place(x=250,y=150)
    else :
        tstlble=Label(tossscreen,text="Tails")
        tstlble.place(x=250,y=150)
    if t==uc:
        bt=Button(tossscreen,text='BAT',command=BATTING)
        bt.place(x=200,y=250)
        bl=Button(tossscreen,text='BOWL',command=BOWLING)
        bl.place(x=250,y=250)
    else :
        c=randint(1,2)
        if c==1:
            BATTING()
            blc=Label(tossscreen,text="Ai won the toss and chose to Bowl")
            blc.place(x=100,y=200)
        else :
            BOWLING()
            btc=Label(tossscreen,text="Ai won the toss and chose to Bat")
            btc.place(x=100,y=200)
    tossbtn.destroy()
def playgame():
    window.pack()
    tossscreen.destroy()
play=Button(tossscreen,text='Play',command=playgame)
hds=Button(tossscreen,text='Heads',command=heads)
hds.place(x=200,y=100)
tls=Button(tossscreen,text='Tails',command=tails)
tls.place(x=250,y=100)
tossbtn=Button(tossscreen,text='Toss',command=toss)
root.title('HAND CRICKET')
tossscreen.pack()
root.mainloop()
