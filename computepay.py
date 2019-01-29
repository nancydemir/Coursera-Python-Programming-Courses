#hrs = raw_input("Enter Hours:")

def computepay(hrs):
    h = float(hrs)
    reghrs=40.00
    overtimehrs=h-reghrs
    regpayrate=10.50
    overtimepayrate=regpayrate*1.5
    regularpay=regpayrate*reghrs
    overtimepay=0   

    if h <=40:
        pay = regularpay
    elif h > 40:
        overtimepay=overtimepayrate*overtimehrs
        pay=overtimepay+regularpay
    print("pay is: %.2f"%pay)

computepay(45)

        
