#=====importing libraries===========
'''This is the section where you will import libraries'''
from datetime import datetime

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''
while True:
    # Take user inputs
    username = input("Username: ")
    password = input("Password: ")

    # Opens user.txt file and creates a dictionary of each username and password
    with open("user.txt", 'r', encoding='utf-8') as f:
        user_data = f.readlines()
        logins = {}
        for line in user_data:
            split_user = line.split(', ')
            # .strip() to remove '\n' added when new user registered
            logins.update({split_user[0]: split_user[1].strip()})

        # Checks if username is a key in logins and checks if password is the associated value
        if username in logins.keys() and password == logins[username]:
            break
        else:
            # Error message if either the username or password are incorrect
            print("Username or password incorrect, please enter a valid username and password")

#====Menu Section====
while True:
    # To display extra menu options if user is admin, otherwise display norm_menu
    norm_menu = '''
a  - Add a task
va - View all tasks
vm - View my task
e  - Exit
: '''
    admin_menu = '''
r  - Register a user
s  - View statistics'''

    if username == 'admin':
        user_menu = admin_menu + norm_menu
    else:
        user_menu = norm_menu

    # presenting the menu to the user and
    # making sure that the user input is converted to lower case.
    menu = input("Select one of the following options:" + user_menu).lower()

    # Creating a break line variable which can be used throughout the program
    break_line = "—" * 100

#====Register new user====
    if menu == 'r' and username == 'admin':
        while True:
            # Take user inputs
            new_user = input("Please enter the new username: ")
            new_pass = input("Please enter the new password: ")
            confirm_pass = input("Please confirm the new password: ")

            # If the passwords match append user.txt with the new name and password
            if new_pass == confirm_pass:
                with open("user.txt", 'a', encoding='utf-8') as f:
                    f.write(f"\n{new_user}, {new_pass}")
                    # Prints successful registration message and a line break
                    print(f"{break_line}\nRegistration successful.\n{break_line}")
                    break

            # If the passwords do not match ask the user if they would like to exit or try again
            else:
                again = input('''The new password and confirmation password did not match. 
Please enter 'e' to exit this section or any key to try again: ''').lower()
                if again == 'e':
                    break
                else:
                    pass

        '''In this block you will write code to add a new user to the user.txt file
        - You can follow the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise you present a relevant message.'''

#====View statistics====
    # If the user is 'admin' open user.txt and tasks.txt and store the number of entries
    elif menu == 's' and username == 'admin':
        with open("user.txt", "r", encoding='utf-8') as f:
            user_stats = f.readlines()
        with open("tasks.txt", "r", encoding='utf-8') as f:
            task_stats = f.readlines()
        # Print the number of entries from each txt file with break lines
        print(f'''{break_line}
User and task statistics are as follows:
Total number of users: {len(user_stats)}
Total number of tasks: {len(task_stats)}
{break_line}''')

#====Add new task====
    elif menu == 'a':
        # Take user's inputs
        task_user = input("Please enter the username of the person the task is assigned to: ")
        task_title = input("Please enter the title of the task: ")
        task_description = input("Please enter a description of the task: ")
        task_due_date = input("Please enter the due date of the task in the format dd mmm yyyy: ")

        # Find today's date and store in dd,mmm,yyyy format
        today_date = datetime.today()
        assigned_date = today_date.strftime("%d %b %Y")

        # Write user input's, assigned date and 'No' to tasks.txt
        with open("tasks.txt","a", encoding='utf-8') as f:
            f.write(f"\n{task_user}, {task_title}, {task_description}, {assigned_date}, {task_due_date}, No")

        # Confirm to user the task has been added
        print(f"\nTask successfully added.\n{break_line}")

        '''In this block you will put code that will allow a user to add a new task to task.txt file
        - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''

#====View all tasks====
    elif menu == 'va':
        # Open tasks.txt and reads each line
        with open("tasks.txt","r", encoding='utf-8') as f:
            data = f.readlines()

            # Splits each item in line of the tasks.txt and prints the data in an easy to read format
            output = ""
            for line in data:
                split_data = line.split(", ")
                # split_data[5].strip() used as some entries had '\n' at the end
                output += f'''{break_line}
Assigned to:     {split_data[0]}
Task:            {split_data[1]}
Date assigned:   {split_data[3]}
Due date:        {split_data[4]}
Task complete:   {split_data[5].strip()}
Task description: 
 {split_data[2]} 
'''
            # Add dividing line to last task and print the tasks
            output += break_line
            print(output)
            
        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 
            - It is much easier to read a file using a for loop.'''

#====View my tasks====
    elif menu == 'vm':
        # Open tasks.txt and reads each line
        with open("tasks.txt", "r", encoding='utf-8') as f:
            data = f.readlines()

            # Splits each item in line of the tasks.txt and prints the data in an easy to read format
            output = ""
            for line in data:
                split_data = line.split(", ")
                # Checks if the task is assigned to the logged in username
                if split_data[0] == username:
                    # split_data[5].strip() used as some entries had '\n' at the end
                    output += f'''{break_line}
Assigned to:     {split_data[0]}
Task:            {split_data[1]}
Date assigned:   {split_data[3]}
Due date:        {split_data[4]}
Task complete:   {split_data[5].strip()}
Task description: 
 {split_data[2]} 
'''
            # If there are no tasks assigned to the username a message is printed, otherwise the assigned tasks are printed
            if len(output) == 0:
                print(f"{break_line}\nNo tasks are assigned to your username.\n{break_line}")
            else:
                # Add dividing line to last task and print the task(s)
                output += break_line
                print(output)

        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same print it in the format of Output 2 in the task PDF'''

#====Exit====
    elif menu == 'e':
        print(f'{break_line}\nGoodbye!!!\n{break_line}')
        exit()

#====Error message====
    else:
        print(f"{break_line}\nYou have made an incorrect choice, please try again\n{break_line}")