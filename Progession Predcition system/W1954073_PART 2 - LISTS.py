#I declare that my work contains no example of misconduct, such as plagiarism, or collusion
#Any code taken from other sources is referenced within my code solution.

#Student ID - w1954073 / 20220741 
#Date - 25/11/2022

Progress= 0
Trailer= 0
Retriever= 0
Excluded = 0
Total =0


Module_Progression=[]             
    
def credit_input(number_of_credits):
    while True:
        try:
            credit= int(input(number_of_credits))
                
        except ValueError:
            print('Integer required \n')# B. validation (If user inputs a value in the wrong data type, 'Integer required' error message will be printed.)
            continue

        try:
            if credit not in range(0,121) or credit% 20 != 0:
                print('out_of_range \n') # B. validation (Checks whether the credits are in the correct range.)
                continue
        except:
             break       
             
        break
    return credit

           
while True:
    

    credits_to_pass= credit_input('\nEnter the number of credits to pass:')
    
    credits_to_defer= credit_input('Enter the number of credits to Defer:')
    
    credits_to_fail= credit_input('Enter the number of credits to fail:')
    
    

    if credits_to_pass + credits_to_defer + credits_to_fail == 120: # B. validation (Checks whether the total of the credits entered in equal to 120)
        
        if credits_to_pass == 120:# A.Outcomes
            progression_outcome = 'Progress'
            Progress += 1
            Total+=1
            
        elif credits_to_pass == 100:
            progression_outcome = 'Progress(module trailer)'
            Trailer += 1
            Total+=1
            
        elif credits_to_fail == 80 or credits_to_fail == 100 or credits_to_fail == 120: 
            progression_outcome = 'Exclude'
            Excluded+=1
            Total+=1
               
        else:  
            progression_outcome = 'Do not progress - module retriever'
            Retriever+=1
            Total+=1
    else:
        print('Total incorrect','\n')
        continue
    
    Module_Progression.append([progression_outcome, credits_to_pass , credits_to_defer , credits_to_fail,])

    print(progression_outcome)
    
    while True:
        option=input("\nWould you like to enter another set of data?\nEnter 'Y' for yes or 'q' to quit and view results:")
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

#Histogram
        
print("\n")
print('Histogram')
print('........................................................')
print('Progress',Progress,':',Progress*'*')
print('Trailer',Trailer, ':', Trailer*'*')
print('Retriever',Retriever, ':',Retriever *'*')
print('Excluded',Excluded,':', Excluded*'*' , '\n')
print(Total,'Outcomes in Total')
print('........................................................','\n')


# Lists

for i in Module_Progression:
    print(f'{i[0]} - {i[1]} , {i[2]} , {i[3]}')        
      
              

    


