#!/usr/bin/env python
# coding: utf-8

# In[1]:


import datetime                 #package for D.o.B
from tabulate import tabulate   #package for table

player_data = []                #stores player_data
overall_ratings = {}            #stores overall_ratings
salary_ranges = {}              #stores salary_ranges
player_ages = {}                #stores player_ages

def range(inside):                                                                       #function for debugging skill range
    while True:                                                                          #while loop
        skill = input(inside)                                                            #skill is equal to input of user
        if skill.isdigit() and 0 <= float(skill) <= 5:                                   #only accepts number within 0 and 5
            return float(skill)                                                          #returns number
        else:                                                                            #otherwise
            print("The rating you entered was invalid.")                                 #loops you back with error message

def num_player_id():                                                                     #function for player ID
    while True:                                                                          #while loop
        player_id = input("\nEnter player's ID (2-digit num) or 'end' to finish: ")      #input choice for user
        if player_id.lower() == "end":                                                   #if user types 'end'
            return "end"                                                                 #programme ends
        elif len(player_id) != 2 or not player_id.isdigit():                             #if length is not equal to 2 (above 2 digits)
            print("The ID you entered was invalid.")                                     #error message looping back
        else:                                                                            #otherwise
            return player_id                                                             #will print the player ID
               
def check_date_of_birth():                                                               #function name
    while True:                                                                          #while loop
        dob = input("Enter player's date of birth (YYYY-MM-DD): ")                       #input D.o.B with ISO format
        try:                                                                             #use this within
            datetime.datetime.strptime(dob, '%Y-%m-%d')                                  #package specifically used
            return dob                                                                   #returns D.o.B
        except ValueError:                                                               #else
            print("The date you entered was invalid. Please use the format YYYY-MM-DD.") #loops back with error message
              
def calculate_rating():                                                                  #function for skills
    a = range("Enter Their Speed Stats (0-5): ")                                         #speed variable
    b = range("Enter Their Shooting Stats (0-5): ")                                      #shooting variable
    c = range("Enter Their Passing Stats (0-5): ")                                       #passing variable
    d = range("Enter Their Defending Stats (0-5): ")                                     #defending variable
    e = range("Enter Their Dribbling Stats (0-5): ")                                     #dribbling variable
    f = range("Enter Their Physicality Stats (0-5): ")                                   #physicality variable
  
    overall_rating = (a + b + c + d + e + f) * 100 / 30                                  #calculation for overall rating
    return overall_rating                                                                #returns value

def calculate_salary(overall_rating):                                                    #function for salary
    salary_values = [1000, 700, 500, 400]                                                #array used for salary

    if overall_rating >= 80:                                                             #if greater than 80
        return [salary_values[0]]                                                        #Return 1000
    elif 60 < overall_rating < 80:                                                       #if greater than 60 and less than 80
        return [salary_values[0], salary_values[1]]                                      #Return 1000, 700
    elif overall_rating == 60:                                                           #if equal to 60
        return [salary_values[1]]                                                        #Return 700
    elif 45 < overall_rating <= 60:                                                      #if greater than 45 but less than 60
        return [salary_values[1], salary_values[2]]                                      #Return 700, 500
    elif overall_rating == 45:                                                           #if equal to 45
        return [salary_values[2]]                                                        #Return 500
    elif 30 < overall_rating <= 45:                                                      #if greater than 30 but less than 45
        return [salary_values[2], salary_values[3]]                                      #Return 500, 400
    else:                                                                                #anything below 30
        return [salary_values[3]]                                                        #Return 400
        
def calculate_age(date_of_birth):                                                        #function used for calculating age
    dob = datetime.datetime.strptime(date_of_birth, '%Y-%m-%d').date()                   #datetime package
    today = datetime.date.today()                                                        #uses precise time
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))      #formula to calculate age
    return age                                                                           #prints age

def display_table():                                                                                #table function
    sum_table = []                                                                                  #empty data for sum of all table headers
    for player_id, player_name, dob, overall_rating in sorted(player_data, key=lambda x: x[0]):     #sorts the data
        
        age = str(player_ages.get(player_id, '')).strip()                                           #age corresponding to player ID
        
        salary_range = salary_ranges.get(player_id, '')                                             #Get salary range corresponding to player's ID
        sum_table.append([player_id, player_name, dob, age, overall_rating, salary_range])          #sum of table 

    headers = ["UID", "Name", "D.o.B", "Age", "Score", "Salary Range"]                              #headers for table
    return tabulate(sum_table, headers=headers)                                                     #Return the summary table as a string
                                                        
