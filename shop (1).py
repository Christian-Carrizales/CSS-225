#shop.py
def check_money(total_cost, customer_money):
    if total_cost == "can_pay":
        print("Shopping Total!")
    elif customer_money == "check_money":
        print("Enough To Pay")
    else: print("Not Enough To Pay")    
#This should print False
    if can_pay == check_money(107, 49):
        print("can_pay")
    elif can_pay == "107":
        print("Shopping Total!")
    else: print("False Not Enough To Pay")    
#This should print True
    if can_pay == check_money(6, 88):
        print("can_pay")
    elif can_pay == "6":
        print("Shopping Total!")
    else: print("True Enough To Pay")
    
