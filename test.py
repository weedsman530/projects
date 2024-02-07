import tkinter as tk
from tkinter import ttk
import psycopg2
import fnmatch

root = tk.Tk()
root.title("PostgreSQL Table Viewer")

def update(data):
    for x in tree.get_children():
        tree.delete(x)
    for item in data:        
        tree.insert("", "end", values=item)

def entry_focus(event):
    typed = search_entry.get()
    if typed == '':
        data = all_drugs
    else:
        data = []
        for item in all_drugs:
            if fnmatch.fnmatch(item[1], '*' + typed + '*') or typed.lower() in item[1].lower():
                data.append(item)
    update(data)

# Create treeview
tree = ttk.Treeview(root)
tree.pack()

conn = psycopg2.connect(
    host="aws-0-eu-central-1.pooler.supabase.com",
    database="postgres",
    user="postgres.ezxkhnkcgbnrtjqiihah",
    password="Qmj4bPXJAZJxPzVK"
)
cur = conn.cursor()
cur.execute("SELECT * FROM kart")
rows = cur.fetchall()

# Initialize all_drugs
all_drugs = []

# Clear existing treeview
for item in tree.get_children():
    tree.delete(item)

# Insert headers
headers = [desc[0] for desc in cur.description]
tree["columns"] = headers
for header in headers:
    tree.heading(header, text=header)

# Insert data
for row in rows:
    tree.insert("", "end", values=row)
    all_drugs.append(row)

cur.close()
conn.close()

search_entry = tk.Entry(root)
search_entry.pack()
search_entry.bind('<KeyRelease>', entry_focus)

root.mainloop()
