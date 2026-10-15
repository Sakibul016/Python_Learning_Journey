month=2
day=3
match day:
    case 1|2|3|4|5|6 if month==1:
        print("January weekday")
    case 1|2|3|4|5|6 if month==2:
        print("February weekday")
    case _:
        print("Onno mas er din")

        #the same code we can write it using if elif else .
        """ month=2
        day=2 
        if day in (1,2,3,4,5,6) and month==1 :
            print("This is January weekday")
            elif day in (1,2,3,4,5,6) and month== 2:
                print("This is February weekday.")
                else:
                    print("HOllyday for me.")"""