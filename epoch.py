import time

currentyear=2015

def mytime():

    global currentyear

    secondssinceepoch=time.time()
    epochminutes=secondssinceepoch/60
    epochhours=epochminutes/60
    epochdays=epochhours/24
    epochyears=epochdays/365
    print epochyears
    print currentyear-epochyears
  
    
    
mytime()
