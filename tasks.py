from ankiproject import compose, reduce, partial
from invoke import task

import operator

def sub(a, b):
    return a - b

pipeline = compose(partial(sub, b = 4), operator.neg)

@task
def clean(c, output = False):
    pass


@task
def build(c):
    print(pipeline(-6))