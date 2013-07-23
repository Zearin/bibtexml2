# -*- coding: utf-8 -*-
'''FIXME: <<DocString>>
'''

# Based on spec summary at
# http://artis.imag.fr/~Xavier.Decoret/resources/xdkbibtex/bibtex_summary.html


#--------------------------------------------------------------------
##  Imports
#--------------------------------------------------------------------


### STDLIB
from __future__ import (
    absolute_import, 
    with_statement, 
    print_function,)

### External
from pygments.lexer import (
    RegexLexer, 
    bygroups, 
    include,)
    
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


#--------------------------------------------------------------------
##  Variables
#--------------------------------------------------------------------


PUBTYPES = frozenset({
    'article',
    'book',
    'booklet',
    'conference',
    'inbook',
    'incollection',
    'inproceedings',
    'manual',
    'mastersthesis',
    'misc',
    'phdthesis',
    'proceedings',
    'techreport',
    'unpublished'
})
'''Official bibTeX publication types.'''
### TODO: Tokenize as Keyword.Reserved

_pubtypes_re_string = '|'.join(PUBTYPES)


FIELDS = frozenset({
    'address',
    'annote',
    'author',
    'booktitle',
    'chapter',
    'crossref',
    'edition',
    'editor',
    'eprint',
    'howpublished',
    'institution',
    'journal',
    'key',
    'month',
    'note',
    'number',
    'organization',
    'pages',
    'publisher',
    'school',
    'series',
    'title',
    'type',
    'url',
    'volume',
    'year',
})
'''Standard bibTeX fields.  (Does not include non-standard fields.)'''


### TODO: Tokenize these as Name.Constant
MONTH_ABBR = ('jan'       ,'feb'      ,'mar'      ,'apr',
              'may'       ,'jun'      ,'jul'      ,'aug',
              'sep'       ,'oct'      ,'nov'      ,'dec')
'''Predefined bibTeX "variables" for the months of the year, 
which resolve to the month's full name.
'''


#--------------------------------------------------------------------
##  Classes
#--------------------------------------------------------------------


class BibtexLexer(RegexLexer):
    '''This class is a modification of the 'BibtexLexer' class from the module 
    'bibtex-pygments-lexer' (version 0.0.1), originally authored by Marco D. Adelfio. 
    
    I couldn't find a repository for the module anywhere, so I modified it according 
    to my needs.
    
    '''
    
    ### TODO: Change '=' type from Token.Text to Operator
    
    name        = 'BibTeX'
    aliases     = ['bibtex', 'bib', 'bibtexml']
    filenames   = ['*.bib']
    tokens      = {
        'whitespace': [
            (r'\s+', Whitespace)
        ],

        'bracket': [
            (r'[^}{]+', String.Double),
            (r'{',      Punctuation, '#push'),
            (r'}',      Punctuation, '#pop'),
        ],
        
        '@comment': [
            (r'[^}{]+', Comment),
            (r'{',      Punctuation, '#push'),
            (r'}',      Punctuation, '#pop'),
        ],

        'value': [
            include('whitespace'),
            (r'-?(0|[1-9]\d*)',     Number.Integer),
            (r'"(\\\\|\\"|[^"])*"', String.Double),
            (r"'(\\\\|\\'|[^'])*'", String.Single),
            (r'{',                  Punctuation,            'bracket'),
            (r'[^,}{]+',            Text),
        ],
        
        
        'root': [
            include('whitespace'),
            
            (r'(?i)(@(?:string|preamble))\s*({)',
             bygroups(
                 Keyword.Declaration, 
                 Punctuation),
             'field'),
             
             (r'(?i)(@(?:comment))\s*({)',
              bygroups(
                  Keyword.Declaration, 
                  Punctuation), 
             '@comment'),
             
             (r'(?i)(@(?:article|book|booklet|conference|inbook|incollection|'
             r'inproceedings|manual|mastersthesis|misc|phdthesis|proceedings|'
             r'techreport|unpublished))\s*({)',
             bygroups(
                 Keyword.Reserved, 
                 Punctuation), 
            'entry'),
            
            (r'(@[^ {]*)\s*({)',
             bygroups(
                 Keyword, 
                 Punctuation), 
            'entry'),
            
            (r'.*\n', Comment),
        ],

        'entry': [
            include('whitespace'),
            (r'([^, ]*)\s*(\,)',
             bygroups(
                 Name.Label, 
                 Punctuation), 
            'multi_fields'),
        ],

        'multi_fields': [
            include('whitespace'),
            
            (r'}', Punctuation, '#pop:2'), # pop back to root
            
            (r'([^}=\s]*)\s*(=)', 
            bygroups(
                Name.Attribute, 
                Operator), 
            'multi_values'),
            
            (r'[^}]+\n', Text),
        ],

        'multi_values': [
            include('value'),
            (r',', Punctuation, '#pop'), # pop back to multi_fields
            (r'}', Punctuation, '#pop:3'), # pop back to root
        ],

        'field': [
            include('whitespace'),
            (r'}', Punctuation, '#pop'), # pop back to root
            (r'([^}=\s]*)\s*(=)',
            bygroups(
                Name.Label, 
                Operator), 
            'single_value'),
            
            (r'[^}]+\n', Text),
        ],

        'single_value': [
            include('value'),
            (r'}', Punctuation, '#pop:2'), # pop back to root
        ],
        
    }
