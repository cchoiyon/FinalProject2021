#temple ui

import tkinter

from tkinter import *
  
class Veg_Table:
      
    def __init__(self,root):
          
        #code for creating table
        for r in range(total_rows):
            for p in range(total_columns):
                  
                self.e = Entry(root, width=30, fg='black',
                               font=('Arial',12,'bold'))
                  
                self.e.grid(row=r, column=p)
                self.e.insert(END, Veg_lst[r][p])
  
#take the data
Veg_lst = [('dev food truck','Accepts debit or credit or cash'),
('tommy lunch truck','Accepts'),
('little lulu','Accepts'),
('tasty eats','Accepts'),
('4 brothers','Accepts'),
('new york gyro','Accepts'),
('mountain pizza','Accepts'),
('philly halal gyro','Accepts'),
('mexican grill stand','Accepts'),
('halal gyro express','Accepts'),
('famous ny gyro','Accepts'),
('caribbean feast','Accepts'),
('sunny halal food','Accepts'),
('eddies','Accepts'),
('sexy green truck','Accepts'),
('cha cha','Accepts'),
('eppys truck','Accepts'),
('ernies','Accepts'),
('the fruit salad & smoothie truck','Accepts'),
('e&e gourmet express','Accepts'),
('chicken heaven','Accepts'),
('chop chop','Accepts'),
('fruit salad','Accepts'),
('kobawoo express','Accepts'),
('jamaican ds','Accepts'),
('philly fellas gyro halal','Accepts'),
('brother pizza','Accepts'),
('temple teppanyaki','Accepts'),
('foot long','Accepts'),
('honey','Accepts'),
('richie lunch box','Accepts'),
('cloud','Accepts'),
('samosa deb','Accepts'),
('top bap','Accepts'),
('ray truck','Accepts'),
('the creperie truck','Accepts'),
('burger tank','Accepts'),
('el guaco loco','Accepts'),
('korea house','Accepts'),
('vegan tree','Accepts'),
('subway','Accepts'),
('zen','Accepts'),
('esposito dining center','Accepts'),
('twisted taco','Accepts'),
('morgan dining hall','Accepts'),
('burgerfi','Accepts'),
('saladworks','Accepts'),
('starbucks','Accepts'),
('pita and Co.','Accepts'),
('panda express','Accepts'),
('jamba','Accepts'),
('java city','Accepts'),
('stella café','Accepts')]
   
# find total number of rows and
# columns in list
total_rows = len(Veg_lst)
total_columns = len(Veg_lst[0])
   
# create root window
root = Tk()
t = Veg_Table(root)
root.mainloop()


class NonVeg_Table:
      
    def __init__(self,root):
          
        #code for creating table
        for r in range(total_rows):
            for p in range(total_columns):
                  
                self.e = Entry(root, width=30, fg='black',
                               font=('Arial',12,'bold'))
                self.e.grid(row=r, column=p)
                self.e.insert(END, Veg_lst[r][p])

                


            
