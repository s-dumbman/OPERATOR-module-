from main import *
def Copyright():
    t = ("// OPERATOR MODULE // CREATOR -- D6CHECKER // VERSION -- b0.1 ~~2022.5.22")
    return t
def HOW_TO_USE_THIS_PACKAGE():
    t = '{}'.format("https://gist.githubusercontent.com/D6CHECKER/56a213a944d0358d918988d36b18226e/raw/f432fcb03f77c8cd0d69d6670f80c7158e82e690/main.py")
    return t
def
def LocalForm():
    try:
        import tkinter
        def TITLEFORM():
            c = '{}'.format("operate")
            return c
        def guiFORM():
            win = tkinter.Tk()
            win.geometry("100x100")
            win.title(TITLEFORM())
            btn = tkinter.Button(win)
            btn.config(width=1000, height=1000, text="operate")
            btn.config(command=script)
            btn.pack()
            win.mainloop()
        guiFORM()
    finally:
        print("")
if __name__=='__main__':
    LocalForm()