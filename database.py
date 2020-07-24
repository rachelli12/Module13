"""
Program: database.py
Author: Rachel Li
Last date modified: 07/14/2020

The purpose of this program is to use query to read database
"""
import sqlite3
from sqlite3 import Error


def create_connection(db):
    """ Connect to a SQLite database
    :param db: filename of database
    :return connection if no error, otherwise None"""
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as err:
        print(err)
    return None

def create_table(conn, sql_statement):
    try:
        c = conn.cursor()
        c.execute(sql_statement)
    except Error as error:
        print(error)

def create_tables(database):
    '''
    :param database: database object
    :return: return tables in database
    '''
    sql_create_person_table = """ CREATE TABLE IF NOT EXISTS person (
                                        id INTEGER PRIMARY KEY,
                                        firstname TEXT NOT NULL,
                                        lastname TEXT NOT NULL
                                    ); """

    sql_create_student_table = """CREATE TABLE IF NOT EXISTS student (
                                    id INTEGER PRIMARY KEY,
                                    major TEXT NOT NULL,
                                    begin_date TEXT NOT NULL,
                                    end_date TEXT,
                                    FOREIGN KEY (id) REFERENCES person (id)
                                );"""

    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_person_table)
        # create tasks table
        create_table(conn, sql_create_student_table)
    else:
        print("Unable to connect to " + str(database))


def create_person(conn, person):
    """Create a new person for table
    :param conn:
    :param person:
    :return: person id
    """
    sql = ''' INSERT INTO person(firstname,lastname)
              VALUES(?,?); '''
    cur = conn.cursor()  # cursor object
    cur.execute(sql, person)
    return cur.lastrowid # returns the row id of the cursor object, the person id


def create_student(conn, student):
    """Create a new person for table
    :param conn:
    :param student:
    :return: student id
    """
    sql = ''' INSERT INTO student(id, major, begin_date)
              VALUES(?,?,?); '''
    cur = conn.cursor()  # cursor object
    cur.execute(sql, student)
    return cur.lastrowid # returns the row id of the cursor object, the student id

def select_all_persons(conn):
    """Query all rows of person table
    :param conn: the connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM person;")

    rows = cur.fetchall()

    return rows # return the rows

def select_all_students(conn):
    """Query all rows of person table
    :param conn: the connection object
    :return:
    """
    sql_statement = "SELECT * FROM student;"
    cur = conn.cursor()
    cur.execute(sql_statement)
    rows = cur.fetchall()

    return rows # return the rows

def get_person_id(conn, firstname, lastname):
    '''
    :param conn: connection object
    :param firstname: this represents person first name
    :param lastname: this represents person last name
    :return: person_id
    '''
    sql_statement = """SELECT id FROM person
                        WHERE firstname = ?
                        AND lastname = ?;"""
    person = (firstname, lastname)
    c = conn.cursor()
    c.execute(sql_statement, person)
    id = cursor.fetchone()
    if id is None:
        return id[0]
    else:
        return id

