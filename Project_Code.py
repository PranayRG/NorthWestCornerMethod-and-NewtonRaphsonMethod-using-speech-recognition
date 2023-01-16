from tkinter.filedialog import *
import tkinter as tk  # pip install tkinter #
import PyPDF2  # for pdf work
import pyttsx3  # pip install pyttsx3  - text to speech library
import speech_recognition as sr  # pip install SpeechRecognition
import datetime  # pip install DateTime
import os  # pip install os-win
import cv2  # pip install opencv-python    - to open camera

import webbrowser  # pip install pycopy-webbrowser  #
import pytz  # python time zone # pip install pytz
import pyautogui  # for screenshot and for controlling system volume

import datetime

from tkinter import *
from tkinter import messagebox  # including messagebox
import os
from sympy import *


# NORTH WEST CORNER METHOD

def method():
    north = Tk()
    north.geometry("800x300")
    north.title("North-West Corner Method")
    supply = []
    demand = []
    cost = []


    def answer(l):
        
        cost2 = [] 

        entry_list1 = ''  # for cost
        entry_list2 = ''  # for supply
        entry_list3 = ''  # for demand

        for entries in supply:
            entry_list2 = entry_list2 + ',' + entries.get()

        for entries in cost:
            entry_list1 = entry_list1 + ',' + entries.get()

        for entries in demand:
            entry_list3 = entry_list3 + ',' + entries.get()

        # For supply list

        x2 = entry_list2.split(",")
        x2.pop(0)
        res2 = [eval(i) for i in x2]

        # For demand list

        x3 = entry_list3.split(",")
        x3.pop(0)
        res3 = [eval(i) for i in x3]

        # For cost list

        x1 = entry_list1.split(",")
        x1.pop(0)
        res1 = [eval(i) for i in x1]

        d = 0

        # print(cost2)
        while res1 != []:
            cost2.append(res1[:c1])
            res1 = res1[c1:]

        p = 0
        q = 0
        sum = 0
        while (p < r1 or q < c1):
            if res2[p] < res3[q]:
                sum += res2[p] * cost2[p][q]
                res3[q] -= res2[p]
                p += 1
            elif res2[p] > res3[q]:
                sum += res3[q] * cost2[p][q]
                res2[p] -= res3[q]
                q += 1
            elif res2[p] == res3[q]:
                sum += res3[q] * cost2[p][q]
                res2[p] -= res3[q]
                q += 1
                p += 1

        l.config(text=sum)


    def matrix(r, c):
       
        global e1
        global e2
        global e3
        global r1
        global c1

        r1 = int(r)
        c1 = int(c)
        f2 = Frame(north,bg="#FCF3CF")
        f2.place( x=0, y=0, width=800, height=300)
        b2 = Button(f2, text="Back", command=home)
        b2.grid(row=0, column=0)

        for i in range(0, r1 + 1):
            for j in range(0, c1 + 1):
                if j == c1:
                    l = Label(f2, text="Supply", font=("Bahnschrift SemiBold",16), fg='blue',bg="#FCF3CF")
                    l.grid(row=1, column=j + 2, padx=3)
                elif i == r1:
                    l = Label(f2, text="Demand", font=("Bahnschrift SemiBold",16), fg='blue',bg="#FCF3CF")
                    l.grid(row=i + 2, column=1, padx=3)
                else:
                    l = Label(f2, text='O' + str(i + 1), font=("Arial Rounded MT Bold",15), fg='blue',bg="#FCF3CF")
                    l.grid(row=i + 2, column=1, padx=3)

                    l = Label(f2, text='D' + str(j + 1), font=("Arial Rounded MT Bold",15), fg='blue',bg="#FCF3CF")
                    l.grid(row=1, column=j + 2, padx=3)

        for i in range(0, r1):
            for j in range(0, c1):
                e1 = Entry(f2, width=5, font=5, bg='#D2B4DE')
                e1.grid(row=i + 2, column=j + 2, padx=3, pady=3)
                cost.append(e1)
        
        for i in range(2, r1 + 2):
            e2 = Entry(f2, width=5, font=5, bg='#D6EAF8')
            e2.grid(row=i, column=c1 + 2, padx=3, pady=3)
            
            supply.append(e2)

        for j in range(2, c1 + 2):
            e3 = Entry(f2, width=5, font=5, bg='#D5F5E3')
            e3.grid(row=r1 + 2, column=j, padx=3, pady=3)
            demand.append(e3)

        label2 = Label(f2, text='Answer here',bg="#FCF3CF")
        label2.grid(row=r1 + 2, column=c1 + 3)

        for i in range(r1 + 2, r1 + 3):
            b3 = Button(f2, text="Answer", command=lambda: answer(label2),font=("Cascadia Code SemiBold",10),activebackground="white",activeforeground="red")
            b3.grid(row=i, column=c1 + 2)


    def home():
        f1 = Frame(north,bg="light blue")
        f1.place(x=0, y=0, width=800, height=300)
        # Labels for number of rows and column
        Label(f1, text="North West Corner Method",bg="light blue",font=("Bahnschrift SemiBold", 18)).grid(row=1, column=1, padx=10)
        Label(f1, text="  Number of rows:  ",bg="light blue",font=("Segoe UI Variable Display Semib",13)).grid(row=2, column=0, padx=20, pady=20)
        Label(f1, text="Number of column:",bg="light blue",font=("Segoe UI Variable Display Semib",13)).grid(row=3, column=0)

        # Text Input for row and column
        var1 = IntVar()
        var2 = IntVar()
        rows = Entry(f1, width=20, borderwidth=5, textvariable=var1,font=("Calibri 13 bold"))
        rows.grid(row=2, column=1)
        columns = Entry(f1, width=20, borderwidth=5, textvariable=var2,font=("Calibri 13 bold"))
        columns.grid(row=3, column=1)

        # Button
        Button(f1, text="Generate",font=("Cascadia Code SemiBold",10),activebackground="white",activeforeground="red", command=lambda: matrix(rows.get(), columns.get())).grid(row=6, column=1, pady=20)


    home()

    north.mainloop()


