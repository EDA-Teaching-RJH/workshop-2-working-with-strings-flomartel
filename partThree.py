def main():
    pounds = pounds_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to charge? "))
    charge = pounds * percent
    print(f"Charge £{charge:.2f}")


def pounds_to_float(d):
    poundsvalue = float(d.replace ("£",""))

def percent_to_float(p):
    
    percentvalue = float(p.replace ("%", ""))
    decimal = float(percentvalue/100)

main()
