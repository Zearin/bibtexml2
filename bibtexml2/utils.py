# -*- coding: utf-8 -*-
'''Miscellaneous BibTeX utilties.'''

##  STDLIB
from __future__ import (
    absolute_import, 
    with_statement, 
    print_function,
    )
    
import io

##  External
import six

##  Local


#------------------------------------------------------------------------------
def _indeces_that_match(sequence, re_object):
    '''Given `sequence`, returns a list of indeces where 
    `sequence[index]` matches `re_object`.
    
    '''
    indeces = []
    for idx, line in enumerate(sequence):
        if re_object.search(line):
            indeces.append(idx)
    return indeces

def _break_list(sequence, indeces):
    '''Breaks sequence into a list containing tuples.  
    Each tuple contains a slice of `sequence`, calculated 
    using each pair of values in `indeces`.
    
    '''
    results = []
    
    for idx, item in enumerate(indeces):
        start = indeces[idx]
        try:                stop = indeces[idx+1]
        except IndexError:  stop = None
        results.append( tuple(sequence[start:stop]) )
        
    return results

#------------------------------------------------------------------------------
def open(file):
    '''Opens a bibtex `file` and returns its contents as a string.

    Uses `readlines()` internally.

    '''
    try:
        lines = None
        # open the file as *bytes*:
        #  - lots of TeX stuff is written in ASCII, 
        #  - this function shouldn't alter the text
        #  - any unicode translation is up to other functions
        with io.open(file, 'rb') as f:
            lines = f.readlines()
        return lines
    except Exception as e:
        # Just adds a little extra message with whitespace to make errors easier to spot
        from textwrap import dedent
        message = '''
        
ERROR OPENING BIBTEX FILE: {file}

        '''.format(file=file)
        print(dedent(message))
        raise e
