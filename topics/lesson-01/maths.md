# Maths operator precedence

Some operators have a greater precedence than others. Think of it like a priority to the computer - the computer will execute those operators first.

```python
Type "help", "copyright", "credits" or "license" for more information.
>>> 3 ** 2
9
>>> 3.0 ** 2
9.0
>>> y = (12 * (3 ** 2)) + (4 * 3) + 4
>>> y
124
>>> 3 * 4 / 2
6.0
>>> 3 * 4 // 2
6
>>> (3 * 4) // 2
6
>>> 3 * (4 // 2)
6
>>> 3 + 4 // 2
5
>>> (3 + 4) // 2
3
>>> 3 + 4 * 2 - 8 / 12
10.333333333333334
>>>

```


## Binary vs Unary operators

Unary minus (-) is a unary operator. This means it only operates on one thing (called it's operand). The operand (value) follows the unary operator. It can be a fixed value or a variable.

```python
>>> -1
-1
>>> / 4
  File "<stdin>", line 1
    / 4
    ^
SyntaxError: invalid syntax
>>> -     1
-1
>>> 5 * -1
-5  
>>> -  (5 * -1)
5   
>>> -    -5
5
>>>
```