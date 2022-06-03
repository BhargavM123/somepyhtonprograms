import psycopg2
import tkinter  as tk
from tkinter import *

my_w = tk.Tk()
my_w.geometry("450x350")
global i

#connect to the db
con = psycopg2.connect(
            host = "localhost",
            database="helloBM_1",
            user = "postgres",
            password = "@Bhargav1")

#cursor
cur = con.cursor()

# cur.execute("insert into project values (%s, %s, %s, %s,%s)", ('5a', 'EVbatteries', 3444,'india','RoyalEnfield'))
# cur.execute("delete from project where proj_name='haaanoob'")
#execute query
cur.execute("select proj_name,country,client_name from project")

rows = cur.fetchall()

for r in rows:
    print (f"name: {r[0]}  client {r[2]}")



def display():
    cur.execute("SELECT * FROM project")
    my_cursor = cur.fetchall()
    global i
    i = 0
    for project in my_cursor:
        for j in range(len(project)):
            e = Label(my_w, width=10, text=project[j],
                      relief='ridge', anchor="w")
            e.grid(row=i, column=j)
            # e.insert(END, student[j])
        e = tk.Button(my_w, width=5, text='Edit', relief='ridge',
                      anchor="w", command=lambda k=project[0]: edit_data(k))
        e.grid(row=i, column=5)
        i = i + 1

display()


def edit_data(id):  # display to edit and update record
    global i  # start row after the last line of display
    # collect record based on id and present for updation.
    row = cur.execute("SELECT * FROM project WHERE proj_id=%s", [id])
    s = cur.fetchone()  # row details as tuple

    e1_str_id = tk.StringVar(my_w)  # String variable
    e2_str_name = tk.StringVar(my_w)
    e3_str_client = tk.StringVar(my_w)
    e4_str_country = tk.StringVar(my_w)
    e5_str_budget = tk.IntVar(my_w)

    e1_str_id.set(s[0])  # id is stored
    e2_str_name.set(s[1])  # Name is stored
    e5_str_budget.set(s[2])
    e4_str_country.set(s[3])
    e3_str_client.set(s[4])# class is stored



    e1 = tk.Entry(my_w, textvariable=e1_str_id, width=10)
    e1.grid(row=i, column=0)
    e2 = tk.Entry(my_w, textvariable=e2_str_name, width=10)
    e2.grid(row=i, column=1)
    e3 = tk.Entry(my_w, textvariable=e5_str_budget, width=10)
    e3.grid(row=i, column=2)
    e4 = tk.Entry(my_w, textvariable=e4_str_country, width=10)
    e4.grid(row=i, column=3)
    e5 = tk.Entry(my_w, textvariable=e3_str_client, width=10)
    e5.grid(row=i, column=4)
    b2 = tk.Button(my_w, text='Update', command=lambda: my_update(),
                   relief='ridge', anchor="w", width=5)
    b2.grid(row=i, column=5)

    def my_update():  # update record
        data = (e1_str_id.get(), e2_str_name.get(),e5_str_budget.get(),e4_str_country.get(), e3_str_client.get())
        # print(type(data[0]))
        id = cur.execute(
            "UPDATE project SET proj_name='{1}',budget='{2}', country='{3}', client_name='{4}' WHERE proj_id='{0}'".format(data[0], data[1], data[2],data[3],data[4]))
        # print("Row updated  = ", id.rowcount)
        for w in my_w.grid_slaves(i):  # remove the edit row
            w.grid_forget()
        display()  # refresh the data


btnAdd = tk.Button(my_w, text='Add', command=lambda: add_data(),
                   relief='ridge', anchor="w", width=15)
btnAdd.place(x=150, y=300)


def add_data():
    e1_str_proj_id = tk.StringVar(my_w)  # String variable
    e2_str_name = tk.StringVar(my_w)
    e3_str_client = tk.StringVar(my_w)
    e4_str_country = tk.StringVar(my_w)
    e5_str_budget = tk.IntVar(my_w)

    e1 = tk.Entry(my_w, textvariable=e1_str_proj_id, width=10)
    e1.grid(row=i, column=0)
    e2 = tk.Entry(my_w, textvariable=e2_str_name, width=10)
    e2.grid(row=i, column=1)
    e3 = tk.Entry(my_w, textvariable=e5_str_budget, width=10)
    e3.grid(row=i, column=2)
    e4 = tk.Entry(my_w, textvariable=e4_str_country, width=10)
    e4.grid(row=i, column=3)
    e5 = tk.Entry(my_w, textvariable=e3_str_client, width=10)
    e5.grid(row=i, column=4)
    b2 = tk.Button(my_w, text='add', command=lambda: my_add(),
                   relief='ridge', anchor="w", width=5)
    b2.grid(row=i, column=5)

    def my_add():
        data = data = (e1_str_proj_id.get(), e2_str_name.get(),e5_str_budget.get(),e4_str_country.get(), e3_str_client.get())
        adding = cur.execute(
            "INSERT INTO project VALUES ('{0}', '{1}', {2},'{3}','{4}')".format(data[0], data[1], data[2],data[3],data[4]))
        # print("Row added = ", adding.rowcount)
        for w in my_w.grid_slaves(i):  # remove the edit row
            w.grid_forget()
        display()


my_w.mainloop()

#commit the transcation
con.commit()

#close the cursor
cur.close()

#close the connection
con.close()