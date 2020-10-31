#!/usr/bin/env python3
# cli - command line interface to ntz yaml file.

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
    if len(argv) == 1:
        return 'list', 'all', 0, ''

def perform_cmd(sw, db, c, k, n):
    pass 

## need a dict that maps cmd to argv-str and the do-func
def mkmapping(argstr, dofunc):
    return (
        argstr,
        dofunc
    )

def make_switchboard():
    swb = {
        'list': mkmapping("-l", do_list),
        'store': mkmapping("-r", do_store),
        'erase': mkmapping("-f", do_erase),
        'replace': mkmapping("-e", do_replace),
    }
    return swb


# funcs that do commands
def do_list(cat):
    pass

def do_store(cat, note):
    pass

def do_erase(cat, n, note):
    pass

def do_replace(cat, n, note):
    pass

## main command line interface (cli)
def cli():
    db = opendb()
    sw = make_switchboard()

    cmd, cat, n, note = scan_args()
    perform_cmd(sw, db, cmd, cat, note)
    save(db)

cli()
