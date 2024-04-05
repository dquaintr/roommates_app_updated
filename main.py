from flatclasses import Bill, Flatmate
from pdf import Pdf

print("Hello User!")
a = float(input("Enter the bill amount: "))
b= input("Enter the period: ")
c= input("Enter the name of the first roommate: ")
d= input("Enter the name of the second roommate: ")
e = float(input(f"How many days was {c} present? "))
f = float(input(f"How many days was {d} present? "))

bill = Bill(amount= a,period = b)
flatmate1 = Flatmate(name=c, days_in_house=e)
flatmate2 = Flatmate(name=d, days_in_house = f)

print(c,  "pays: ", flatmate1.pays(bill, flatmate2))
print(d, " pays: ", flatmate2.pays(bill, flatmate1))

pdf_report = Pdf(filename="Report_Test.pdf")
print(pdf_report.generate(flatmate1, flatmate2, bill =bill))
