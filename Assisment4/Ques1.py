total_bill=float(input("Total bill amount ="))
gst=int(input("GST ="))
service_charge=int(input("Service Charge ="))
friend=int(input("Number of friends ="))
final=total_bill+(total_bill*(5/100))+(total_bill*(10/100))
print("Final Bill =",final)
print("Each Person need to Pay =",final/friend)

