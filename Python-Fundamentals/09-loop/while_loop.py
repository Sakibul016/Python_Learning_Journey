i=1
while i<9:
    i +=1
    """if i == 3:
        break  # break is used to stop the loop at that point."""
    if i in (3,5):
        continue # continue is used to run the code according to the condition except that if condition number .
    print(i)
else: #The else block will NOT be executed if the loop is stopped by a break statement.
    print(" i is no longer less than 9 ")
    # always remember , result will be differnet based on using increment before and after print function.
