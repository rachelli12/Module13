"""
Program: database_gui.py
Author: Rachel Li
Last date modified: 07/18/2020

The purpose of this program is to use database with GUI
"""
import tkinter as t
import database as db
from database import *


class GUI(t.Tk):
    DATABASE = 'assignment.db'
    def __init__(self):
        t.Tk.__init__(self)
        self.title("Database with GUI")

        self.button_create_database = t.Button(self, text='Create Database and Table', command=self.create_database)
        self.button_create_database.grid(row=1)

        self.first_name_label = t.Label(self, text='First Name').grid(row=2, column=0)
        self.first_name_enter = t.Entry(self)
        self.first_name_enter.grid(row=2, column=1)

        self.last_name_label = t.Label(self, text='Last Name').grid(row=3, column=0)
        self.last_name_enter = t.Entry(self).grid(row=3, column=1)

        self.major_label = t.Label(self, text='Major').grid(row=4, column=0)
        self.major_enter = t.Entry(self).grid(row=4, column=1)

        self.start_date_label = t.Label(self, text='Start date').grid(row=5, column=0)
        self.start_date_enter = t.Entry(self).grid(row=5, column=1)

        self.add_student_button = t.Button(self, text='Add Student', command=self.add_student).grid(row=6, column=0)
        self.add_person_button = t.Button(self, text='Add Person', command=self.add_person).grid(row=6, column=1)
        self.view_student_button = t.Button(self, text='View Student', command=self.view_student).grid(row=7, column=0)
        self.view_person_button = t.Button(self, text='View Person', command=self.view_person).grid(row=7, column=1)

        self.exit_button = t.Button(self, text="Exit", width=10, command=self.destroy).grid(row=8, column=0)

    def create_database(self):
        '''
        :return: tables in database
        '''
        create_tables(self.DATABASE)

    def add_person(self):
        '''
        :return: person in database
        '''
        conn = create_connection(self.DATABASE)
        with conn:
            person = (self.first_name_enter.get(), self.last_name_enter.get())
            create_person(conn, person)

    def view_person(self):
        '''
        :return: view person
        '''
        conn = create_connection(self.DATABASE)
        persons = select_all_persons(conn)
        for person in persons:
            print(person)

    def add_student(self):
        '''
        :return: add student to database
        '''
        conn = create_connection(self.DATABASE)
        with conn:
            person_id = get_person_id(conn, self.first_name_enter.get(), self.last_name_enter.get())
            if person_id is None:
                person = (self.first_name_enter.get(), self.last_name_enter.get())
                person_id = create_person(conn, person)
            student = (person_id, self.major_enter.get(), self.start_date_enter.get())
            create_student(conn, student)

    def view_student(self):
        '''
        :return: view student in database
        '''
        conn = create_connection(self.DATABASE)
        students = select_all_students(conn)
        for student in students:
            print(student)


if __name__ == '__main__':
    gui = GUI()
    gui.mainloop()
