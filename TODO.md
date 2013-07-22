# TODO


## Overall Project

- [ ] Set up Travis-CI
- [ ] Set up CodeQ.io
- [ ] Set up Coveralls.io
- [ ] Set up PyPI Version (Crate.io)
- [ ] Set up Downloads (Crate.io)


## Tokenization 

See [bibtexml2/lexer.py](bibtexml2/lexer.py).

- [x] Tokenize bibtex pubtypes as `Keyword.Reserved`
- [x] Change tokenization type of `=` from `Token.Text` to `Token.Operator`
- [ ] Tokenize bibtex predefined month abbreviations as `Name.Constant`


## Filtering

- [ ] Convert special bibtex characters to Unicode/UTF-8 characters


## Formatter

- [ ] Convert tokens to XML (using `xmlwitch`)
- [ ] Output is valid according to original BibTeXML



<!-- ## Style -->
<!-- - [ ]  -->