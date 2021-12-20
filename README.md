# fmappy

![Python Workflow](https://github.com/xtofl/fmappy/workflows/Python%20Main%20Workflow/badge.svg) [![codecov](https://codecov.io/xtofl/fmappy/branch/master/graph/badge.svg)](https://codecov.io/xtofl/fmappy) [![CodeFactor](https://www.codefactor.io/repository/github/xtofl/fmappy/badge)](https://www.codefactor.io/repository/github/xtofl/fmappy) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Brings the Functionality of the Functor to Python.

```python
>>> fmap(square, dict(one=1, two=2, three=3))
{'one': 1, 'two': 4, 'three': 9}
```

I miss this.  The implementation of `map` always returns a generator; but sometimes
I want to keep the container type, just map the contained values.  This is what
the functiona-programming world knows as a Functor.

## Why this Library?

```python
>>> numbers = {'one': 1, 'two': 2, 'three': 3}
>>> squared = {k: v*v for k, v in numbers.items()}
>>> names = numbers.keys()
>>> NAMES = tuple(n.upper() for n in names)
>>> NAMES_TOO = tuple(map(str.upper, names))
```

We have got used to these patterns: dict-comprehensions, using `map` and storing
it into a `tuple` for later use.  So used that we don't realize it is chipping
away some of our mental capacity while reading and writing code.  I want this to
stop: a use case that occurs so often has the right to be streamlined into
something simpler, and we can borrow gratefully from the functional programming
world here.

A number of libraries exist for full fledged functional programming in Python.
These libraries assume an FP background.  I want a library that starts from the
Python syntax, and adds as little clutter as possible - as many batteries included.

As Alan Kaye said: make Simple things Simple, and Hard things Possible.

I bumped onto [this gist] and realized this was something: We Already Needed It For
A Long Time ([WANIFALT]).  This is simple enough to use for even starting Pythonistas.
And it allows enough extensions for the professional to integrate it in their code base.

## Goals

* `import this`
* cover 95% of the day to day use cases (to my knowledge)
* wrist-friendly: use `fmap` instead of `map` and you're there
* Closed for Change, Open for Extension

## Other Libraries

* https://pypi.org/project/pyfunctor/: almost, but not quite, entirely unlike Python

  ```python
  f = (Functor(range(10)) >> c_(map)(lambda x: x * 2)
  ```

* https://pypi.org/project/tx-functional/: almost like Python

  ```python
  assert Nothing.map(lambda x:2) == Nothing
  ```

[this gist]: https://gist.github.com/3noch/eef18dba108be7db0441
[WANIFALT]: https://qbziz.wordpress.com/2008/10/23/you-heard-it-here-first/
