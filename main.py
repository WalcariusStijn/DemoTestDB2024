from services.CategoryService import CategoryService

def main():
    print("Welcome administrator! Manage your categories here.")
    print('Select an option: C=Create, R=Read, R+=Read with products, U=Update, D=Delete, S=Search, X=Exit ')
    choice = ""

    while(choice.upper() != 'X'):
        print("---------------------------------------------------------------------")
        choice = input('Choose an option [C,R,R+,U,D,S,X]:> ')

        if choice.upper() == 'C':
            name = input('Enter a new category name: ')
            pass
         
        elif (choice.upper() == 'R') :
            CategoryService.print_all_categories()

        elif choice.upper() == 'R+':
             pass
             
        elif choice.upper() == 'S':
            id = int(input('Enter a categorynumber: '))             
            pass
    
        elif choice.upper() == 'U':
            id = int(input('Enter a categorynumber: '))
            pass
    
        elif choice.upper() == 'D':
            id = (input('Enter a categorynumber: '))
            pass
    
        elif choice.upper()== 'X':
            print("Closing application. Bye!")
        
        else:
            choice =""
            print("Invalid choice, try again.")

####  main function ########################################################
main()