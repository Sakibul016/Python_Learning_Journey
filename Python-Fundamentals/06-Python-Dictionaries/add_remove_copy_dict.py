first_dict={
    "name":"sakib",
    "country":"bangladesh",
    "phone": "01742226344"

}
print(first_dict)
first_dict["profession"]="student"    #this is the way to add item in a dectionary. 
print(first_dict)
first_dict.pop("country")  #use pop() function to remove the item from dictionary.
print(first_dict)
last_dict=first_dict.copy() #use copy() function to copy item from another dictionary.
print(last_dict)