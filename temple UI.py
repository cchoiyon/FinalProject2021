#temple ui

import tkinter

from tkinter import *
  
class Veg_Table:
      
    def __init__(self,root):
          
        # code for creating table
        for r in range(total_rows):
            for p in range(total_columns):
                  
                self.e = Entry(root, width=30, fg='black',
                               font=('Arial',12,'bold'))
                  
                self.e.grid(row=r, column=p)
                self.e.insert(END, Veg_lst[r][p])
  
# take the data
Veg_lst = [('which wich','accepts meal equivalency'),
       ('saladworks','accepts credit/debit/cash')]
   
# find total number of rows and
# columns in list
total_rows = len(Veg_lst)
total_columns = len(Veg_lst[0])
   
# create root window
root = Tk()
t = Veg_Table(root)
root.mainloop()
