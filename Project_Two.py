#Psuedocode
#
#classwork_grade = input("Whats your total class work grade?")/100
#
#homework_grade = input("Whats your total homework grade?")/100
#
#class_participation_grade = int(input("Whats your total class participation grade?"))/100
#
#test_grade = input("Whats your total test grade?")/100
#
#number_of_tests = input("How many tests how you taken thus far?")
#
#test_aim = input("What do you aim to get on your next test?")/100
#
#new_test_grade = number_of_tests/(number_of_tests+1) *(test_grade) + (1/(number_of_tests+1)*test_aim
#
#test_weighting = 0.50
#classwork_weighting = 0.15
#homework_weighting = 0.25
#class_participation_wieghting = .10
#
#total_grade = new_test_grade * test_weighting + classwork_grade * classwork_weighting + homework_grade*homework_weighting + class_participation_grade *class_participation_wieghting
#
#total_grade = total_grade*100
#
#print ("If you got a " + test_aim +" on the next test, your total grade would be " + total_grade + "%")
#



def get_user_input():
    #get the grades for each section and convert them into a decimal
    classwork_grade = int(input("Whats your total class work grade?\n"))/100

    homework_grade = int(input("Whats your total homework grade?\n"))/100

    class_participation_grade = int(input("Whats your total class participation grade?\n"))/100

    test_grade = int(input("Whats your total test grade?\n"))/100

    number_of_tests = int(input("How many tests how you taken thus far?\n"))

    test_aim = int(input("What do you aim to get on your next test?\n"))/100

    #Calculates the new test score based on what the user hopes to get on their next test
    new_test_grade = ((number_of_tests/(number_of_tests+1))*(test_grade)) + ((1/(number_of_tests+1))*(test_aim))

    #The weighting for tests,classwork,hoemwork, and class participation
    test_weighting = 0.50
    classwork_weighting = 0.15
    homework_weighting = 0.25
    class_participation_wieghting = .10

    #Calculates the total grade
    total_grade = ((new_test_grade * test_weighting) + (classwork_grade * classwork_weighting) + (homework_grade*homework_weighting) + (class_participation_grade *class_participation_wieghting))

    #converts back to a integer
    total_grade = int(total_grade*100)

    return test_aim, total_grade

#Print the results
def print_results():
    test_aim, total_grade = get_user_input()
    print ("If you got a " + str(test_aim * 100) +" on the next test, your total grade would be " + str(total_grade) + "%")

print_results()