# NEWTON RAPHSON METHOD

def newton():
    
        # geometry
    root = Tk()
    root.title("Newton Raphson method")
    root.geometry("1250x550")
    root.config(bg="#EBDEF0")

    # title inside window
    a = Label(root,text="Newton Raphson method:",font="Georgia 15 underline bold",bg="#EBDEF0")
    a.place(x=350,y=10)

    # statements for taking inputs
    eqn = Label(root, text="Enter equation with variable x : ", font="Georgia 15",bg="#EBDEF0") # use * for multiplication and ** for power
    x_0 = Label(root, text="Enter the initial guess (real no.): ", font="Georgia 15",bg="#EBDEF0") #it can be any number according to the graph of eqn, mostly it is one
    eqn.place(x=80, y=60)
    x_0.place(x=80, y=130)

    # taking input as string
    eqn1_input = StringVar()
    x0_input = StringVar()
    eqn_entry = Entry(root,textvariable=eqn1_input, font=("Segoe UI", 20), width=20,bg="#F2D7D5")
    x0_entry = Entry(root,textvariable=x0_input, font=("Segoe UI", 20), width=20,bg="#F2D7D5")          
    eqn_entry.place(x=500, y=60)
    x0_entry.place(x=500, y=130)

    def calculator():
        try:
            x0 = float(x0_entry.get())
            eqn = eqn_entry.get()  # inputs
            
            x = Symbol('x')
        except:
            pass
        while True:
            try:
                exp = eval(eqn)  # execute legal expression
            except:
                messagebox.showerror('Error', 'Please enter the correct entry')
                break
            else:
                break

        try:
            der = diff(exp, x)# differentiation
            x1 = 1
            while True:
                if der.subs(x, x0) <= 0.1:
                    # substituting x by x0
                    x0 += 1
                else:
                    break
            err = (exp/der).subs(x, x0)
            for i in range(10):
                x1 = x0 - err
                x0 = x1
                x0 = round(x1, 3)  # it will round it up to 3 decimal places
                x1 = round(x1, 3)
                err = (exp/der).subs(x, x0)
            Label(root,text=f'Root for x is {round(x1, 3)}', font="arial 30 bold", bg="#EBDEF0").place(x=220,y=250)  # output on window
        except:
            # print("Enter correct equation")
            pass


    # calculate button
    Button(root,text="Calculate",font="Georgia 15 bold",command=calculator).place(x=200,y=190)

    root.mainloop()


