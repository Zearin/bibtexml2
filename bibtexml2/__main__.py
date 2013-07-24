#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''{program[human_format]}

Usage: {program[cli_format]} [options]  <file>...

Options:
  -X, --no-xml    Output bibTeX instead of XML

'''

#--------------------------------------------------------------------
##  Imports
#--------------------------------------------------------------------
##  StdLib 
from __future__ import (
    absolute_import, 
    with_statement, 
    print_function,)

import sys

##  External
from    docopt import docopt

import  pygments
from    pygments.filters    import (
    KeywordCaseFilter, 
    TokenMergeFilter, 
    RaiseOnErrorTokenFilter,)
    
from    pygments.token      import *


##  Internal
from    bibtexml2 import (
    lexer,
    utils,)


#--------------------------------------------------------------------
##  Variables
#--------------------------------------------------------------------
BibtexLexer = lexer.BibtexLexer
docstring_format_dict = {
    'human_format': 'BibTeXML2',
    'cli_format'  : 'bibtexml2',
    }


#--------------------------------------------------------------------
##  __main__
#--------------------------------------------------------------------
def main():
    arguments = docopt( 
        __doc__.format( program=docstring_format_dict ), 
        version=        '{docstring_format_dict["human_format"]} 2.0', 
        options_first=  True
        )

    lexer = BibtexLexer()
    lexer.add_filter( RaiseOnErrorTokenFilter() )
    #lexer.add_filter( TokenMergeFilter() )
    lexer.add_filter( KeywordCaseFilter(case='lower') )
    
    for f in arguments['<file>']:
        
        # get bibtex source
        code = None
        with open(f, 'r') as f:
            code = ''.join( f.readlines() )

        # lex away at zee source!
        for idx, item in enumerate(pygments.lex(code, lexer)):
            tokentype, tokenvalue = item[0], item[1]
            if tokentype not in frozenset([Token.Text.Whitespace, Token.Punctuation]):
                print(
                    "{0:>5}\t{1[0]!s}\t{1[1]!r}".format(idx, item),
                    file=sys.stdout)
            continue
            
            if tokentype == Token.Keyword.Declaration:      # entry
                sys.stdout.write( '\n' + tokenvalue )
                    
            elif tokentype == Token.Name.Label:             # bibtex-id
                sys.stdout.write( '\tid=' + tokenvalue )
                
            elif tokentype == Token.Name.Attribute:         # field
                sys.stdout.write( '\t' + tokenvalue)
                
            elif tokentype == Token.Literal.String.Double:  # value 
                sys.stdout.write( (2*'\t') + tokenvalue )
            
            else:
                continue
            
            
if __name__ == '__main__':
    try:
        main()
    except pygments.filters.ErrorToken as e:
        sys.exit(e)