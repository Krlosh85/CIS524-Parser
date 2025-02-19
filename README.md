# CIS524-Parser

In this repo you can find the coding/programming assignment for CIS 524, we developed a top down recursive parser and lexical analyzer for the following CFG:

```bash
<prog> ::= <let-in-end> { <let-in-end> }
<let-in-end> ::= let <decl-list> in <type> ( <expr> ) end ;
<decl-list> ::= <decl> { <decl> }
<decl> ::= id : <type> = <expr> ;
<type> ::= int | real
<expr> ::= <term> { + <term> | - <term> } |
if <cond> then <expr> else <expr>
<term> ::= <factor> { * <factor> | / <factor> }
<factor> ::= ( <expr> ) | id | number | <type> ( id )
<cond> ::= <oprnd> < <oprnd> |
<oprnd> <= <oprnd> |
<oprnd> > <oprnd> |
<oprnd> >= <oprnd> |
<oprnd> == <oprnd> |
<oprnd> <> <oprnd>
<oprnd> ::= id | intnum
```

## License
[Apache-2.0]http://www.apache.org/licenses/