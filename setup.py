# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from    textwrap import dedent

import bibtexml2 


config = {
    ##
    ##  OVERALL
    ##---------------------------------------------------------------
    'name':             bibtexml2.__name__,
    'version':          bibtexml2.__version__,
    'description':      bibtexml2.__description__,
    'long_description': bibtexml2.__doc__,
        
    ##
    ##  PEOPLE
    ##---------------------------------------------------------------
    'author':       bibtexml2.__author__,
    'author_email': bibtexml2.__author_email__,

        
    
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
    'packages':         [bibtexml2.__name__],
    'install_requires': ['docopt', 'pygments'],
    'setup_requires':   ['docopt', 'pygments'],
    'tests_require':    ['pyvows>=2.0.4'],
    
    'entry_points':     {
        'pygments.lexers': 'bibtex = bibtexml2.lexer:BibtexLexer',
        'pygments.formatters': 'bibtex = bibtexml2.formatter:BibTeXML',
        'console_scripts': 'bibtexml2 = bibtexml2.__main__:main'
    },
    
    #'scripts': [],
}


setup(**config)
