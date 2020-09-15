import sqlite3, time

def login():
    while True:
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        with sqlite3.connect("login.db") as db:
            cursor = db.cursor()
        find_user = ("SELECT * FROM user WHERE username = ? AND password = ?")
        cursor.execute(find_user, [(username), (password)])
        result = cursor.fetchall()

        if result:
            for i in result:
                print("Welcome "+i[2])
            #return("exit")
            break
        else:
            print("Username and password not recognised")
            again = input("Do you want to try again?(y/n): ")
            if again.lower() == "n":
                print("Goodbye")
                time.sleep(1)
                #return("exit")
                break

login()

#=====================================================Corner Street Chicken Dust Programme=========================================================================
from tkinter import*
import random
#import time;

root = Tk()
root.geometry("1600x800+0+0")
root.title("Corner Street Chicken Dust Management Systems")

text_Input = StringVar()
operator = ""

Tops = Frame(root, width=1600, height=50, bg = "powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

frame1 = Frame(root, width=800, height=700, relief=SUNKEN)
frame1.pack(side=LEFT)

frame2 = Frame(root, width=300, height=700, relief=SUNKEN)
frame2.pack(side=RIGHT)

#====================================================Time==========================================================================
localtime = time.asctime(time.localtime(time.time()))
#====================================================Info==========================================================================

lblInfo = Label(Tops, font=('arial',50, 'bold'), text="Corner Street Chicken Dust Management Systems", fg="Steel Blue", bd=10, anchor='w')
lblInfo.grid(row=0, column=0)

lblInfo = Label(Tops, font=('arial',20, 'bold'), text=localtime, fg="Steel Blue", bd=10, anchor='w')
lblInfo.grid(row=1, column=0)

#====================================================Calculator====================================================================
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup =str(eval(operator))
    text_Input.set(sumup)
    operator = ""

def Ref():
    x = random.randint(10908, 500876)
    randomRef = str(x)
    rand.set(randomRef)

    CoF =float(Fries.get()) #Cost of Fries
    CoD = float(Drinks.get()) #Cost of Drinks
    CoFilet = float(Filet.get()) #Cost of Filet
    CoBurger = float(Burger.get()) #Cost of Burger
    CoChicBurger = float(Chicken_Burger.get()) #Cost of Chicken burger
    CoCheese_Burger = float(Cheese_Burger.get())  # Cost of Cheese burger

    CostofFries = CoF * 18.99
    CostofDrinks = CoD * 20
    CostofFilet = CoFilet * 25.99
    CostofBurger = CoBurger * 22.99
    CostofChicken_Burger = CoChicBurger * 23.50
    CostofCheese_Burger = CoCheese_Burger * 22.50

    CostofMeal = "R", str('%.2f' % (CostofFries + CostofDrinks + CostofFilet + CostofBurger
                                   + CostofChicken_Burger + CostofCheese_Burger))

    PayTax = ((CostofFries + CostofDrinks + CostofFilet + CostofBurger
                                   + CostofChicken_Burger + CostofCheese_Burger) * 0.15)

    TotalCost = (CostofFries + CostofDrinks + CostofFilet + CostofBurger
                                   + CostofChicken_Burger + CostofCheese_Burger)

    Ser_Charge = ((CostofFries + CostofDrinks + CostofFilet + CostofBurger
                                   + CostofChicken_Burger + CostofCheese_Burger)/99)

    Service = "R", str('%.2f' % Ser_Charge)
    OverAllCost = "R", str('%.2f' % (PayTax + TotalCost + Ser_Charge))
    PaidTax = "R", str('%.2f' % PayTax)
    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)


def qExit():
    root.destroy()

def Reset():
    rand.set("")
    Fries.set("")
    Burger.set("")
    Filet.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Chicken_Burger.set("")
    Cheese_Burger.set("")



txtDisplay = Entry(frame2, font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4,
                   bg="powder blue", justify='right')
