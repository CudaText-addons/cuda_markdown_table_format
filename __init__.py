from cudatext import *
import sys
import os
import json
import re

from .simple_markdown import table
from . import format_proc

format_proc.INI = 'cuda_markdown_table_format.json'
format_proc.MSG = '[MD Table Format] '

def options():
    res = {}
    fn = format_proc.ini_filename()
    if os.path.isfile(fn):
        s = open(fn, 'r').read()
        #del // comments
        s = re.sub(r'(^|[^:])//.*'  , r'\1', s)           
        res = json.loads(s)
    return res
    

def do_format(text):
    op = options()
    return table.format(text,
                        margin = op["margin"], 
                        padding = op["padding"],
                        default_justify = table.Justify.from_string[op["default_justification"]],
                        )

class Command:
    def config_global(self):
        format_proc.config_global()

    def config_local(self):
        format_proc.config_local()

    def run(self):
        format_proc.run(do_format)
