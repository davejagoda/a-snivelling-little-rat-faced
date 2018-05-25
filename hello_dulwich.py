#!/usr/bin/env python3

from dulwich.repo import Repo
r = Repo('.')
h = r.head()
print(h)
c = r[h].message
print(c)
