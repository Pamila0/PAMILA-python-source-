def personal_info_manager():
    person = ("Spy", 19, "Banglamung", "Chonburi")  # name, age, city, country
    hobbies = ["Roblox"]
 
    while True:
        print("1 Display info, 2 Add hobby ,3 Remove hobby,4 Edit age,5 Exit")
        choice = input ("What do you want to do : ")
 
        if choice == "1" :    
            print("Name: ",person[0])
            print("Age: ",person[1])
            print("City: ",person[2])
            print("Country: ",person[3])
           
               
        elif choice == "2":
            hobby = int(input("Insert new hobby : "))
            hobbies.append(hobby)
 
        elif choice == "3":
         del hobbies[0]
 
        elif choice == "4":
            age = input("Insert new age : ")
            person_list = list(person)
            person_list[1] =age
            person = tuple(person_list)
 
 
        elif choice == "5":
            print("Exit :")
            exit(0)
 
        else:
            print("Exit")
            break
 
 
def personal_info_manager():
    person = ("Spy", 19, "Banglamung", "Chonburi")  # name, age, city, country
    hobbies = ["Roblox"]
 
    while True:
        print("1 Display info, 2 Add hobby ,3 Remove hobby,4 Edit age,5 Exit")
        choice = input ("What do you want to do : ")
 
        if choice == "1" :    
            print("Name: ",person[0])
            print("Age: ",person[1])
            print("City: ",person[2])
            print("Country: ",person[3])
           
               
        elif choice == "2":
            hobby = int(input("Insert new hobby : "))
            hobbies.append(hobby)
 
        elif choice == "3":
         del hobbies[0]
 
        elif choice == "4":
            age = input("Insert new age : ")
            person_list = list(person)
            person_list[1] =age
            person = tuple(person_list)
 
 
        elif choice == "5":
            print("Exit :")
            exit(0)
 
        else:
            print("Exit")
            break
if __name__ == "__main__":
    personal_info_manager()
 