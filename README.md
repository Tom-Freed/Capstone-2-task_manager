# Capstone 2: task_manager

## Description
- A Python program to manage and assign tasks to team members

## Installation
- Download task_manger.py, tasks.txt and user.txt
- Run task_manager.py

## Usage
- Log into program using the username and password in user.txt
- The following menu will appear:

  ![image](https://user-images.githubusercontent.com/91968539/219952609-1507ce41-4e91-4bfd-8c08-2f46453773eb.png)
  - If not logged in as 'admin': 'r  - Register a user' and 's  - View statistics' will not be visable or accessible
- r  - Register a user
  - Input new username and password, these will be appended to user.txt
- s  - View statistics
  - Will display the total number of users and total number of tasks
- a  - Add a task
  - Input the username, title, description and due date for the task
  - These will be appended to tasks.txt (along with 'assigned_date' - todays date and 'No' - i.e. the task is not complete
- va - View all tasks
  - Displays all tasks in easy to read format
- vm - View my task
  - Displays tasks assigned to the logged in user in easy to read format
- e  - Exit
  - Exits the program
