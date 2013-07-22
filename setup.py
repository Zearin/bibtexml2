# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from    textwrap import dedent


_config_metadata = {
    'name':             'bibtexml2',
    'version':          '0.1',
    'description':      'Convert bibTeX files to XML (with Pygments).',
    'long_description': dedent(
        
        '''Convert bibTeX files to XML!  

        Useful for manipulating bibTeX data as XML with XML toolsets.
        
        If you don't like something about bibtexml2, it's built with Pygments--so 
        you have its mature, widespread ecosystem at your disposal to tweak 
        whatever you want.
        
        

        ''' # add story of inspiration by original BibTeXML project on SourceForge
        
        ),
    
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
    
}

_config_urls = {
    #'url': 'URL to get it at.',
    #'download_url': 'Where to download it.',
}

_config_people = {
    'author':       'Zearin',
    'author_email': 'zearin@users.sourceforge.net',
}

_config_technical = {
    'packages':         ['bibtexml2'],
    'install_requires': ['docopt', 'pygments'],
    'tests_require':    ['pyvows>=2.0.4'],
    
    'entry_points':     
        '''[pygments.lexers]
            bibtexml2 = bibtexml2.lexer:BibtexLexer
            
        ''',
        
    'console_scripts': [
        'bibtexml2 = bibtexml2.__main__:main'
    ]
    
    #'scripts': [],
}

config = dict(**_config_metadata)
config.update(_config_urls)
config.update(_config_people)
config.update(_config_technical)

setup(**config)
