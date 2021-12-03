#temple Eats UI

import tkinter 
from tkinter import *


class Veg_Table:
    
    def __init__(self,root):
          
        #code for creating table
        for r in range(total_rows):
            for c in range(total_columns):
                  self.e = Entry(root, width=65, fg='purple',font=('Arial',7,'bold'))
                  self.e.grid(row=r, column=c,)
                  self.e.insert(END, Veg_lst[r][c])
                  
#take the data
Veg_lst = [('VEG RESTAURANTS','ACCEPTED PAYMENT TYPES'),
('Dev Food Truck','debit/credit/cash'),
('Tommy Lunch Truck','debit/credit/cash'),
('Little Lulu','debit/credit/cash'),
('Tasty Eats','debit/credit/cash'),
('4 Brothers','debit/credit/cash'),
('New York Gyro','debit/credit/cash'),
('Mountain Pizza','debit/credit/cash'),
('Philly Halal Gyro','debit/credit/cash'),
('Mexican Grill Stand','debit/credit/cash'),
('Halal Gyro Express','debit/credit/cash'),
('Famous NY Gyro','debit/credit/cash'),
('Caribbean Feast','debit/credit/cash'),
('Sunny Halal Food','debit/credit/cash'),
('Eddies','debit/credit/cash'),
('Sexy Green Truck','debit/credit/cash'),
('Cha Cha','debit/credit/cash'),
('Eppys Truck','debit/credit/cash'),
('Ernies','debit/credit/cash'),
('The Fruit Salad & smoothie truck','debit/credit/cash'),
('E&E Gourmet Express','debit/credit/cash'),
('Chicken Heaven','debit/credit/cash'),
('Chop Chop','debit/credit/cash'),
('Fruit Salad','debit/credit/cash'),
('Kobawoo Express','debit/credit/cash'),
('Jamaican Ds','debit/credit/cash'),
('Philly Fellas Gyro Halal','debit/credit/cash'),
('Brother Pizza','debit/credit/cash'),
('Temple Teppanyaki','debit/credit/cash'),
('Foot Long','debit/credit/cash'),
('Honey','debit/credit/cash'),
('Richie Lunch Box','debit/credit/cash'),
('Cloud','debit/credit/cash'),
('Samosa Deb','debit/credit/cash'),
('Top Bap','debit/credit/cash'),
('Ray Truck','debit/credit/cash'),
('The Creperie Truck','debit/credit/cash'),
('Burger Tank','debit/credit/cash'),
('El Guaco Loco','debit/credit/cash'),
('Korea House','debit/credit/cash'),
('Vegan Tree','debit/credit/cash'),
('Subway','debit/credit/cash | diamond dollars'),
('Zen','meal equivalency | debit/credit/cash | diamond dollars'),
('Esposito Dining Center','meal plan | meal equivalency | debit/credit/cash | diamond dollars'),
('Twisted Taco','meal equivalency | debit/credit/cash | diamond dollars'),
('Morgan Dining Hall','meal plan | meal equivalency | debit/credit/cash | diamond dollars'),
('BurgerFi','meal equivalency | debit/credit/cash | diamond dollars'),
('Saladworks','meal equivalency | debit/credit/cash | diamond dollars'),
('Starbucks','debit/credit/cash | diamond dollars'),
('Pita and Co.','meal equivalency | debit/credit/cash | diamond dollars'),
('Panda Express','meal equivalency | debit/credit/cash | diamond dollars'),
('Jamba','debit/credit/cash'),
('Java City','debit/credit/cash'),
('Stella Café','debit/credit/cash')]
   
#find total number of rows and
#columns in list

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
            for c in range(total_columns):
                   self.e = Entry(root, width=65, fg='red',font=('Arial',7,'bold'))
                   self.e.grid(row=r, column=c)
                   self.e.insert(END, NonVeg_lst[r][c])

