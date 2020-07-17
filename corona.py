
from covid import Covid

covid = Covid()

print("Select your choice")

print("\n1.Total Active Cases")
print("2.Total Deaths")
print("3.Total confirmed cases")

n = int(input("\nEnter Your choice :"))

if n==1:
 print("\nTotal Active cases currently is :",covid.get_total_active_cases(),"\n")
elif n==2:
 print("\nTotal Death cases currently is :",covid.get_total_deaths(),"\n")
elif n==3:
 print("\nTotal confirmed cases currently is :",covid.get_total_confirmed_cases(),"\n")
else:
 print("wrong choice select the correct Number\n")


