# su20-hw-01a


# display title
print("Miles Per Gallon (MPG) program")
print()

# get input from the user
miles_driven = float(input("Enter miles driven: \t\t"))
gallons_used = float(input("Enter gallons of gas used: \t"))
cost_gallon = float(input("Enter cost per galon: \t\t"));

                
# calculate and round miles per gallon
miles_per_gallon = miles_driven / gallons_used
miles_per_gallon = round(miles_per_gallon, 2)
total_gas_cost = round(gallons_used*cost_gallon, 2);
cost_per_mile = round(total_gas_cost/miles_driven, 2);

# display the result
print()
print("Miles Per Gallon:\t\t" + str(miles_per_gallon))
print("Total Gas Cost:\t\t\t" + str(total_gas_cost));
print("Cost Per Mile:\t\t\t" + str(cost_per_mile));
print()
print('End of Program.')

