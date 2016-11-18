import os
import re
import json
from cudatext import *

from .simple_markdown import table
from . import format_proc

format_proc.INI = 'cuda_markdown_table_format.json'
format_proc.MSG = '[MD Table Format] '


def options():
    fn = format_proc.ini_filename()
    if os.path.isfile(fn):
        s = open(fn, 'r').read()
        #del // comments
        s = re.sub(r'(^|[^:])//.*'  , r'\1', s)           
        d = json.loads(s)
        
        op_margin = d.get("margin", 1)
        op_padding = d.get("padding", 0)
        
        s = d.get("default_justify", "L")
        op_just = table.Justify.LEFT if s=="L" else table.Justify.RIGHT if s=="R" else table.Justify.CENTER
        
        return op_margin, op_padding, op_just 
    else:
        return 1, 0, table.Justify.LEFT
    

def do_format(text):
    op_margin, op_padding, op_just = options()
    return table.format(text,
                        margin = op_margin, 
                        padding = op_padding,
                        default_justify = op_just,
                        )

class Command:
    def config_global(self):
        format_proc.config_global()

    def config_local(self):
        format_proc.config_local()

    def run(self):
        format_proc.run(do_format)
