#student name input
name = input("enter student name: ")

#marks input
 maths = float(input("Enter maths marks: "))

 physics = float(input(Enter physics marks: "))    

 English = float(input(Enter English marks: "))
  
 programming = float(input(Enter programming marks: "))
                           
 Electronics = float(input(Enter Electronics marks: "))


 #All subject marks add
  total = maths + physics + English + programming + Electonics



#find percentage
percentage = total/5

#percentage according grade
if percentage >=90:
  grade = "A+"

elif percentage >=80:
   grade = "A"

elif percentage >=70:
   grade = "B"

elif percentage >=60:
   grade = "C"

elif percentage >=50:
   grade = "D"

else:
  grade = "F"


#Result heading print
print("\n---Student Result---")

print("Name:", name)

print("Total Marks:", total, "/ 500")

print("Percentage:", percentage, "%")

print("Grade:", grade)



#Check FAIL PASS
if percentage >=40:
   print("Result: PASS")
else:
  print("Result: FAIL")


 

 
 
