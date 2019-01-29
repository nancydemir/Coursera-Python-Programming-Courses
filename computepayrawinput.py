def computepay(h,r):
  # return 42.37
    h = float(h)
    reghrs=40.00
    overtimehrs=h-reghrs
    regpayrate=float(r)
    overtimepayrate=regpayrate*1.5
    regularpay=regpayrate*reghrs
    overtimepay=0   

    if h <=40:
        pay = regularpay
    elif h > 40:
        overtimepay=overtimepayrate*overtimehrs
        pay=overtimepay+regularpay
    #print("pay is: %.2f"%pay)
    return pay


hours = raw_input("Enter Hours:")
rate= raw_input("Enter Rate:")
p = computepay(hours,rate)
print p
