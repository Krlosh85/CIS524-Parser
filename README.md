![](https://www.csuohio.edu/sites/default/files/Full%20Vertical_CSU%20Green_Fresh%20Green_CMYK_Update.jpg)
# CIS524-Parser
In this repo you can find the coding/programming assignment for CIS 524.

Authors:

Carlos Herrera

Hannah Simon

## About the repo
We developed a top down recursive parser and lexical analyzer for the following CFG:

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

We implemented the following before moving to the :
- Top Down Parser with Lexical analyzer from class, in C
- Top Down Parser with Lexical analyzer from class, in C with input from user (translation)
- Top Down Parser with Lexical analyzer from class, in python with input from user (translation)
- Top Down parser with Lexical analyzer from the book, in python, using REGEX
- Top Down parser with Lexical analyzer from class, in python, using REGEX like the one from the book.

The top down parser seen in class follows the CFG:

```bash
<expr>   ::= <term> { ("+" | "-") <term> }
<term>   ::= <factor> { ("*" | "/") <factor> }
<factor> ::= <IDENT> | <INT_LIT> | "(" <expr> ")"
<IDENT>  ::= <LETTER> { <LETTER> | <DIGIT> }
<INT_LIT> ::= <DIGIT> { <DIGIT> }
<LETTER> ::= "a" - "Z"
<DIGIT>  ::= "0" - "9"

```

## Any questions?
You can reach out via email in profiles!