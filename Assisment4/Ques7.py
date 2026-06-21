run,over=map(float,input("Enter total run and total over").split())
rmg_ball=over-int(over)
balls = int(over)*6+rmg_ball*10
run_rate=run/over
print("Run rate :",run_rate)
print("Balls :",balls)
