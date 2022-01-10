# foop.py
this is ment to be interperated and easy to use. feel free to remake this in different coding lanuages, games, or projects. if publicly use, please give some credit

it is ment to execute commands and skip the rest
```
print:foo
this line will be looked at but not used
print:foo
```
## Syntax
commands are done with the word, then `:`, then the inputs
```
print:foo
print:foop
```
varables are made by puting `#` then key, then value.
```
#f=foo
#b=boo
```
to get varables, you put the key around `$`
```
print:$f$
print:$b$
```
math and OPs are done like this
```
(1+1)
(1-1)
(1*1)
(1/1)
(1=1)
```
### Layering
the scripts starts the lowest layer layers are shown by `;` every time an `if:` is true, it moves up an layer, if there is none, it will move down a layer
```
#a=false
print:first starting low
if:$a$
;print:now am higher
;end:
#a=true
print:geting up
jump:1
```
## built-in varables
| Syntax | Description |
| ----------- | ----------- |
| `cl` | returns curent line, usefull for jumps |
| `lines` | returns the lines  |
## Commands
| Syntax | Description |
| ----------- | ----------- |
| `print:<any>` | put text to screen |
| `$<key>$` | varable |
| `if:<True>` | if true move up layer |
| `end:` | stops script |
| `jump:<int>` | jumps lines |
| `(<any>+<any>)` | math |
| `(<any>=<any>)` | compare |