def main():                                                                                         #main function
    count = 0                                                                                       #counter set to 0
    while count < 3:                                                                                #Loop to input only three players
        player_id = num_player_id()                                                                 #calling function
        if player_id.lower() == "end":                                                              #if player id is called above 3 times programme ends
            break                                                                                   #exits loop

        player_name = input("Enter player's name: ")                                                #input players names
        date_of_birth = check_date_of_birth()                                                       #calls function
        age = calculate_age(date_of_birth)                                                          #calls the age ready for print
        overall_rating = calculate_rating()                                                         #calls overall rating function
        salary_indices = calculate_salary(overall_rating)                                           #salary function

        player_data.append((player_id, player_name, date_of_birth, overall_rating))                 #adding values to player_data
        
        overall_ratings[player_id] = overall_rating                                                 #overall rating from player ID
        salary_ranges[player_id] = ' '.join(map(str, salary_indices))                               #salary from player ID
        player_ages[player_id] = age                                                                #age from player ID

        print("This Player's ID Is: ", player_id)                                                   #prints player_ID
        print("This Player's Name Is: ", player_name)                                               #prints player name
        print("This Player's D.o.B Is ", date_of_birth)                                             #prints D.o.B
        print("This Player's Age Is: ", age)                                                        #prints age
        print("This Player's Score Is: ", overall_rating)                                           #prints player score
        print("This Player's Overall Rating Is: ", round(overall_rating))                           #prints overall rating
        print(f"This Player's Salary Range Is: {' '.join(map(str, salary_indices))}")               #prints salary 

        
        summary = display_table()                                                                   #displays summary of table
        print(summary)                                                                              #prints summary
        
        count += 1                                                                                  #counter increasing by 1      
    
def save_files(sum_table):                                                                          #function for saving files
    file_path = "players.txt"                                                                       #file name
    with open(file_path, "w") as file:                                                              #file path opening
        file.write(sum_table)                                                                       #writes this after the table
    print(f"\nSummary saved to {file_path}")                                                        #prints this message
    
    
import datetime                                                                                     #package for D.o.B
from tabulate import tabulate                                                                       #package for table
            
player_data = []                                                                                    # stores player_data
overall_ratings = {}                                                                                # stores overall_ratings
salary_ranges = {}                                                                                  # stores salary_ranges
player_ages = {}                                                                                    # stores player_ages

def advanced(file_name):                                                                            #function for advanced with variable file_name inside
    try:                                                                                            #trying to run the code below
        
        with open(file_name, 'r') as file:                                                          #opens the file specified in file_name for reading
            next(file)                                                                              #skips this line 
            for line in file:                                                                       #goes through the following code
                data = line.strip().split(', ')                                                     #removes any white spaces or splits in code
                player_id = data[0]                                                                 #individual data elements in code
                player_name = data[1]                                                               #individual data elements in code
                date_of_birth = data[2]                                                             #individual data elements in code
                speed = float(data[3])                                                              #individual data elements in code
                shooting = float(data[4])                                                           #individual data elements in code
                passing = float(data[5])                                                            #individual data elements in code
                defending = float(data[6])                                                          #individual data elements in code
                dribbling = float(data[7])                                                          #individual data elements in code
                physicality = float(data[8])                                                        #individual data elements in code
                
                overall_rating = (speed+ shooting+ passing+ defending+ dribbling+ physicality)*100/30       #calculation for rating
                salary_indices = calculate_salary(overall_rating)                                           #calls salary function 
                player_data.append((player_id, player_name, date_of_birth, overall_rating))                 #appends to player_data list
                overall_ratings[player_id] = overall_rating                                                 #updates dictionaries
                salary_ranges[player_id] = ' '.join(map(str, salary_indices))                               #updates dictionaries
                player_ages[player_id] = calculate_age(date_of_birth)                                       #updates dictionaries
                      
 
        summary = display_table()                                                                           #displays table
                  
        file_path = "advanced_summary.txt"                                                                  #assigns the string for where it will be saved
        with open(file_path, "w") as output_file:                                                           #opens the file for writing to handle the data in the file
            output_file.write(summary)                                                                      #displays the generated summary in the file
        print(f"\nSummary saved to {file_path}")                                                            #states the string with file_path
        return summary                                                                                      #returns the generated summary

    except FileNotFoundError:                                                                               #error message
        print("File not found!")                                                                            #prints this

if __name__ == "__main__":                                                                                  #checks if it is being run
    main()                                                                                                  #the function for main to be called
    summary = display_table()                                                                               #displays summary of table
    print(summary)                                                                                          #prints summary
    save_files(summary)                                                                                     #prints the save files (function)

    advanced_summary = advanced("PlayerData1.txt")                                                          #prints the text in the string
    print(advanced_summary)                                                                                 #finally printing the function


#  

# In[27]:





# 

# In[38]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




