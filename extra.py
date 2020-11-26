import os

def choices():
    message='''
    -----------------------------------
                welcome Admin
    -----------------------------------
    1.Create New School
    2.Choose Existing School
    3.Exit
    -----------------------------------
    Only enter number:
    ''' 
    try:
        option=int(input(message))
    except ValueError:
        print('\nYou have entered wrong input in the place of number.Please do it again with the right input.')
    except NameError:
        print('You have entered alphabet which is wrong input.Please do it again with the right input.')
    except:
        print('There is a problem in the input.Please do it again with the right input.')            
    else:     
        if option==1:
            print('\nCreate New School')
        elif option==2:
            print('\nChoose Existing School')
        elif option==3:
            print('\nYou have successfully Exited.')
        else:    
            print('You have entered wrong ipuut.Please do it again with the right input.')

# Create new school function:yaha par ek school ke name se folder create hoga and school ka name ek school_list.txt 
# me addon hoga. 
def create_new_school():
    #print('\nCreate New School')
    #get school name
    school_name = input('Enter new school name: ')
    #school name se folder create karna hai
    os.mkdir('C:/python/School_management/Schools/'+school_name)
    
# Chhose school function :yaha se existing school folder ke andar enter honge.     
def choose_school():
    print('\nChoose Existing School')


message='''
    -----------------------------------
                welcome Admin
    -----------------------------------
    1.Create New School
    2.Choose Existing School
    3.Exit
    -----------------------------------
    Only enter number:
    '''
try:
    option=int(input(message))
except ValueError:
    print('\nYou have entered wrong input in the place of number.Please do it again with the right input.')
except NameError:
    print('You have entered alphabet which is wrong input.Please do it again with the right input.')
except:
    print('There is a problem in the input.Please do it again with the right input.')            
else:     
    if option==1:
            #print('\nCreate New School')
            create_new_school()
    elif option==2:
            #print('\nChoose Existing School')
            choose_school()
    elif option==3:
            print('\nYou have successfully Exited.')
    else:    
            print('You have entered wrong ipuut.Please do it again with the right input.')
