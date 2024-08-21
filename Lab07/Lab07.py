#from cs1033_evaluator import evaluate_lab7,evaluate_lab7()  
#These are used to evaluate the code in moodle so run this code in any other platform dont need these 

from datetime import datetime
from cs1033_evaluator import evaluate_lab7

def days_to_birthday(date):
    '''
    Calculates the number of days that have passed since the 1st of January 
    to the given date.

    :param date: A date string in the format of yyyy-mm-dd
    :return: The number of days to the date from 1st of January 
             (eg: date->2021-01-01, return->1)
    '''

    # Convert the date string to a datetime object
    datetime_object = datetime.strptime(date, "%Y-%m-%d")

    # Extract only the date and remove the timestamp
    date = datetime_object.date()

    # Find the number of days since the begining of the year
    num_days = date.timetuple().tm_yday

    return num_days


# Please do not edit anything above this line.
################################################################################


#Get the input as text file
file=input()
#Creating a file to store Name and Id
output=open("output.txt",'w')
#Reading the file 
with open(file,'r') as fl:
    input_details=[]
    #Creating a list with the details that got from the source file 
    for i in fl:
        input_details.append(i.split())
    c_year=[]
    #itterating through the created list
    for j in input_details:
        year=j[1][0:4]
        c_year.append(year)
        if j[2]=="M":
            day=days_to_birthday(j[1])
            while len(str(day))!=3:
                day=str(0)+str(day)
        else:
            #we have to add 500 for Female
            day=days_to_birthday(j[1])+int(500)
        
        no=str(c_year.count(year))
        #Adding zero when length is not enough as mentioned
        while len(no)!=3:
            no=str(0)+no
        
        id=str(year)+str(day)+str(no)
        #Writing the final file 
        #Name=j[0]
        output.write(str(j[0])+" "+id+"\n")
output.close()
            
        
################################################################################
# Please do not edit anything below this line.
evaluate_lab7()

##################### End of the programme #####################################
