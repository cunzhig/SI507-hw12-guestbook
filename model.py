import json
from datetime import datetime

GUESTBOOK_ENTRIES_FILE = "entries.json"
entries = []

def init():
    global entries, next_id
    try:
        f = open(GUESTBOOK_ENTRIES_FILE)
        entries = json.loads(f.read())
        next_id = int(entries[0]['id']) + 1
        f.close()
    except:
        entries = []
        next_id = 0

def get_entries():
    global entries
    return entries

def add_entry(name, text):
    global entries, GUESTBOOK_ENTRIES_FILE, next_id
    now = datetime.now()
    time_string = now.strftime("%b %d, %Y %-I:%M %p")
    # if you have an error using this format, just use
    # time_string = str(now)
    entry = {"author": name, "text": text, "timestamp": time_string, "id": str(next_id)}
    next_id += 1
    entries.insert(0, entry) ## add to front of list
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")
    
def delete_entry(ID):
    global entries, GUESTBOOK_ENTRIES_FILE
    for e in entries:
        if e['id'] == ID:
            entries.remove(e)
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not delete entries from file.")

def change_entry(ID, text):
    global entries, GUESTBOOK_ENTRIES_FILE
    now = datetime.now()
    time_string = now.strftime("%b %d, %Y %-I:%M %p")
    for e in entries:
        if e['id'] == ID:
            e['text']=text
            e['timestamp']=time_string
    
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not change entries in file.")
        
            
