#!/usr/bin/env python3
# cli - command line interface to ntz yaml file.

"""
### Showing notes.
Typing `ntz` will display your notes.
So will `ntz -l Shopping`

### Saving notes
Use [-r] for remember. Using [-r] on its own will save to the default ToDo category, like so:

`$ ntz -r "my first note"`

Using `-r` is the same as `ntz -c ToDo "my first note"

Use the -c flag to create a new category or direct a note to an existing category, like this:

`$ ntz -c Shopping "while out, get eggs"`

### Removing notes
Use [-f] for forget. [-f] requires a category and note number.

To delete the note we made in the Shopping category (and also the category, because it will be empty) we can do:

`$ ntz -f Shopping 1`

### Editing notes
Use [-e] for edit. This is more of a replacement then an edit.

To replace our first note, we can do

`$ ntz -e General 1 'my first note, edited'`

### Clearing all notes

`$ ntz clear`

You will be prompted with a Y/N and given a chance to review your notes before they are deleted.
"""

import yaml
from sys import argv 


def opendb():
    fn = 'db.yaml'
    try:
        file = open(fn, 'r')
        data = yaml.load(file, Loader=yaml.FullLoader)
        #print(data)
        return data
    except FileNotFoundError:
        file = open(fn, 'w')
    return {}

def save(db):
    fn = 'db.yaml'
    with open(fn, 'w') as file:
        documents = yaml.dump(db, file)

def scan_args():
    print("debug:", argv)
    # "ntz"
    if len(argv) == 1:
        return '-l', 'ToDo', '0', ''
    # ntz -r "note"
    if len(argv) == 3:
        return argv[1], "ToDo", '0', argv[2]
    # 'ntz' '-c' 'cat' 'note/num'
    if len(argv) == 4:
        return argv[1], argv[2], '0', argv[3]
    # 'ntz' '-e' 'cat' 'num' 'new note'
    if len(argv) == 5:
        return argv[1], argv[2], argv[3], argv[4]



def perform_cmd(db, cmd, cat, n, note):
    swb = {
        '-l': do_list,
        '-r': do_store,
        '-c': do_store,
        '-f': do_erase,
        '-e': do_replace,
    }
    do_work = swb.get(cmd)

    if do_work is None:
        return -1, "invalid command"

    return do_work(db, cat, n, note)

# funcs that do commands
def do_list(db, cat, n, note):
    # `ntz -l Shopping`
    if cat != 'all':
        print_cat(db, cat)
    else:
        cats = db.get(cat)
        if cats != None:
            for cat in cats:
                print_cat(db, cat)
    return 0, ''

def print_cat(db, cat):
    notes = db.get(cat)
    #print("debug: db", db)
    #print("debug: notes", notes)
    if notes is not None:
        i = 0
        print(cat, ":")
        for n in notes:
            print('\t', i, '-', n)
            i = i + 1

def do_store(db, cat, n, note):
    # ntz -c Shopping "while out, get eggs"
    if db.get(cat) is None:
        db[cat] = []
    db[cat].append(note)
    return 0, ''

def do_erase(db, cat, n, note):
    # -f Shopping 1
    return 0, ''

def do_replace(db, cat, n, note):
    # -e General 1 'my first note, edited'
    return 0, ''

## main command line interface (cli)
def cli():
    db = opendb()

    cmd, cat, n, note = scan_args()
    result, reason = perform_cmd(db, cmd, cat, n, note)
    save(db)
    if result != 0: # some error
        print(result, reason)

cli()
