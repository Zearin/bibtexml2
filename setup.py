# -*- coding: utf-8 -*-
'''Convert bibTeX files to XML!  Built on Pygments.

Useful for manipulating bibTeX data as XML with XML toolsets.

If you don't like something about bibtexml2, it's built with Pygments--so 
you have its mature, widespread ecosystem at your disposal to tweak 
whatever you want.

'''


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from    textwrap import dedent

##---------------------------------------------------------------
__name__            = 'bibtexml2'
__version__         = '0.2'
__author__          = 'Zearin'
__author_email__    = 'zearin@users.sourceforge.net'
__description__     = __doc__.splitlines()[0]
##---------------------------------------------------------------

config = {
    ##
    ##  OVERALL
    ##---------------------------------------------------------------
    'name':             __name__,
    'version':          __version__,
    'description':      __description__,
    'long_description': __doc__,
        
    ##
    ##  PEOPLE
    ##---------------------------------------------------------------
    'author':           __author__,
    'author_email':     __author_email__,
                        
    ##
    ##  METADATA
    ##---------------------------------------------------------------
    'license':          'MIT',
    'keywords':         'bibtex xml conversion pygments',
    'classifiers':      [
        'Development Status :: 2 - Pre-Alpha',
        
        'Environment :: Console',
        'Environment :: Plugins',
        
        'Intended Audience :: Science/Research',
        
        'License :: OSI Approved :: MIT License',
        
        'Natural Language :: English',
        
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: OS Independent',
        
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        
        'Topic :: Text Processing',
        'Topic :: Utilities',
    ],


    ##
    ##  URLS
    ##---------------------------------------------------------------
    #'url': 'URL to get it at.',
    #'download_url': 'Where to download it.',

    ##
    ##  TECHNICAL
    ##---------------------------------------------------------------
    'packages':         [__name__],
    'install_requires': ['docopt', 'pygments'],
    'setup_requires':   ['docopt', 'pygments'],
    'tests_require':    ['pyvows>=2.0.4'],
    
    'entry_points':     {
        'pygments.lexers':      'bibtex = bibtexml2.lexer:BibtexLexer',
        'pygments.formatters':  'bibtex = bibtexml2.formatter:BibTeXML',
        'console_scripts':      'bibtexml2 = bibtexml2.__main__:main'
    },
    
    #'scripts': [],
}


setup(**config)
