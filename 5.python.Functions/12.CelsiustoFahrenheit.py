def toFahrenheit(Celsius):
    Fahrenheit=(Celsius*(9/5))+32
    return Fahrenheit
def toCelsius(Fahrenheit):
    Celsius=(Fahrenheit-32)*(5/9)
    return Celsius
Input=int(input("Give the Number="))
A=input("Give the Celsius are Fahrenhit=")
if A=="f":
    print(toFahrenheit(Input))
elif A=="c":
    print(toCelsius(Input))