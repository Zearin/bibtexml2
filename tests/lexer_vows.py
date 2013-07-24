# -*- coding: utf-8 -*-
##  Generated by PyVows v2.0.4  (2013/07/19)
##  http://pyvows.org



#--------------------------------------------------------------------
##  Imports
#--------------------------------------------------------------------
### Standard Library
from    __future__  import (
    absolute_import, 
    with_statement, 
    print_function,)

import  os
from    os          import  path
from    os.path     import (
    abspath,
    basename,
    dirname,)
    
from    pprint      import pprint
import  sys

### Third Party
import  pygments
from    pygments.token import *
from    pygments.filters    import (
    KeywordCaseFilter, 
    TokenMergeFilter, 
    RaiseOnErrorTokenFilter,)
    
import  six

### PyVows Testing
from    pyvows      import (Vows, expect)

##  Local Imports
# imported below...



#--------------------------------------------------------------------
##  Variables
#--------------------------------------------------------------------
TEST_PATH       =   abspath(dirname(__file__))
MOD_PATH        =   abspath(path.join(TEST_PATH, '../'))
TESTDATA_PATH   =   abspath(path.join(TEST_PATH, 'examples'))

try:
    #   Import the file directly above this one
    #   (i.e., don’t use similar modules found in PYTHONPATH)
    _syspath = sys.path[:]
    sys.path.insert(0, MOD_PATH)
    
    import  bibtexml2
    from    bibtexml2   import lexer
    sys.path = _syspath[:]
    del _syspath
except ImportError as err:
    print(err)
    sys.exit(err)


FILES = set((f for f in os.listdir(TESTDATA_PATH)
            if f != 'testcases.bib')) # causes weird encoding errors; fix later
FILES = set((path.join(TESTDATA_PATH, f) for f in FILES))
LEXER = lexer.BibtexLexer()
LEXER.add_filter( RaiseOnErrorTokenFilter() )

#--------------------------------------------------------------------
##  Custom Contexts
#--------------------------------------------------------------------
def token_context(token_types):
    class Context(Vows.Context):
        def topic(self, parent_topic):
            if parent_topic[0] in frozenset(token_types):
                yield parent_topic
    return Context


#--------------------------------------------------------------------
##  Tests
#--------------------------------------------------------------------
@Vows.batch
class FilesToLex(Vows.Context):
    # first, rule out any dumb file errors
    def topic(self):
        for f in FILES:
            yield f
            
    def test_files_exist(self, topic):
        expect(topic).to_be_a_file()
        
    
    class WhenLexed(Vows.Context):
        def topic(self, parent_topic):
            with open(parent_topic, 'r') as f:
                code = ''.join( f.readlines() )
            for item in pygments.lex(code, LEXER):
                yield item  # 2-tuple of TokenType, TokenValue
            
        def we_get_no_lexer_errors(self, topic):
            expect(topic).not_to_be_an_error()
            expect(topic[0]).not_to_equal(Token.Error)
        
        
        class WhitespaceTokens(token_context( (Token.Text.Whitespace,) )):
            def only_contain_whitespace(self, topic):
                expect(topic[1]).to_match(r'\s+')
        
        
        class EntriesAndFields(token_context( (Token.Keyword.Declaration,
                                               Token.Name.Attribute) )):
            def contain_no_whitespace(self, topic):
                pre_strip, post_strip = topic[1], topic[1].strip()
                expect(topic[1]).not_to_match(r'\s+')
                expect(pre_strip == post_strip).to_be_true()
        
        
        class Entries(token_context( (Token.Keyword.Reserved, ) )):
            def have_valid_token_values(self, topic):
                pubtype = topic[1].lower()
                pubtype = pubtype.lstrip('@')
                expect(pubtype in lexer.PUBTYPES).to_be_true()