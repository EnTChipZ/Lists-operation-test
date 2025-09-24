# x=7
# y=10
# if x==5:
#    print(x)
# else:
#     print(y)

# firstname="Avril Carlos"
# lastname="Lirio"
# print(firstname + " " + lastname)
# print(firstname, lastname)
# print(f"{firstname} {lastname}")
# print("")
# print("Ako si "+ firstname + " " + lastname)
# print("Ako si", firstname, lastname)
# print(f"Ako si {firstname} {lastname}")

# name="Avril Carlos M. Lirio"
# age=20
# print(type(age))
# newage=str(age)
# print(type(newage))
# print(f"Hello {name}, You are {age} years old!")
# print("Hello", name, "You are", age, "years old!")
# print("Hello "+ name + " You are ", age, "years old!")
# print("Hello "+ name + " You are " + newage + " years old!")

# aa=[1 , 2]
# bb=(1 , 2)
# cc={1 , 2}
# a=1
# b="Avril"
# c=1.5413
# print(type(aa))
# print(type(bb))
# print(type(cc))
# print(str(a))
# print(str(b))
# print(str(c))
# print(type(a))
# print(type(b))
# print(type(c))
# aa=int(a)
# bb=int(b)
# cc=int(c)
# print(type(aa))
# print(type(bb))
# print(type(cc))
# print(cc)

# Fname=input("Firstname:")
# Lname=input("Lastname:")
# age=input("Age:")
# brgy=input("Brgy:")
# municipality=input("Municipality:")
# province=input("Province:")
# print(f"Hello {Fname + " " + Lname}, you are {age} years old and you live in brgy. {brgy}, {municipality}, {province}")
# print(type(age))

# Fnum=int(input("Firstnumber:"))
# Snum=int(input("Secondnumber"))
# sum=float(Fnum + Snum)
# prod=float(Fnum * Snum)
# diff=float(Fnum - Snum)
# Qoutient=float(Fnum / Snum)
# FloorDiv=float(Fnum // Snum)
# modular=float(Fnum % Snum)
# exponent=float(Fnum ** Snum)
# print(f"Answers: {sum: .2f}, {prod: .2f}, {diff: .2f}, {Qoutient: .2f}, {FloorDiv: .2f}, {modular: .2f}, {exponent: .2f},")
# print(f"{sum: .2f}")
# print(f"{prod: .2f}")
# print(f"{diff: .2f}")
# print(f"{Qoutient: .2f}")
# print(f"{FloorDiv: .2f}")
# print(f"{modular: .2f}")
# print(f"{exponent: .2f}")

#Implicity
# a = 1
# b = 2.0
# c = a + b
# print(c)
#Explicitly
# a = 1
# print(type(a))
# b = int (a)

# a = 1
# b = 1
# print(id(a))
# print(id (b))

# a = ["apple", "banana"]
# b = ["apple", "banana"]
# print(a==b)
# print(a is b)
# print(id(a))
# print(id (b))

#Userinput
# num=int(input("Enter Your Number:"))
# if num%2==0:
#     print(f"The number {num} is EVEN")
# else:
#     print(f"The number {num} is ODD")
#Userinput string
# Let1=str(input("Enter a letter:"))
# if Let1 in "a, e, i, o, u":
#     print(f"The letter {Let1} is a vowel")
# else:
#     print(f"The letter {Let1} is consonant")

#Escape character
# txt = "hello my name is \"Avril Carlos Lirio\" i am from \"Victoria, Laguna\"."
# print(txt)

# while True:
#     FFnum=input("Firstnumber:")
#     SSnum=input("Secondnumber:")

#     try:
#         Fnum = float(FFnum)
#         Snum = float(SSnum)
#         sum=float(Fnum + Snum)
#         prod=float(Fnum * Snum)
#         diff=float(Fnum - Snum)
#         Qoutient=float(Fnum / Snum)
#         FloorDiv=float(Fnum // Snum)
#         modular=float(Fnum % Snum)
#         exponent=float(Fnum ** Snum)
#         print(f"{sum: .2f}")
#         print(f"{prod: .2f}")
#         print(f"{diff: .2f}")
#         print(f"{Qoutient: .2f}")
#         print(f"{FloorDiv: .2f}")
#         print(f"{modular: .2f}")
#         print(f"{exponent: .2f}")
    
#     except ZeroDivisionError:
#         print("Cannot be divided to zero")
#         continue

#     except ValueError:
#         print("Number number lang tyo boi")
#         continue
    
#     while True:
#         user = input("Would you like to continue, Y/N? ")
#         if user.upper()=='Y':
#             break
#         elif user.upper()=='N':
#             print("program shutdown")
#             exit()
#         else:
#             print("invalid input")
#             continue

Username = input("Username: ")
Password = input("Password: ")
if (Username == "admin") & (Password == "admin") | (Username == "ADMIN") & (Password == "ADMIN"):
    print("Pasok ka pogi")
else:
    print("womp womp di ka pasok")

# while True:
#     Username = input("Username: ")
#     Password = input("Password: ")
#     if (Username == "admin") & (Password == "admin") | (Username == "ADMIN") & (Password == "ADMIN"):
#         print("Pasok ka pogi")
#         break
#     else:
#      print("Ulitin mo may mali ka")

#while loop
# i = 0
# while i<=5:
#     print(i)
#     i += 1

#while loop with sum
# x = int(input("Startnumber: "))
# y = int(input("Endnumber: "))
# sum=0
# while x<=y:
# #     print(x)
# #     sum+=x
# #     x+=1
#     if x%2==1:
#         print(x)
# print(f"Sum is: {sum}")

#for loop with sum
# x = int(input("Startnumber: "))
# y = int(input("Endnumber: "))
# # sum=0
# for xy in range(x , y+1):
#     print(xy)
#     sum+=xy
# print(f"Sum is: {sum}")

# for xy%2==1:
    # print(xy)

# user = int(input("Lagay ka number: "))
# if user < 0:
#     print(f"{user} ay negative number")
# elif user>0:
#     print(f"{user} ay positive number")
# else:
#     print("ZERO")