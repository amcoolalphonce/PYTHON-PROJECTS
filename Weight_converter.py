weight = int(input("Enter your weight: "))
unit = input("(K)gs or (L)bs ")
if unit.upper() == "L":
    converted_weight = weight*0.45
    print(f" Your weight is: {converted_weight} kilos" )
else:
    converted_weight = weight/0.45
    print(f'Your weight is : {converted_weight} pounds')