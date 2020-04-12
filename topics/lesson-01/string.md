# String operations

## String concatenation (joining)

```python

>>> 'Hello Sgt Taylor!'
'Hello Sgt Taylor!'
>>> print('Hello Sgt Taylor!')
Hello Sgt Taylor!
>>> print('Hello '    'Sgt Taylor!') 
Hello Sgt Taylor!
>>> print('Hello ''Sgt Taylor!')     
Hello Sgt Taylor!
>>> print('Hello ' 'Sgt Taylor!') 
Hello Sgt Taylor!
>>> print('Hello'    'Sgt Taylor!') 
HelloSgt Taylor!
>>> print('Hello ' 'Sgt Taylor!')    
Hello Sgt Taylor!
>>> print('Hello ' * 3)
Hello Hello Hello 
>>> print('Hello ' * 3 'Sgt Taylor!') 
  File "<stdin>", line 1
    print('Hello ' * 3 'Sgt Taylor!')
                       ^
SyntaxError: invalid syntax
>>> print('Hello ' * (3) 'Sgt Taylor!') 
  File "<stdin>", line 1
    print('Hello ' * (3) 'Sgt Taylor!')
                         ^
SyntaxError: invalid syntax
>>> print(('Hello ' * 3) 'Sgt Taylor!') 
  File "<stdin>", line 1
    print(('Hello ' * 3) 'Sgt Taylor!')
                         ^
SyntaxError: invalid syntax
>>> print(('Hello ' * 3).join() 'Sgt Taylor!') 
  File "<stdin>", line 1
    print(('Hello ' * 3).join() 'Sgt Taylor!')
                                ^
SyntaxError: invalid syntax
>>> print(('Hello ' * 3) + 'Sgt Taylor!')      
Hello Hello Hello Sgt Taylor!
>>> print('Hello ' 'Sgt Taylor!')         
Hello Sgt Taylor!
>>> print(('Hello ' * 3) + 'Sgt Taylor!') 
Hello Hello Hello Sgt Taylor!
>>> print('Hello ' * 3 + 'Sgt Taylor!')   
Hello Hello Hello Sgt Taylor!

```

## String variables

```python
>>> greeting = 'Hello '
>>> print(greeting)
Hello
>>> print(greeting * 3)
Hello Hello Hello
>>> print(greeting * 3)
Hello Hello Hello
>>> multiplier = 3
>>> print(greeting * multiplier)
Hello Hello Hello
>>> print(greeting * multiplier + 'Sgt Taylor!')
Hello Hello Hello Sgt Taylor!
>>> name = 'Sgt Taylor!'
>>> print(greeting * multiplier + name)
Hello Hello Hello Sgt Taylor!
>>> name = 'Fred!'
>>> print(greeting * multiplier + name)
Hello Hello Hello Fred!
```