NonVeg_lst = [('NON-VEG RESTAURANTS','ACCEPTED PAYMENT TYPES'),
('Dev Food Truck','debit/credit/cash'),
('Tommy Lunch Truck','debit/credit/cash'),
('Little Lulu','debit/credit/cash'),
('Tasty Eats','debit/credit/cash'),
('4 Brothers','debit/credit/cash'),
('New York Gyro','debit/credit/cash'),
('Mountain Pizza','debit/credit/cash'),
('Philly Halal Gyro','debit/credit/cash'),
('Mexican Grill Stand','debit/credit/cash'),
('Halal Gyro Express','debit/credit/cash'),
('Famous NY Gyro','debit/credit/cash'),
('Caribbean Feast','debit/credit/cash'),
('Sunny Halal Food','debit/credit/cash'),
('Eddies','debit/credit/cash'),
('Sexy Green Truck','debit/credit/cash'),
('Cha Cha','debit/credit/cash'),
('Eppys Truck','debit/credit/cash'),
('Ernies','debit/credit/cash'),
('E&E Gourmet Express','debit/credit/cash'),
('Chicken Heaven','debit/credit/cash'),
('Chop Chop','debit/credit/cash'),
('Kobawoo Express','debit/credit/cash'),
('Jamaican Ds','debit/credit/cash'),
('Philly Fellas Gyro Halal','debit/credit/cash'),
('Brother Pizza','debit/credit/cash'),
('Temple Teppanyaki','debit/credit/cash'),
('Foot Long','debit/credit/cash'),
('Honey','debit/credit/cash'),
('Richie Lunch Box','debit/credit/cash'),
('Samosa Deb','debit/credit/cash'),
('Top Bap','debit/credit/cash'),
('Ray Truck','debit/credit/cash'),
('Burger Tank','debit/credit/cash'),
('El Guaco Loco','debit/credit/cash'),
('Korea House','debit/credit/cash'),
('Esposito Dining Center','meal plan | meal equivalency | debit/credit/cash | diamond dollars'),
('Morgan Dining Hall','meal plan | meal equivalency | debit/credit/cash | diamond dollars'),
('BurgerFi','meal equivalency | debit/credit/cash | diamond dollars'),
('Saladworks','meal equivalency | debit/credit/cash | diamond dollars'),
('Which Wich','meal equivalency | debit/credit/cash | diamond dollars'),
('Chick-fil-a','meal equivalency | debit/credit/cash | diamond dollars'),
('Twisted Taco','meal equivalency | debit/credit/cash | diamond dollars'),
('Panda Express','meal equivalency | debit/credit/cash | diamond dollars'),
('Bento Sushi','meal equivalency | debit/credit/cash | diamond dollars'),
('Così','debit/credit/cash'),
('Zaydee Kosher Delicatessen','debit/credit/cash')]

total_rows = len(NonVeg_lst)
total_columns = len(NonVeg_lst[0])
   
# create root window
root = Tk()
t = NonVeg_Table(root)
root.mainloop()



class Vegan_Table:
      
    def __init__(self,root):
          
        #code for creating table
        for r in range(total_rows):
            for c in range(total_columns):
                  self.e = Entry(root, width=65, fg='green',font=('Arial',8,'bold'))
                  self.e.grid(row=r, column=c)
                  self.e.insert(END, Vegan_lst[r][c])

Vegan_lst =[('VEGAN RESTAURANTS','ACCEPTED PAYMENT TYPES'),
('Dev Food Truck','debit/credit/cash'),
('New York Gyro','debit/credit/cash'),
('Mountain Pizza','debit/credit/cash'),
('Philly Halal Gyro','debit/credit/cash'),
('Mexican Grill Stand','debit/credit/cash'),
('Halal Gyro Express','debit/credit/cash'),
('Famous NY Gyro','debit/credit/cash'),
('Sunny Halal Food','debit/credit/cash'),
('Ernies','debit/credit/cash'),
('The Fruit Salad & smoothie truck','debit/credit/cash'),
('Chicken Heaven','debit/credit/cash'),
('Fruit Salad','debit/credit/cash'),
('Philly Fellas gyro halal','debit/credit/cash'),
('Samosa Deb','debit/credit/cash'),
('Ray Truck','debit/credit/cash'),
('Vegan Tree','debit/credit/cash'),
('Subway','Diamond dollars | debit/credit/cash'),
('Esposito Dining center','Meal plan | meal equivalency | debit/credit/cash | diamond dollars'),
('Twisted Taco','meal equivalency | debit/credit/cash | diamond dollars'),
('Morgan Dining Hall','meal plan | meal equivalency | debit/credit/cash | diamond dollars'),
('BurgerFi','meal equivalency | debit/credit/cash | diamond dollars'),
('Saladworks','meal equivalency | debit/credit/cash | diamond dollars'),
('Starbucks','debit/credit/cash | diamond dollars'),
('Pita and Co.','meal equivalency | debit/credit/cash | diamond dollars'),
('Panda Express','meal equivalency | debit/credit/cash | diamond dollars'),
('Jamba','debit/credit/cash'),
('Java City','debit/credit/cash'),
('Stella Café','debit/credit/cash')]


total_rows = len(Vegan_lst)
total_columns = len(Vegan_lst[0])
   
# create root window
root = Tk()
t = Vegan_Table(root)
root.mainloop()


