#I declare that my work contains no example of misconduct, such as plagiarism, or collusion
#Any code taken from other sources is referenced within my code solution.

#Student ID - w1954073 / 20220741 
#Date - 09/12/2022


creditss = {}

   

   
              
    
def credit_input(number_of_credits):
    while True:
        try:
            credit= int(input(number_of_credits))
                
        except ValueError:
            print('Integer required')#If user inputs a value in the wrong data type, 'Integer required' error message will be printed.
            continue

        try:
            if credit not in range(0,121) or credit% 20 != 0:
                print('out_of_range')
                continue
        except:
             break
        
             
        break
    return credit

       
    
while True:
    Student_ID = input('\nEnter the Student ID:')

    credits_to_pass= credit_input('\nEnter the number of credits to pass:')
    
    credits_to_defer= credit_input('Enter the number of credits to Defer:')
    
    credits_to_fail= credit_input('Enter the number of credits to fail:')
    
    

    if credits_to_pass + credits_to_defer + credits_to_fail == 120: 
        if credits_to_pass == 120:
                                    
            creditss[Student_ID] = "Progress-",credits_to_pass,credits_to_defer,credits_to_fail
            
            
        elif credits_to_pass == 100:
            
            creditss[Student_ID] = "Progress(module trailer)-",credits_to_pass,credits_to_defer,credits_to_fail
            
            
        elif credits_to_fail == 80 or credits_to_fail == 100 or credits_to_fail == 120:
            
            
            creditss[Student_ID] = "Exclude-",credits_to_pass,credits_to_defer,credits_to_fail
            
               
        else:
            
            creditss[Student_ID] = "module retriever-",credits_to_pass,credits_to_defer,credits_to_fail
            
    else:
        print('Total incorrect','\n')
        continue

    while True:
        option=input("\nWould you like to enter another set of data?\nEnter 'Y' for yes or 'q' to quit and view the Dictionary:")
        if option == 'y':
            break
         
        elif option == 'q':
            break
                
        else:
            print('Invalid option!!Please re-enter','\n')
            continue
   
    
    if option == 'q':
         break
    else:
         continue
 
print("\n")
print(creditss)
     
    
        
       

    


