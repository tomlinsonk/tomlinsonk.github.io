---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Python Quine"
subtitle: "A program that outputs itself."
summary: "A quine is a program that outputs its own source code. Here's one I wrote in Python."
authors: []
tags: []
categories: []
date: 2021-02-19T14:03:00-05:00
lastmod: 2021-02-19T14:03:00-05:00
featured: false
draft: false
share: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  height: "200"
  caption: ""
  focal_point: "Left"
  preview_only: true

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---


In [CS 6110](https://classes.cornell.edu/browse/roster/SP21/class/CS/6110) today, [Dexter](https://www.cs.cornell.edu/~kozen/) mentioned [quines](https://en.wikipedia.org/wiki/Quine_(computing)): programs that output their own source code. I quickly got sucked into a very fun internet rabbit-hole, including [a collection of quines in different languages](http://www.nyx.net/~gthompso/quine.htm), [a 128-language cyclical quine](https://github.com/mame/quine-relay), [a quine robust to mutations](https://github.com/mame/radiation-hardened-quine), and [an HTML page that displays its own source](https://no-gravity.github.io/html-quine/).

I had to try it out for myself. Here's what I came up with in Python 3:

```python
from abc import ABC, abstractmethod
from string import ascii_lowercase


class AbstractQuine(ABC):

    imports = 'from abc import ABC, abstractmethod\n' \
              'from string import ascii_lowercase'

    @abstractmethod
    def print_code(self):
        ...


class Quine(AbstractQuine):

    def print_code(self):
        unmap = lambda x: x[0].replace('d', 'd\\n') + f' \\\n{s}{s}{s}  ' + x[1]
        s, n, q, t, r, b = '    ', '\n', '\'', '~', 'r', '\\'

        body = r'{self.imports}\n\n\nclass {self.__class__.__base__.__name__}~' \
               r'({ascii_lowercase[:3].upper()}):\n\n~' \
               r'{s}imports = {unmap(list(map(repr, self.imports.split(n))))}\n\n~' \
               r'{s}@abstractmethod\n{s}def print_code(self):\n{s}{s}...\n\n\n~' \
               r'class Quine({self.__class__.__base__.__name__}):\n\n~' \
               r'{s}def print_code(self):\n~' \
               r'{s}{s}unmap = lambda x: x[0].replace({q}d{q}, {q}d\\\\n{q})~' \
               r' + f{q} \\\\\\n{{s}}{{s}}{{s}}  {q} + x[1]\n~' \
               r'{s * 2}s, n, q, t, r, b = {q}    {q}, {repr(n)}, \'\\\'\', ~' \
               r'{q}{t}{q}, {q}r{q}, {q}{b}{b}{q}\n\n~' \
               r'{s * 2}body = {r}{q}{body.replace(t, t + q + s[1] + b + n + ~' \
               r'3 * s + s[:3] + r + q)}{q}\n\n~' \
               r'{s * 2}exec(f{q}print(f\"{{body.replace(t, \"\")}}\"){q})\n\n\n~' \
               r'{self.__class__.__name__}().print_code()'

        exec(f'print(f"{body.replace(t, "")}")')


Quine().print_code()

```

Some people might not like using `exec`, but I think it's fair game. To verify that this is a quine, you can save the above code in `quine.py` and run `python3 quine.py | diff quine.py -` (make sure to have one newline after `Quine().print_code()`). Of course, much shorter quines are possible in Python, notably:
```python
c='c=%r;print(c%%c)';print(c%c)
```
from [Wikipedia](https://en.wikipedia.org/wiki/Quine_(computing)#Examples), but it was fun to make something a bit longer work. 
