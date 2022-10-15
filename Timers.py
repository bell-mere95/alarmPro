import tkinter as tk
import sqlite3
from sqlite3 import Error
from tkinter import *
from tkcalendar import *
import time
import os
import sys

# SQL commands:
create_task_table = "CREATE TABLE IF NOT EXISTS tasks (id integer PRIMARY KEY,name text NOT NULL, completed boolean, alarm boolean, due date); "
create_alarm_table = "CREATE TABLE IF NOT EXISTS tasks (id integer PRIMARY KEY,name text NOT NULL, time time, days list, music file); "


def sql_select(t_name):
    sql = "SELECT * FROM %s" % t_name
    return sql


def sql_delete(t_name, column):
    sql = "DELETE FROM %s WHERE %s=?" % (t_name, column)
    return sql


sql_insert_alarm = "INSERT INTO alarms (name, time, days, music) VALUES (?,?,?,?)"
sql_insert_task = "INSERT INTO tasks (name, completed, alarm, due) VALUES (?,?,?,?)"


# Database:


def connection_db(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error:
        print("fail at creation of database")
    return conn


def create_task_table_db(conn):
    try:
        c = conn.cursor()
        c.execute(create_task_table)
    except Error:
        print("fail to create table")
    pass


def create_alarm_table_db(conn):
    try:
        c = conn.cursor()
        c.execute(create_alarm_table)
    except Error:
        print("fail to create table")
    pass


def insert_alarm_db():
    pass


def search_in_db():
    pass


def active_alarm_db():
    pass


# Graphics:


class Logo:
    def __init__(self, w):
        self.master = w
        self.master.geometry('500x500')
        self.master.title('AlarmPro')


class PrintAlarms:
    def __init__(self, w):
        self.master = w
        self.master.geometry('150x500')


class Menu:
    def __init__(self, w):
        self.master = w
        self.master.geometry('400x300')
        self.master.resizable(0, 0)
        self.frame = tk.Frame(self.master)
        self.frame.pack(anchor="center")
        bct = tk.Button(self.frame, text="Create Task", command=self.create_task)
        bca = tk.Button(self.frame, text="Create Alarm", command=self.create_alarm)
        bvt = tk.Button(self.frame, text="View Tasks", command=self.view_tasks)
        bva = tk.Button(self.frame, text="View Alarms", command=self.view_alarms)
        bct.grid(row=0, column=0, padx=40, pady=50)
        bca.grid(row=0, column=1, padx=40, pady=50)
        bvt.grid(row=1, column=0, padx=40, pady=40)
        bva.grid(row=1, column=1, padx=40, pady=40)

    def create_alarm(self):
        self.master.destroy()
        self.master = tk.Tk()
        self.master.resizable(False, False)
        self.master.geometry('400x400')
        hours = StringVar()
        minutes = StringVar()
        time_frame = tk.Frame(self.master)
        time_frame.pack(anchor="center")
        tk.Label(time_frame, text="Time : ").grid(row=0, column=0, padx=40, pady=25)
        tk.Label(time_frame, text=" : ").grid(row=0, column=3, padx=0, pady=25)
        h_spin = tk.Spinbox(time_frame, from_=00, to=23, wrap=True, textvariable=hours, width=2)
        h_spin.grid(row=0, column=2, padx=3, pady=25)
        min_spin = tk.Spinbox(time_frame, from_=00, to=59, wrap=True, textvariable=minutes, width=2)
        min_spin.grid(row=0, column=4, padx=3, pady=25)

    def create_task(self):
        self.master.destroy()
        self.master = tk.Tk()
        self.master.resizable(False, False)

    def view_alarms(self):
        self.master.destroy()
        self.master = tk.Tk()
        self.master.resizable(False, False)

    def view_tasks(self):
        self.master.destroy()
        self.master = tk.Tk()
        self.master.resizable(False, False)


class App:
    def __init__(self, w):
        self.master = w
        Logo(self.master)
        self.master.after(3000, Menu, self.master)


def main():
    root = tk.Tk()
    App(root)
    root.mainloop()
    pass
