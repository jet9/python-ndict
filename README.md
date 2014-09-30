python-ndict
============

Named dict for python based on common dict

```(python)
Custom dict class for access items thru methods:

>>> d = { 'a': 1, 'b': { 'c': 'foo', 'd': True, 'e': [1,2,3,{ 'f': 'good'}] }}
>>> d = NDict(d)
>>> d.a
1
>>> d.b.c
'foo'
>>> d.b.e[2]
3
>>> d.b.e[3]
{'f': 'good'}
>>> d.b.e[3].f
'good'
```