txtDisplay.grid(columnspan=4)

btn7=Button(frame2, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
            text="7", bg="powder blue", command=lambda: btnClick(7)).grid(row=2, column=0)

btn8=Button(frame2, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
            text="8", bg="powder blue", command=lambda: btnClick(8)).grid(row=2, column=1)

btn9=Button(frame2, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
            text="9", bg="powder blue", command=lambda: btnClick(9)).grid(row=2, column=2)

Addition=Button(frame2, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
            text="+", bg="powder blue", command=lambda: btnClick("+")).grid(row=2, column=3)
#===============================================================================================================================

btn4=Button(frame2, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
            text="4", bg="powder blue", command=lambda: btnClick(4)).grid(row=3, column=0)

btn5=Button(frame2, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
            text="5", bg="powder blue", command=lambda: btnClick(5)).grid(row=3, column=1)

btn6=Button(frame2, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
            text="6", bg="powder blue", command=lambda: btnClick(6)).grid(row=3, column=2)

Subtraction=Button(frame2, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
            text="-", bg="powder blue", command=lambda: btnClick("-")).grid(row=3, column=3)
#===============================================================================================================================

btn1=Button(frame2, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
            text="1", bg="powder blue", command=lambda: btnClick(1)).grid(row=4, column=0)

btn2=Button(frame2, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
            text="2", bg="powder blue", command=lambda: btnClick(2)).grid(row=4, column=1)

btn3=Button(frame2, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
            text="3", bg="powder blue", command=lambda: btnClick(3)).grid(row=4, column=2)

Multiply=Button(frame2, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
            text="*", bg="powder blue", command=lambda: btnClick("*")).grid(row=4, column=3)
#==============================================================================================================================

btn0=Button(frame2, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
            text="0", bg="powder blue", command=lambda: btnClick(0)).grid(row=5, column=0)

btnClear=Button(frame2, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
            text="C", bg="powder blue", command=btnClearDisplay).grid(row=5, column=1)

btnEquals=Button(frame2, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
            text="=", bg="powder blue", command=btnEqualsInput).grid(row=5, column=2)

Division=Button(frame2, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),
            text="/", bg="powder blue", command=lambda: btnClick("/")).grid(row=5, column=3)
#=============================================Fast_Food 1============================================================================

rand = StringVar()
Fries = StringVar()
Burger = StringVar()
Filet = StringVar()
SubTotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
Cost = StringVar()
Chicken_Burger = StringVar()
Cheese_Burger = StringVar()

lblReference = Label(frame1, font=('arial',16,'bold'), text="Reference", bd=16, anchor='w')
lblReference.grid(row=0, column=0)
txtReference = Entry(frame1, font=('arial',16,'bold'), textvariable=rand, bd=10, insertwidth=4,
                     bg="powder blue", justify='right')
txtReference.grid(row=0, column=1)

lblFries = Label(frame1, font=('arial',16,'bold'), text="Large Fries", bd=16, anchor='w')
lblFries.grid(row=1, column=0)
txtFries = Entry(frame1, font=('arial',16,'bold'), textvariable=Fries, bd=10, insertwidth=4,
                     bg="powder blue", justify='right')
txtFries.grid(row=1, column=1)

lblBurger = Label(frame1, font=('arial',16,'bold'), text="Burger Meal", bd=16, anchor='w')
lblBurger.grid(row=2, column=0)
txtBurger = Entry(frame1, font=('arial',16,'bold'), textvariable=Burger, bd=10, insertwidth=4,
                     bg="powder blue", justify='right')
txtBurger.grid(row=2, column=1)

lblFilet = Label(frame1, font=('arial',16,'bold'), text="Filet Meal", bd=16, anchor='w')
lblFilet.grid(row=3, column=0)
txtFilet = Entry(frame1, font=('arial',16,'bold'), textvariable=Filet, bd=10, insertwidth=4,
                     bg="powder blue", justify='right')
