from tkinter import *
from tkinter import messagebox

try:
    import httplib
except:
    import http.client as httplib

def check_internet():
    conn = httplib.HTTPSConnection("8.8.8.8", timeout=5)
    try:
        conn.request("HEAD","/")
        return True
    except Exception:
        return False

def powiadomienie():
    if check_internet() == False:
        messagebox.showwarning(title='E smalec',message="Nie ma neta :)")
    else:
        messagebox.showinfo(title='E smalec', message="Jest net :)")

window=Tk()

window.title("Program do sprawdzania neta")

window.geometry("600x400+500+200")
window.config(background="#6db5fc")

icon = PhotoImage(file='i.png')
funnyComputer=PhotoImage(file='stolen.png')
window.iconphoto(True, icon)

labelImage=Label(window,image=funnyComputer,bg="#6db5fc")
labelImage.pack()
guzik=Button(window,text="Sprawdz neta", command=powiadomienie, justify="center", font=("Comic Sans", 16))
guzik.pack()

window.mainloop()