# For taking various queries in jarvis
def jarvis():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # print(voices[1].id)
    engine.setProperty('voices', voices[0].id)
    engine.setProperty('rate', 200)

    # text to speech
    def speak(audio):
        engine.say(audio)
        print(audio)
        engine.runAndWait()

    # voice to text
    def takecommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening.......")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing.....")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")

        except Exception as e:
            speak("Pardon Sir")
            return "none"
        return query

    # to wish
    def wish():
        hour = int(datetime.datetime.now().hour)
        if 0 <= hour <= 12:
            speak("Good Morning Sir")
        elif 12 < hour < 18:
            speak("Good Afternoon Sir")
        else:
            speak("Good Evening Sir")

    def date():
        t_date = datetime.datetime.now(tz=pytz.timezone('Asia/kolkata'))
        speak("Today's date is.")
        speak(t_date.strftime("%d %B, of %Y"))

    def time():
        t_now = datetime.datetime.now().strftime('%H:%M:%S')
        speak("Sir the running time is")
        speak(t_now)

        speak("Please tell me how can I help you")

    root = tk.Tk()
    window = tk.Canvas(root, width=200, height=200)
    window.pack()

    def screenshot():
        img = pyautogui.screenshot()

        speak("From which name do you want to save file")
        file_path = asksaveasfilename()

        img.save(file_path + " _screenshot.png")

        window.create_window(100, 100)
        speak("I have taken the screenshot.")


    def pdf():
        file = open("transform.pdf", "rb")
        reader = PyPDF2.PdfFileReader(file)  # pip install PyPDF2
        pages = reader.numPages  # for counting number of pages in pdf
        speak(f"Total number of pages in the pdf are {pages}")
        speak("Sir please enter the page number which you want to read")
        pg = input("Enter page number = ")
        pg=int(pg)
        pg=pg-1
        page1 = reader.getPage(pg)
        pdfData = page1.extractText()
        speak(pdfData)

    if __name__ == '__main__':
        wish()
        time()
        while True:
            if 1:
                query = takecommand().lower()

                # logic building for tasks

                if "open notepad" in query:
                    npath = "C:\\Windows\\SysWOW64\\notepad.exe"
                    os.startfile(npath)

                elif "open command prompt" in query:
                    os.system("start cmd")

                elif "open camera" in query:
                    cap = cv2.VideoCapture(0)
                    while True:
                        ret, img = cap.read()
                        cv2.imshow('webcam', img)
                        k = cv2.waitKey(50)
                        if k == 27:
                            break
                    cap.release()
                    cv2.destroyAllWindows()

                elif "date" in query:
                    date()
   
                elif "search youtube" in query:
                    speak("sir, what should i search on youtube")
                    cm = takecommand().lower()
                    webbrowser.open(f"https://www.youtube.com/results?search_query={cm}")


                elif "screenshot" in query:
                    screenshot()

                elif "open google" in query:
                    speak("sir, what should i search on google")
                    cm = takecommand().lower()
                    webbrowser.open(f"{cm}")

                elif "open my whatsapp" in query:
                    webbrowser.open("https://web.whatsapp.com/")

                elif "hello" in query:
                    speak("Hello sir . How are you.")

                elif "how are you jarvis" in query:
                    speak("I'm fine sir. ")   

                elif "volume up" in query:
                    pyautogui.press("volumeup")
                elif "volume down" in query:
                    pyautogui.press("volumedown")
                elif "volume mute" in query:
                    pyautogui.press("volumemute")

                elif "read pdf" in query:
                    pdf()

                elif "north west corner method" in query:
                    method()
                
                elif "newton raphson method" in query:
                    newton()

                elif "exit" in query:
                    quit()


def delete2():
    screen3.destroy()
    screen2.destroy()
    screen.destroy()


def delete3():
    screen4.destroy()


def delete4():
    screen5.destroy()


def login_sucess():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("400x250")
    Label(screen3, text="Login Sucess").pack()
    Button(screen3, text="OK", height='2', width="15").pack()
    screen3.destroy()
    screen2.destroy()
    screen.destroy()
    jarvis()


def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Success")
    screen4.geometry("500x350")
    Label(screen4, text="Password or Email Error").pack()
    Button(screen4, text="OK", command=delete3).pack()


def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Success")
    screen5.geometry("500x350")
    Label(screen5, text="User Not Found").pack()
    Button(screen5, text="OK", command=delete4).pack()


def des2():
    screen2.destroy()
    screen1.destroy()


def success():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Successfully Register")
    screen2.geometry("500x350")
    Label(screen2, text="Registration Successful", fg="green", font=("calibri", 11)).pack()
    Label(screen1, text="").pack()
    Button(screen2, text="ok", bg="lightgreen", height="2", width="20", command=des2).pack()


def register_user():
    print("working")

    email_info = email.get()
    password_info = password.get()

    file = open("Details.txt", "w")
    file.write(email_info + "\n")
    file.write(password_info)
    file.close()

    email_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="Registration Success", fg="green", font=("calibri", 11), command=success()).pack()


def login_verify():
    email1 = email_verify.get()
    password1 = password_verify.get()
    email_entry1.delete(0, END)
    password_entry1.delete(0, END)

    f = open("Details.txt", "r")
    verify = (f.readlines())
    if (verify != ""):
        if email1 and password1 in verify:
            login_sucess()
        else:
            password_not_recognised()

    else:
        user_not_found()


def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register Here")
    screen1.geometry("500x350")

    global email
    global password
    global email_entry
    global password_entry
    email = StringVar()
    password = StringVar()

    Label(screen1, text="Please enter details below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Email * ").pack()

    email_entry = Entry(screen1, textvariable=email)
    email_entry.pack()
    Label(screen1, text="Password * ").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", bg="lightgreen", height="2", width="20", command=register_user).pack()


def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("500x350")
    Label(screen2, text="Please enter details below to login").pack()
    Label(screen2, text="").pack()

    global email_verify
    global password_verify

    email_verify = StringVar()
    password_verify = StringVar()

    global email_entry1
    global password_entry1

    Label(screen2, text="Email * ").pack()
    email_entry1 = Entry(screen2, textvariable=email_verify)
    email_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password * ").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", bg="aqua", height="2", width="20", command=login_verify).pack()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("600x450")
    screen.title("Python Project")
    Label(text="Welcome\nUser", bg="skyblue", width="300", height="5", font=("Arial Black", 20)).pack()
    Label(text="").pack()
    Button(text="Login", bg="skyblue", height="3", width="50", command=login).pack()
    Label(text="").pack()
    Button(text="Register", bg="skyblue", height="3", width="50", command=register).pack()

    screen.mainloop()


main_screen()
