#Temple Eats

choose = input("Hello! What Would You Like To Eat Today?: vegetarian/non-vegetarian/vegan: ")
def choice():
    if choose == "vegetarian":
        list1 = ['dev food truck','tommy lunch truck','little lulu','tasty eats','4 brothers','new york gyro','mountain pizza','philly halal gyro','mexican grill stand','halal gyro express','famous ny gyro','caribbean feast','sunny halal food','eddies','sexy green truck','cha cha','eppys truck','ernies','the fruit salad & smoothie truck','e&e gourmet express','chicken heaven','chop chop','fruit salad','kobawoo express','jamaican ds','philly fellas gyro halal','brother pizza ','temple teppanyaki','foot long','honey','richie lunch box','cloud','samosa deb','top bap','ray truck','the creperie truck','burger tank','el guaco loco','korea house','vegan tree','subway','zen','esposito dining center','twisted taco','morgan dining hall','burgerfi','saladworks','starbucks','pita and Co.','panda express','jamba','java city','stella café']
        print(*list1, sep = "\n")

    
    elif choose == "non-vegetarian":
        list2 = ['dev food truck','tommy lunch truck','little lulu','tasty eats','4 brothers','new york gyro','mountain pizza','philly halal gyro','mexican grill stand','halal gyro express','famous ny gyro','caribbean feast','sunny halal food','eddies','sexy green truck','cha cha','eppys truck','ernies','e&e gourmet express','chicken heaven','chop chop','kobawoo express','jamaican ds','philly fellas gyro halal','brother pizza ','temple teppanyaki','foot long','honey','richie lunch box','samosa deb','top bap','ray truck','burger tank','el guaco loco','korea house','esposito dining center','morgan dining hall','burgerfi','saladworks','which wich','chick-fil-a','twisted taco','panda express','bento sushi','così','zaydee kosher delicatessen'] 
        print(*list2, sep = "\n")
        
    elif choose == "vegan":
        list3 = ['dev food truck','new york gyro','mountain pizza','philly halal gyro','mexican grill stand','halal gyro express','famous ny gyro','sunny halal food','ernies','the fruit salad & smoothie truck','chicken heaven','fruit salad','philly fellas gyro halal','samosa deb','ray truck','vegan tree','subway','esposito dining center','twisted taco','morgan dining hall','burgerfi','saladworks','starbucks','pita and co.','panda express','jamba','java city','stella café']
        print(*list3, sep = "\n")

    else:
        print("Please Choose An Option")

choice()


def payment():
    diamondDollars_credit_debit_cash = ['esposito dining center','twisted taco','subway','which wich','zen','saladworks','pita and co.','chick-fil-a','burgerfi','starbucks','panda express','jamba','java city','stella café','bento sushi','Così','Zaydee Kosher Delicatessen']
    meal_plans = ['esposito dining center','morgan dining hall']
    meal_equivalency = ['esposito dining center','morgan dining hall','twisted taco','which wich','saladworks','zen','pita and co.','chick-fil-a','burgerfi']
    debit_credit_cash = ['vegan tree','korea house','el guaco loco','burger tank','the creperie truck','ray truck','top bap','samosa deb','cloud','richie lunch box','honey','foot long','temple teppanyaki','brother pizza','philly fellas gyro halal','jamaican ds','kobawoo express','fruit salad','chop chop','chicken heaven','e&e gourmet express','the fruit salad & smoothie truck','ernies','eppys truck','cha cha','sexy green truck','eddies','sunny halal food','caribbean feast','famous ny gyro','halal gyro express','mexican grill stand','philly halal gyro','mountain pizza','new york gyro','4 brothers','tasty eats','little lulu','tommy lunch truck','dev food truck']
    

    if pick in diamondDollars_credit_debit_cash and pick in meal_equivalency and pick in meal_plans:
        print("Accepts diamond dollars, credit/debit/cash, meal equivalency and meal plan board swipe")

    elif pick in diamondDollars_credit_debit_cash and pick in meal_equivalency:
        print("Accepts diamond dollars, credit/debit/cash and meal equivalencies")

    elif pick in diamondDollars_credit_debit_cash and pick in meal_plans:
        print("Accepts diamond dollars, credit/debit/cash and meal plan board swipe")

    elif pick in meal_plans and pick in meal_equivalency:
        print("Accepts meal plans board swipe and meal equivalencies")

    elif pick in diamondDollars_credit_debit_cash:
        print("Accepts Diamond dollars and credit/debit/cash")

    elif pick in meal_plans:
        print("Accepts meal plan board swipe")

    elif pick in meal_equivalency:
        print("Accepts meal equivalency")

    elif pick in debit_credit_cash:
        print("Accepts debit/credit/cash")

    else:
        print("Not sure, sorry!")
    

pick = input("Sounds Great! Which dining place would you like to go to: ")
payment()

