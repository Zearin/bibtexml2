# -*- coding: utf-8 -*-
'''Pygments-style filters.'''

##  StdLib
from __future__ import (
    absolute_import, 
    with_statement, 
    print_function,)
    

##  External
from pygments.util import get_bool_opt
from pygments.token import Name
from pygments.filter import (
    Filter,         # class-based     filters
    simplefilter,   # decorator-based filters
    )


@simplefilter
def token_types(lexer, stream, options):
    for ttype, value in stream:
        if ttype in options['ttypes']:
            yield ttype, value


@simplefilter 
def lowercase_entries(lexer, stream, options):
    for ttype, value in stream:
        pass  # TODO
        
        
@simplefilter 
def lowercase_fields(lexer, stream, options):
    for ttype, value in stream:
        pass  # TODO
        

@simplefilter
def expand_month_abbrs(lexer, stream, options):
    months = {
        'jan': 'January',
        'feb': 'February',
        'mar': 'March',
        'apr': 'April',
        'may': 'May',
        'jun': 'June',
        'jul': 'July',
        'aug': 'August',
        'sep': 'September',
        'oct': 'October',
        'nov': 'November',
        'dec': 'December',}
    for ttype, value in stream:
        if ttype is Token.Text and value in months.keys():
            value = months[value]
        yield ttype, value
        

@simplefilter    
def drop_whitespace(lexer, stream, options):
    for ttype, value in stream:    
        if ttype is not Token.Text.Whitespace:
            yield ttype, value

@simplefilter    
def drop_punctuation(lexer, stream, options):
    for ttype, value in stream:    
        if ttype is not Token.Punctuation:
            yield ttype, value

