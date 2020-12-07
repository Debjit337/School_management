import os

def school_choices():
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

#Class choose
def choose_class(school_name):
    #print('\nChoose Existing School')
    #first get class_list.txt file from school folder
    get_class_list_file = open('School_management/Schools/yo/class_list.txt','r')
    get_classes_in_list = get_class_list_file.readlines()
    print('\nHello Admin,\nExisting class list,\nEnter the number of class in which you want to enter: \n')
    #blank list to get all school names
    class_list_for_options=[]
    #for loop to show nnumber and school name
    #for i,name in enumerate(get_classes_in_list , start=1):
    i=1
    for name in get_classes_in_list:
        #use condition to handle blank
        if bool(name.strip())==True:
            #name.strip()use to remove space of special char.
            print('{} {} class'.format(i,name.strip()))
            i += 1 #for showing continues number in list
            class_list_for_options.append(name.strip())
    get_class_list_file.close()

    #get class name by admin
    #print(class_list_for_options)
    #exit()
    #try & except to handle value error
    try:
        option=int(input('\nEnter class number: '))

    except ValueError:
        print('\nYou have entered wrong input in the place of number.Please do it again with the right input.')
        #call choices function
        class_choices(school_name)
    except NameError:
        print('You have entered alphabet which is wrong input.Please do it again with the right input.')
        #call choices function
        class_choices(school_name)
    except:
        print('There is a problem in the input.Please do it again with the right input.')
        #call choices function
        class_choices(school_name)
    else:    
        #print('\nAdmin option: ', school_list_for_options[option-1])
        #call choose class options function
        class_name = class_list_for_options[option-1]
        #class_choices(school_name)

        #class ke andar details dene ke liye function new
        student_option_in_class(class_name)

#class ke andar details ka function
def student_option_in_class(class_name):
    print('\nHello admin welcome to ', class_name ,'class')

#Function for class choice
def class_choices(school_name):
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
            #print('\nChoose Existing Class')
            choose_class(school_name)
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
        class_choices(school_name)

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
    #try & except to handle value error
    try:
        option=int(input('\nEnter school number: '))

    except ValueError:
        print('\nYou have entered wrong input in the place of number.Please do it again with the right input.')
        #call choices function
        school_choices()
    except NameError:
        print('You have entered alphabet which is wrong input.Please do it again with the right input.')
        #call choices function
        school_choices()
    except:
        print('There is a problem in the input.Please do it again with the right input.')
        #call choices function
        school_choices()
    else:    
        #print('\nAdmin option: ', school_list_for_options[option-1])
        #call choose class options function
        school_name = school_list_for_options[option-1]
        class_choices(school_name)


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
    #call choices function
    school_choices()
except NameError:
    print('You have entered alphabet which is wrong input.Please do it again with the right input.')
    #call choices function
    school_choices()
except:
    print('There is a problem in the input.Please do it again with the right input.')
    #call choices function
    school_choices()
            
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
            #call choices function
            school_choices()

