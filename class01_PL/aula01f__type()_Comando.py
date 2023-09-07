Python 3.11.3 (v3.11.3:f3909b8bc8, Apr  4 2023, 20:12:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = True
>>> type(a)
<class 'bool'>
>>> a = 123
>>> type(a)
<class 'int'>
>>> a=4.40
>>> Type(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    Type(a)
NameError: name 'Type' is not defined. Did you mean: 'type'?
>>> type(a)
<class 'float'>
>>> a
4.4
>>> type(a)
<class 'float'>
