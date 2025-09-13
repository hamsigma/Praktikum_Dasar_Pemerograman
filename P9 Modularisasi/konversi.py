#celcius
def celciuskefahrenheit(c):
    return (c * 9/5) + 32

def celciuskereamur(c):
    return (4/5) * c

def celciuskekelvin(c):
    return c + 273.15



#reamur
def reamurkecelcius(r):
    return (5/4) * r

def reamurkefahrenheit(r):
    return (9/4) * r + 32

def reamurkekelvin(r):
    return (5/4) * r + 273



#farhrenheit
def farhenheitkekelvin(f):
    return (f - 32) * 5/9 + 273.15

def farhrenheitkecelcius(f):
    return (f - 32) * 5/9

def farhrenheitkereamur(f):
    return (4/9) * (f - 32 )


#kelvin
def kelvinkefarhrenheit(k):
    return (k - 273.15) * 9/5 +32

def kelvinkecelcius(k):
    return k - 273.15

def kelvinkereamur(k):
    return (4/5) * (k - 273)
    