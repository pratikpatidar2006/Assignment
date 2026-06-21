total_ed= int(input("Enter total event duration"))
hours = total_ed/3600   //3672   1
total_ed=total_ed%3600  //72
minutes=total_ed/60     //1
total_ed=total_ed%60    //12
seconds=total_ed        

print("Hours :",hours)
print("Minutes :",minutes)
print("Seconds :",seconds)