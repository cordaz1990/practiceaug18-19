>>> s = 'abc'
>>> t = [0,1,2]
>>> zip(s, t)

>>> for pair in zip(s, t):
        print(pair)
 
('a', 0)
('b', 1)
('c', 2)

>>> list(zip(s, t))
[('a', 0), ('b', 1), ('c', 2)]

>>> list(zip('Anne', 'Elk'))
[('A', 'E'), ('n','l'), ('n', 'k')]

t = [('a', 0), ('b', 1), ('c',2)
for letter, number in t:
    print(number, letter)
