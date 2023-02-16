# #Functions
def fxn1():
    print("My first Function.")
fxn1()

def rect():
    l = int(input("Enter Length:"))
    w = int(input("Enter width:"))
    peri = 2*(l+w)
    Area= l*w
    print("The area =",Area," and Perimeter =",peri)

rect()

def rect(l,w):
    peri = 2*(l+w)
    Area= l*w
    print("The area =",Area," and Perimeter =",peri)

rect(6,5)

def rect(l=6,w=5):
    peri = 2*(l+w)
    Area= l*w
    print("The area =",Area," and Perimeter =",peri)

rect()

def strf():
    mystr = str(input("Enter your string: "))
    nstr = mystr.capitalize()
    print("My old string is",mystr,"\n my new string is",nstr)

strf()