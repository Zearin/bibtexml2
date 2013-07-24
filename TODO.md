# TODO


## Overall Project

- [x] Set up Travis-CI (working on it!)
- [x] Set up CodeQ.io
- [x] Set up Coveralls.io
- [ ] Set up PyPI Version (Crate.io)
- [ ] Set up Downloads (Crate.io)


## Tokenization 

See [bibtexml2/lexer.py](bibtexml2/lexer.py).

- [x] Tokenize bibtex pubtypes as `Keyword.Reserved`
- [x] Change tokenization type of `=` from `Token.Text` to `Token.Operator`
- [ ] Tokenize bibtex predefined month abbreviations as `Name.Constant`


## Filtering

See [bibtexml2/filter.py](bibtexml2/filter.py).

- [ ] Convert special bibtex characters to Unicode/UTF-8 characters


## Formatter

See [bibtexml2/formatter.py](bibtexml2/formatter.py).

- [ ] Convert tokens to XML (using `xmlwitch`)
- [ ] Valid output (from original BibTeXML schema)



<!-- ## Style -->
<!-- - [ ]  -->