# -*- coding: utf-8 -*-
'''Pygments formatter. Converts bibTeX to XML.'''


#----------------------------------------------------------------------
#   Imports
#----------------------------------------------------------------------
##  StdLib
from __future__ import (
    absolute_import, 
    with_statement, 
    print_function,)

import itertools    

##  External
from pygments.formatter import Formatter
from pygments.token import (
    Text, 
    Comment, 
    Keyword, 
    String, 
    Number, 
    Operator,
    Other, 
    Punctuation, 
    Literal, 
    Whitespace,
    Name,)
    
import xmlwitch


#----------------------------------------------------------------------
#   Variables
#----------------------------------------------------------------------
DTD     = '<!DOCTYPE bibtex:file PUBLIC "-//BibTeXML//DTD XML for BibTeX v1.0//EN" "bibtexml.dtd">\n'
XMLNS   = 'http://bibtexml.sf.net/'
SKIPPABLE_TTYPES = frozenset([Whitespace, Operator, Punctuation])
XML     = xmlwitch.Builder(version='1.0', encoding='utf-8')


#----------------------------------------------------------------------
#   Functions
#----------------------------------------------------------------------
def _write_entry(entry_token_list):
    try:
        assert( entry_token_list[0][0] is Keyword.Reserved ) # sanity check! be sure we have an entry
    except AssertionError:
        import sys
        sys.exit(entry_token_list[0])
    
    entrytype = entry_token_list[0][1]
    entrytype = entrytype.lstrip('@')
    entrylabel = (entry_token_list[1][0] is Name.Label) and entry_token_list[1][1] or None
    
    if entrylabel:
        with XML.bibtex__entry( id=entrylabel ):
            with XML['bibtex__{0}'.format(entrytype)]:
                _write_fields( entry_token_list[2:] )
    else:
        with XML.bibtex__entry():
            with XML['bibtex__{0}'.format(entrytype)]:
                _write_fields( entry_token_list[1:] )

def _write_fields(field_token_list):
    field_indeces = sorted([idx for idx, item in enumerate(field_token_list) if item[0] is Name.Attribute])
    field_indeces = tuple(field_indeces)
    is_field = lambda x: x[0] is not Name.Attribute
    
    for idx, item in enumerate(field_token_list):
        ttype, value = item[0], item[1]
        if ttype is Name.Attribute:
            fieldname = value
            metaidx = field_indeces.index(idx)
            start   = idx+1
            stop    = 1 + metaidx
            value   = ''.join([ item[1] for item in 
                                itertools.takewhile(
                                    is_field, 
                                    field_token_list[idx+1:])
                        ])
            XML['bibtex__{0}'.format(fieldname)]( value )
                

def _entries(token_seq, indeces):
    # returns a list where each item is an entry 
    # (a slice of `token_seq`)
    entries = []
    
    for idx, i in enumerate(indeces):
        start = indeces[idx]
        try:
            stop      = indeces[idx + 1]
            entries.append( token_seq[start:stop] )
        except IndexError:
            entries.append( token_seq[start:] )
        
    return entries


#----------------------------------------------------------------------
#   Classes
#----------------------------------------------------------------------
class BibTeXML(Formatter):
    '''Formats a bibTeX token-stream to XML output.
    
    Output (should) be valid according to the output from the original 
    BibTeXML project (hosted on SourceForge.net).
    '''
    
    name = 'BibTeXML'
    aliases = ['bibtexml', 'bibteXML', 'bibxml']
    
    
    def __init__(self, **options):
        Formatter.__init__(self, **options)

        
    def format(self, tokensource, outfile):
        # need to be able to look ahead 
        token_seq = tuple([i for i in tokensource if i[0] not in SKIPPABLE_TTYPES])
        
        # mark where entries occur
        entry_indeces = tuple([ idx for idx, (ttype, value)  in enumerate(token_seq) 
                                if  ttype is Keyword.Reserved and 
                                    value.startswith('@') 
                            ])
        
        
        # build list of sub-iterators
        entries = _entries(token_seq, entry_indeces)
        
        # begin XML document
        XML.write(DTD)
        
        with XML.bibtex__file(xmlns__bibtex=XMLNS):
            idx = 0
            
            # write anything that occurs before the first entry
            for idx, item in enumerate(token_seq):
                if idx >= entry_indeces[0]:
                    break
                ttype, value = item[0], item[1]
                XML.write_indented('<!-- {0} -->'.format(value)) # FIXME: temp comment everything to debug

            # write the entries
            for idx, entry in enumerate( entries ):
                _write_entry(entry)
        
        outfile.write(str(XML))
            