# conditinal satements


#### by using if statement 

# 1//
age = int(input("Enter your age :"))
if age >= 18 :
    print ("you are eligible to vote")

# 2////
num = 33

if num > 0:
    print("Positive Number")

# 3///
marks = 99

if marks == 99:
    print("Excellent!")

# 4///
stock = 11 
if stock > 2:
    print("Stock is available")

# 5///
age = 20 
if age >=18:
    print("you are an adult")

#6///
temprature = 110 
if temprature >100:
    print ("temprature is high")

#7///
salery = 66000
if salery > 50000:
    print ("you are doing well")

# -------------------------- 
#### by using elif statement 
#---------------------------


#1///
num = -4
if num > 0:
    print ("positive number")
else:
    print ("negative number")



#2///
salery = 50000
if salery >40000:
    print ("you doing well")
else:
    print ("not bad")


#3///
age = 22
if age <18:
    print ("you are adult")
else:
    print ("you are not an adult")


#4///
marks = 30 
if marks >= 35:
    print ("you are pass")
else:
    print ("you are fail")

#5///
stock = 4 
if stock>3:
    print ("stock is avilable")
else:
    print ("stock is not avilable")    

#7///
num = 13
if num >3:
    print ("number is greter then 3")
else:
    print ("num is not greter then 3")


#--------------------------------------
####useing  if - elif - else statement 
# -------------------------------------       




#1///////
marks = 89 
if marks > 80:
    print("grade A")
elif marks > 60:
    print("grade B")
elif marks > 40:
    print("grade C")
else:
    print("grade D")

#2////

stock = 20 
if stock >1:
    print ("we have to restore the stock")
elif stock > 15:
    print("yes we have a stock ")
elif stock >21:
    ("we dont have a stock")
else:
    print ("no stock ") 


#3////
num = 22 
if num >14:
    print ("num  is smaller then 22")
elif num >23:
    print ("num is big then 22 ")
elif num >22:
    print("num is same as 22 ") 
else:
    print ("no num ") 


# 5////
signal = "red"
if signal == "green":
    print("you can go now ")
elif signal == "yellow":
    print ("you have to wait")
elif signal == "red":
    print("stop on signal")
else:
    print("go to home ")

#6////
num1 = int (input ("Enter your num1"))
num2 = int (input ("Enter your num 2"))
if num >= 20:
    print (num1 + num2)
elif num <=20:
    print (num1 - num2)
else:
    print("no num")

#7///
age = 50 
if age >20:
    print("your are adult")
elif age >55:
    print ("your are older")
else:
    print("minor")



#-------------------------------------------------
##### using nested if 
#------------------------------------------------


#1///
marks = int (input("Enter your marks"))
documenets = input ("verify your dodcumenets")
if marks >60:
    print("ypu can get the addmission")
    if documenets== "yes":
        print("documents verifyed")
else:
    print("you can not get the addmission")