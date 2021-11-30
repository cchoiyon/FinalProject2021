import tkinter


root = tkinter.Tk()
root.title("Temple Eats")
root.geometry("400x400")

#background color
root['background']='#FFFAF0'

#text
text = tkinter.Label(root, text="Hello! What Would You Like To Eat Today?",height = 5, bg="#FFFAF0")
text.place(x=50,y=0)


#window functions
def openwindow1():
    newWindow = tkinter.Toplevel(root)
    newWindow.geometry("400x400")
    tkinter.Label(newWindow,
          text ="Vegetarian Restaurants").pack()

def openwindow2():
    newWindow = tkinter.Toplevel(root)
    newWindow.geometry("400x400")
    tkinter.Label(newWindow,
          text ="Vegan Restaurants").pack()

def openwindow3():
    newWindow = tkinter.Toplevel(root)
    newWindow.geometry("400x400")
    tkinter.Label(newWindow,
          text ="Non-Veg Restaurants").pack()
#buttons 
button1= tkinter.Button(root, text='Vegetarian', width=30, height=3, command = openwindow1)
button1.pack()
button2 = tkinter.Button(root, text='Vegan', width=30, height=3,command = openwindow2)
button2.pack()
button3 = tkinter.Button(root, text='Non-Veg', width=30, height=3,command = openwindow3)
button3.pack()

#button postitions 
button1.place(x=50,y=100)
button2.place(x=50,y=175)
button3.place(x=50,y=250)


root.mainloop()
