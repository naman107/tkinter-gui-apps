from tkinter import *
import sqlite3

window = Tk()
window.title('Database')
window.geometry('370x320')

conn = sqlite3.connect('employee.db')
csr = conn.cursor()

def add():
    conn = sqlite3.connect('employee.db')
    csr = conn.cursor()

    csr.execute("INSERT INTO employees VALUES (:name,:age,:designation,:salary)",
                    {
                        'name': name_entrybox.get(),
                        'age': age_entrybox.get(),
                        'designation': designation_entrybox.get(),
                        'salary': salary_entrybox.get()
                    }
    )

    conn.commit()
    conn.close()

    name_entrybox.delete(0,END)
    age_entrybox.delete(0,END)
    designation_entrybox.delete(0,END)
    salary_entrybox.delete(0,END)

def destroyWindow(window):
    window.destroy()

def show():
    conn = sqlite3.connect('employee.db')
    csr = conn.cursor()

    csr.execute("SELECT *,oid FROM employees")
    records = csr.fetchall()

    show_window = Tk()
    show_window.title('Show Records')

    for record in records:
        # labels for records
        record_name_label = Label(show_window, text=record[0]+ "     " + record[2] +  "\n")
        record_name_label.pack(padx=20, pady=1, ipadx = 100)

    print(records)
    conn.commit()
    conn.close()

    exit_btn = Button(show_window,text='Exit',command=lambda: destroyWindow(show_window))
    exit_btn.pack(padx=20, pady=8, ipadx = 100)

    show_window.mainloop()

def delete():
    conn = sqlite3.connect('employee.db')
    csr = conn.cursor()

    csr.execute("DELETE from employees WHERE oid = " + id_entrybox.get())
    id_entrybox.delete(0,END)

    conn.commit()
    conn.close()

def update():
    conn = sqlite3.connect('employee.db')
    csr = conn.cursor()

    record_id = id_entrybox.get()

    csr.execute("""UPDATE employees SET
        name = :name,
        age = :age,
        designation = :designation,
        salary = :salary
        WHERE oid = :oid""",
              {
                  'name': name_entrybox.get(),
                  'age': age_entrybox.get(),
                  'designation': designation_entrybox.get(),
                  'salary': salary_entrybox.get(),
                  'oid': record_id
              })

    conn.commit()
    conn.close()

    name_entrybox.delete(0,END)
    age_entrybox.delete(0,END)
    designation_entrybox.delete(0,END)
    salary_entrybox.delete(0,END)

def edit():
    conn = sqlite3.connect('employee.db')
    csr = conn.cursor()
    record_id = id_entrybox.get()

    csr.execute("SELECT * FROM employees WHERE oid = " + record_id)
    records = csr.fetchall()

    for record in records:
        name_entrybox.insert(0, record[0])
        age_entrybox.insert(0, record[1])
        designation_entrybox.insert(0, record[2])
        salary_entrybox.insert(0, record[3])

    # Create a Save Button To Save edited record
    edit_btn = Button(window, text="Save Record", command=update)
    edit_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=(25,1), ipadx=120)

#labels
name_label = Label(window,text='Employee name')
name_label.grid(row=0,column=0,padx=20,sticky=W)

age_label = Label(window,text='Employee age')
age_label.grid(row=1,column=0,padx=20,sticky=W)

designation_label = Label(window,text='Employee designation')
designation_label.grid(row=2,column=0,padx=20,sticky=W)

salary_label = Label(window,text='Employee salary($)')
salary_label.grid(row=3,column=0,padx=20,sticky=W)

id_label = Label(window,text='Select ID')
id_label.grid(row=6,column=0,pady=7)

#entry boxes
name_entrybox = Entry(window,width=30,borderwidth=2)
name_entrybox.grid(row=0,column=1,sticky=W)

age_entrybox = Entry(window,width=30,borderwidth=2)
age_entrybox.grid(row=1,column=1,sticky=W)

designation_entrybox = Entry(window,width=30,borderwidth=2)
designation_entrybox.grid(row=2,column=1,sticky=W)

salary_entrybox = Entry(window,width=30,borderwidth=2)
salary_entrybox.grid(row=3,column=1,sticky=W)

#ID entry box
id_entrybox = Entry(window,width=8,borderwidth=2)
id_entrybox.grid(row=6,column=1)

# #Buttons
add_btn = Button(window,text='Add record',command=add)
add_btn.grid(row=4, column=0, columnspan=2, pady=(15,5), padx=(28,15), ipadx=120)

show_btn = Button(window,text='Show records',command=show)
show_btn.grid(row=5, column=0, columnspan=2, pady=5, padx=(35,25), ipadx=120)

delete_btn = Button(window,text='Delete record',command=delete)
delete_btn.grid(row=8, column=0, columnspan=2, pady=5, padx=(28,15), ipadx=120)

edit_btn = Button(window,text='Edit record',command=edit)
edit_btn.grid(row=9, column=0, columnspan=2, pady=5, padx=(16,4), ipadx=130)

conn.commit()
conn.close()

mainloop()