txtFilet.grid(row=3, column=1)

lblChicken = Label(frame1, font=('arial',16,'bold'), text="Chicken Meal", bd=16, anchor='w')
lblChicken.grid(row=4, column=0)
txtChicken = Entry(frame1, font=('arial',16,'bold'), textvariable=Chicken_Burger, bd=10, insertwidth=4,
                     bg="powder blue", justify='right')
txtChicken.grid(row=4, column=1)

lblCheese = Label(frame1, font=('arial',16,'bold'), text="Cheese Meal", bd=16, anchor='w')
lblCheese.grid(row=5, column=0)
txtCheese = Entry(frame1, font=('arial',16,'bold'), textvariable=Cheese_Burger, bd=10, insertwidth=4,
                     bg="powder blue", justify='right')
txtCheese.grid(row=5, column=1)
#=============================================Fast_Food 2============================================================================

lblDrinks = Label(frame1, font=('arial',16,'bold'), text="Drinks", bd=16, anchor='w')
lblDrinks.grid(row=0, column=2)
txtDrinks = Entry(frame1, font=('arial',16,'bold'), textvariable=Drinks, bd=10, insertwidth=4,
                     bg="#ffffff", justify='right')
txtDrinks.grid(row=0, column=3)

lblCost = Label(frame1, font=('arial',16,'bold'), text="Cost of Meal", bd=16, anchor='w')
lblCost.grid(row=1, column=2)
txtCost = Entry(frame1, font=('arial',16,'bold'), textvariable=Cost, bd=10, insertwidth=4,
                     bg="#ffffff", justify='right')
txtCost.grid(row=1, column=3)

lblService = Label(frame1, font=('arial',16,'bold'), text="Service Charge", bd=16, anchor='w')
lblService.grid(row=2, column=2)
txtService = Entry(frame1, font=('arial',16,'bold'), textvariable=Service_Charge, bd=10, insertwidth=4,
                     bg="#ffffff", justify='right')
txtService.grid(row=2, column=3)

lblStateTax = Label(frame1, font=('arial',16,'bold'), text="Tax", bd=16, anchor='w')
lblStateTax.grid(row=3, column=2)
txtStateTax = Entry(frame1, font=('arial',16,'bold'), textvariable=Tax, bd=10, insertwidth=4,
                     bg="#ffffff", justify='right')
txtStateTax.grid(row=3, column=3)

lblSubTotal = Label(frame1, font=('arial',16,'bold'), text="Sub Total", bd=16, anchor='w')
lblSubTotal.grid(row=4, column=2)
txtSubTotal = Entry(frame1, font=('arial',16,'bold'), textvariable=SubTotal, bd=10, insertwidth=4,
                     bg="#ffffff", justify='right')
txtSubTotal.grid(row=4, column=3)

lblTotalCost = Label(frame1, font=('arial',16,'bold'), text="Total Cost", bd=16, anchor='w')
lblTotalCost.grid(row=5, column=2)
txtTotalCost = Entry(frame1, font=('arial',16,'bold'), textvariable=Total, bd=10, insertwidth=4,
                     bg="#ffffff", justify='right')
txtTotalCost.grid(row=5, column=3)
#==================================================Button=========================================================================

btnTotal=Button(frame1, padx=16, pady=8, bd=16, fg="black", font=('arial',16,'bold'), width=10,
                text="Total", bg="powder blue", command = Ref).grid(row=7, column=1)

btnReset=Button(frame1, padx=16, pady=8, bd=16, fg="black", font=('arial',16,'bold'), width=10,
                text="Reset", bg="powder blue", command = Reset).grid(row=7, column=2)

btnExit=Button(frame1, padx=16, pady=8, bd=16, fg="black", font=('arial',16,'bold'), width=10,
                text="Exit", bg="powder blue", command = qExit).grid(row=7, column=3)

root.mainloop()
3

