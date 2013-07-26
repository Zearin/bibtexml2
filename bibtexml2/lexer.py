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


PUBTYPES = frozenset((
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
))
'''Official bibTeX publication types.'''
### TODO: Tokenize as Keyword.Reserved

_pubtypes_re_string = r'|'.join(PUBTYPES)


FIELDS = frozenset((
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
))
'''Standard bibTeX fields.  (Does not include non-standard fields.)'''


### TODO: Tokenize these as Name.Constant
MONTH_ABBR = ('jan'       ,'feb'      ,'mar'      ,'apr',
              'may'       ,'jun'      ,'jul'      ,'aug',
              'sep'       ,'oct'      ,'nov'      ,'dec')
'''Predefined bibTeX "variables" for the months of the year, 
which resolve to the month's full name.
'''
_month_abbr_re_string = '|'.join(MONTH_ABBR)


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
        'root': [
            include('whitespace'),
            include('@nonentries'),
            include('@entries'),
            include('raw_comment'),
        ],
        
        'whitespace': [
            (r'\s+',    Whitespace)
        ],

        'bracket': [
            (r'[^}{]+', String.Double),
            (r'{',      Punctuation, '#push'),
            (r'}',      Punctuation, '#pop'),
        ],
        
        'raw_comment': [
            (r'.*\n', Comment)
        ],
        
        '@entries': [  
            (r'(?i)(@(?:' + _pubtypes_re_string + r'))\s*({)',
                bygroups(
                    Keyword.Reserved, 
                    Punctuation), 
               '@entry'
               ),
        ],
        
        '@nonentries': [
            # non-comment @declarations
            (r'(?i)(@(?:string|preamble))\s*({)',
                bygroups(
                    Keyword.Declaration,
                    Punctuation),
                'field'),
             
            (r'(?i)(@(?:comment))\s*({)',
                bygroups(
                    Keyword.Declaration,
                    Punctuation),
                '@comment'),  # like 'bracket', but contents tokenized as Comment instead
             
             (r'(?i)(@[^(' + _pubtypes_re_string + '){]+)\s*({)',
                  bygroups(
                      Keyword, 
                      Punctuation), 
                 '@entry'
             ),
        ],
        
        '@comment': [
            (r'[^}{]+', Comment),
            (r'{',      Punctuation, '#push'),
            (r'}',      Punctuation, '#pop'),
        ],
        
        '@entry': [
            include('whitespace'),
            (r'(?i)([^, ]*)\s*(\,)',
                 bygroups(
                     Name.Label, 
                     Punctuation), 
                'field_multi'
            ),
        ],

        'field_multi': [
            include('whitespace'),
            
            (r'}', Punctuation, '#pop:2'), # pop back to root
            
            (r'(?i)([^}=\s]*)\s*(=)', 
                bygroups(
                    Name.Attribute, 
                    Operator), 
                'value_multi'
            ),
            
            (r'[^}]+\n', Text),
        ],
        
        'field': [
            include('whitespace'),
            (r'}', Punctuation, '#pop'), # pop back to root
            (r'(?i)([^}=\s]*)\s*(=)',
                bygroups(
                    Name.Label, 
                    Operator), 
                'value_single'
            ),
            (r'[^}]+\n', Text),
        ],

        'value': [
            include('whitespace'),
            (r'-?(0|[1-9]\d*)',     Number.Integer),
            (r'"(\\\\|\\"|[^"])*"', String.Double),
            (r"'(\\\\|\\'|[^'])*'", String.Single),
            (r'{',                  Punctuation,            'bracket'),
            (r'[^,}{]+',            Text),
        ],
        
        'value_multi': [
            include('value'),
            (r',', Punctuation, '#pop'), # pop back to field_multi
            (r'}', Punctuation, '#pop:3'), # pop back to root
        ],

        'value_single': [
            include('value'),
            (r'}', Punctuation, '#pop:2'), # pop back to root
        ],
        
        
        
    }
