Month = int(input("ENTER THE MONTH:"))
Day = int(input("ENTER THE DAY:"))
Year = int(input("ENTER THE YEAR:"))

if 1<= Month <=12 :
    Month += 1
else:
    print("Invalid month")
    if 1<= Day <=31 :
        Day += 1
    else:
        print("Invalid Day")
        if 1800 <= Year <=2025:
            Year += 1
        else:
            print("Invalid Year")

            print("Next Day :-", Day , "/",Month,"/", Year )


