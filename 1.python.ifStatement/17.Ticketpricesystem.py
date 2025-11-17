Age=int(input("Age of Passenger="))
if Age <= 18:
   Amount= 50
elif Age <= 24:
    student=input("Are you student (Yes/No)=").lower()
    if student =="yes":
     Amount=50
    else:
        Amount=100
else :
    Amount=100
print(f"Ticket Cost is {Amount}")



