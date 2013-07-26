# -*- coding: utf-8 -*-
'''Convert bibTeX files to XML!  Built on Pygments.

Useful for manipulating bibTeX data as XML with XML toolsets.

If you don't like something about bibtexml2, it's built with Pygments--so 
you have its mature, widespread ecosystem at your disposal to tweak 
whatever you want.

'''

##  STDLIB
from __future__ import (
    absolute_import, 
    with_statement, 
    print_function,)

##  Local    
from bibtexml2 import (
    lexer,
    utils)

__name__            = 'bibtexml2'
__version__         = '0.2'
__author__          = 'Zearin'
__author_email__    = 'zearin@users.sourceforge.net'
__description__     = __doc__.splitlines()[0]