import functional

# isCallable = lambda x: "__call__" in x
isFloat = lambda x: isinstance(x,float)
isPrivate = lambda x: x.startswith("__")
isNotPrivate = lambda x: not isPrivate(x)
import math
names = list(dir(math)).filter(isNotPrivate)
names.map(lambda x:eval(f"type(math.{x}"))
# this shows 'builtin_function_or_method or float
# what I want is like "float -> float"

# example of a function that typechecks its argument at runtime

class testFun(object):
    def __call__(self,arg):
        if (not isinstance(arg,str)):
            raise("TypeError")

testFun()("abc") # double braces are ugly
#testFun()(123) # raises Error

from inspect import signature
#signature(math.hypot) # error, no signature for built in
dir(math.hypot)
type(math.hypot)
#math.hypot.__text_signature__ # is empty

from typing import Callable, get_type_hints, List
def x(arg:int) -> int:
    return arg
get_type_hints(x) # gives __annotations__
get_type_hints(list) # is empty
#get_type_hints(List) # fails
type(List)

# id : Callable = lambda x: x

# Todo write type function
'''
that uses
* signature()
* get_type_hints()
* type()
appropriately
'''