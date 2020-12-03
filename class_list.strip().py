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

#Create new class function
def create_new_class(school_name):
    #get class name
    class_name = input('Enter new class name: ')
    add_class_name = open('C:/python/School_management/Schools/'+ school_name + '/class_list.txt','a')
    add_class_name.write('\n'+class_name)
    add_class_name.close()
    #school name se folder create karna hai
    os.mkdir('C:/python/School_management/Schools/'+ '/' + class_name)
    
    print('\nCongratulations,new class'+ class_name +'has been created.')


#Function for class choice
def class_choice(school_name):
    message='''
    -----------------------------------
            School {0}
    -----------------------------------
    1.Create New Class
    2.Choose Existing Class
    3.Exit
    -----------------------------------
    Only enter number:
    ''' .format(school_name)
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
            #print('\nCreate New Class')
            create_new_class(school_name)
        elif option==2:
            print('\nChoose Existing Class')
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
    #os path exists error check
    folder_path = 'C:/python/School_management/Schools/'+school_name
    if os.path.exists(folder_path):
        print('\nThis school'+school_name+'already exists.\nThese are the names of all existing school.\nPlease input the schhol name in which you want to enter.')
    else:
        add_school_name = open('school_list.txt','a')
        add_school_name.write('\n'+school_name)
        add_school_name.close()

        #school name se folder create karna hai
        os.mkdir('C:/python/School_management/Schools/'+school_name)
        print('\nCongratulations,new school'+ school_name +'has been created.')
        #new school create hone ke baad me class ke option ke function ko call karna hai.
        class_choice(school_name)
# Choose school function :yaha se existing school folder ke andar enter honge.     
def choose_school():
    #print('\nChoose Existing School')
    get_school_list_file = open('school_list.txt','r')
    get_schools_in_list = get_school_list_file.readlines()
    print('\nHello Admin,\nExisting school list,\nEnter the number of school in which you want to enter: \n')
    #blank list to get all school names
    school_list_for_options=[]
    #for loop to show nnumber and school name
    for i,name in enumerate(get_schools_in_list , start=1):
        #name.strip()use to remove space of special char.
        print('{} {}'.format(i,name.strip()))
        school_list_for_options.append(name.strip())

    get_school_list_file.close()

    #get school name by admin
    option=int(input('\nEnter school number: '))
    #print('\nAdmin option: ', school_list_for_options[option-1])
    #call choose class options function
    class_choice(school_list_for_options[option-1])


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

