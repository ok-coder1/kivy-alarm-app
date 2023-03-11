import tkinter
import webbrowser

Window = tkinter.Tk()

def openURL():
    webbrowser.open_new_tab("https://ok-coder1.github.io/Personal-Site/")

urlOpenButton = tkinter.Button(Window, text = "Click Here!", command = openURL)
urlOpenButton.pack()

Window.mainloop()