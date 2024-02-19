# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Gustavo Limongi Araujo, 2/19/2024, Assignment06)
#   RRoot,1/1/2030,Created Script
#   <Gustavo L. Araujo>,<02/19/2024>,<Assignment 06>
# ------------------------------------------------------------------------------------------ #
"""
Created on Mon Feb 19 13:25:33 2024

@author: nm108e
"""

import json

class FileProcessor:
    """Processes file data"""

    @staticmethod
    def read_data_from_file(file_name: str):
        """Reads data from a file"""
        try:
            with open(file_name, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
        except Exception as e:
           IO.output_error_messages("Error readding data from file",e)
           data=[]
        return data

    @staticmethod
    def write_data_to_file(file_name: str, data: list):
        """Writes data to a file"""
        try:
            with open(file_name, 'w') as file:
                json.dump(data, file)
        except Exception as e:
            IO.output_error_messages("Error writing data to a file", e)            

class IO:
    """Handles input/output operations"""

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """Displays error messages"""
        print(f"Error: {message}")
        if error:
            print(f"Details: {error}")

    @staticmethod
    def output_menu(menu: str):
        """Displays the program menu"""
        print(menu)

    @staticmethod
    def input_menu_choice():
        """Prompts the user for a menu choice"""
        return input("Enter your choice: ")

    @staticmethod
    def output_student_courses(student_data: list):
        """Displays student data"""
        for student in student_data:
            print(f"Student: {student['first_name']} {student['last_name']} - Course: {student['course']}")

    @staticmethod
    def input_student_data(student_data: list):
        """Prompts the user to enter student data"""
        while True:
            first_name = input("Enter student's first name: ")
            if first_name:
               break
            else:
               print("First name can not be empty")
        while True:
            last_name = input("Enter student's last name: ")
            if last_name:
                break
            else:
                print("Last name can not be empty")
        while True:
           course = input("Enter course name: ")
           if course:
               break
           else:
               print("Course name can not be empty")
        student_data.append({'first_name': first_name, 'last_name': last_name, 'course': course})

# Constants
MENU = """---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
-----------------------------------------"""

FILE_NAME = "Enrollments.json"

# Variables
menu_choice = ''
student_first_name: str = '' 
student_last_name: str = ''  
course_name: str = ''  
student_data: dict = {}  
students: list = []  
csv_data: str = ''  
json_data: str = ''  
file = None  
menu_choice: str  

students = FileProcessor.read_data_from_file(FILE_NAME)

# Main program loop
while menu_choice != '4':
    IO.output_menu(MENU)
    menu_choice = IO.input_menu_choice()

    if menu_choice == '1':
        IO.input_student_data(students)
    elif menu_choice == '2':
        IO.output_student_courses(students)
    elif menu_choice == '3':
        FileProcessor.write_data_to_file(FILE_NAME, students)
        print("Data saved to file.")
    elif menu_choice == '4':
        print("Exiting program...")
    else:
        IO.output_error_messages("Invalid menu choice. Please select a valid option.")
