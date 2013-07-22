# -*- coding: utf-8 -*-
'''Pygments XML formatter for bibTeX.'''

##  StdLib
from __future__ import (
    absolute_import, 
    with_statement, 
    print_function,)
    

##  External
from pygments.formatter import Formatter
import xmlwitch


#-------------------------------------------------------------------------------------------------
xml         = xmlwitch.Builder()

# 
# Token.Name.Attribute = field

class NullFormatter(Formatter):
    def format(self, tokensource, outfile):
        for ttype, value in tokensource:
            