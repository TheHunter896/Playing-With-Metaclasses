"""
Created by: David Bros
Date: 11/05/2020
Notes: This document lacks social distancing
"""

import types
import collections
import collections.abc
import functools
import operator
import re
import sys

class Transform(object):
    """
    Little test I did to ensure getattr and setitem are the correct methods
    """
    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def __setitem__(self, key, value):
        return object.__setattr__(self, key, value)

class MetaTransform(type):
    """
    Metaclass binds methods to the class that is being created, rather than to the only one that inherits this behaviour
    """

    def __new__(mcs, classname, bases, classDict, *args):
        classDict['__len__'] = dict.__len__ #If you want to integrate it with pandas, this will have to change
        classDict['__getitem__'] = object.__getattribute__
        classDict['__setitem__'] = object.__setattr__
        classDict['__str__'] = mcs.tostr
        classDict['lattributes'] = mcs.lattributes
        classDict['lvalues'] = mcs.lvalues
        classDict['update'] = mcs.update
        classDict['fromdict'] = mcs.fromdict
        classDict['seq_update'] = mcs.seq_update
        classDict['nonseq_update'] = mcs.nonseq_update
        classDict['items'] = mcs.items
        classDict['get'] = mcs.get
        classDict['pop'] = mcs.popitem

        return super().__new__(mcs, classname, bases, classDict)

    def lattributes(cls):
        return list(cls.__dict__.keys())

    def lvalues(cls):
        return list(cls.__dict__.values())

    #Make a wrapper to use sequential/non sequential updates, right now it will be on a 2D iterable Iterable[Iterable[_KT, _VT]]
    #sequpdate(seq: set, list, dict...), nonsequpdate(name, value) -> None

    def seq_update(cls, iterable):
        for tup in iterable: cls.nonseq_update(tup)

        return True

    def nonseq_update(cls, non_iterable):

        return object.__setattr__(cls, non_iterable[0], non_iterable[1])

    def update(cls, iterable):
        """
        Update from a 2D sequence
        :param iterable:
        :return:
        """

        if type(iterable) == list:
            cls.seq_update(iterable)
        elif type(iterable) == dict:
            cls.seq_update(iterable.items())
        elif type(iterable) == tuple:
            cls.nonseq_update(iterable)
        else:
            raise TypeError("Type given to update is wrong, only iterators are allowed.")

        return True

    def tostr(cls):
        return cls.__dict__.__str__()

    def fromdict(cls, seq):
        for key, value in seq.items():
            object.__setattr__(cls, key, value)

    def get(cls, key):
        r = False
        if key in cls.__dict__.keys(): r = object.__getattribute__(cls, key)

        return r

    def popitem(cls, key):
        return object.__delattr__(cls, key)

    def items(cls):
        items_dict = {}

        for key, value in zip(cls.lattributes(), cls.lvalues()): items_dict[key] = value

        return items_dict

    def addDict(cls):
        """
        This one is a little bit particular, has also nothing to do with drugs
        :return:
        """
        

    #Future operations, such as joins, left joins, outer joins, inner joins and unions should be supported
    #Sort of a pythonic SQL like operations

class asdict(metaclass=MetaTransform):
    """
    asdict is meant to be inherited, making the metaclass propagate to your own classes (no community transmission tho)
    """
    pass

class generic(asdict):
    """
    Generic item for those who do not want the metaclass to propagate like covid-19
    """
    pass

class MetaDataframe(type):
    """
    Metaclass binds methods to the class that is being created, rather than to the only one that inherits this behaviour
    """

    def __new__(mcs, classname, bases, classDict, *args):
        classDict['__len__'] = dict.__len__ #If you want to integrate it with pandas, this will have to change
        classDict['__getitem__'] = mcs.__getitem__ # Gets item according to attribute
        classDict['__setitem__'] = mcs.__setitem__ #Set item controls columns are same length + checks item is List (or subclass of list)
        classDict['__repr__'] = mcs.__repr__ # Set repr as iter more or less
        classDict['__iter__'] = mcs.__iter__ #We want to define how to iter, since it's over every attribute (which is a list)
        classDict['lattributes'] = mcs.lattributes
        classDict['lvalues'] = mcs.lvalues
        classDict['fromdict'] = mcs.fromdict
        classDict['items'] = mcs.items
        classDict['get'] = mcs.get
        classDict['pop'] = mcs.popitem

        return super().__new__(mcs, classname, bases, classDict)

    def __getitem__(cls, item): # Get item as list index or name :D
        if type(item) == int:
            item = str(item)

        if item not in cls.lattributes():
            item = cls.lattributes()[int(item)]

        return object.__getattribute__(cls, item)

    def __setitem__(cls, key, value): #Enable setting attributes as column names or list names, who cares let's do everything
        if type(value) != list:
            raise TypeError("Column has to be a list class, or subclass.")

        if type(key) == int:
            key = str(key)

        return object.__setattr__(cls, key, value)

    def __iter__(cls): #Return a tuple of values (lists) per attribute, can also define __next__ on next iterations (of the code, not the loop lol)
                       # Curiously this does not work with ```return cls.lvalues()``` (which returns a list)
        return (cls.__getitem__(key) for key in cls.lattributes())

    def __repr__(cls):
        return (cls.__getitem__(key) for key in cls.lattributes())

    def lattributes(cls):
        return list(cls.__dict__.keys())

    def lvalues(cls):
        return list(cls.__dict__.values())

    def tostr(cls):
        return cls.__dict__.__str__()

    def fromdict(cls, seq):
        for key, value in seq.items():
            object.__setattr__(cls, key, value)

    def get(cls, key):
        r = False
        if key in cls.__dict__.keys(): r = object.__getattribute__(cls, key)

        return r

    def popitem(cls, key):
        return object.__delattr__(cls, key)

    def items(cls):
        return list(zip(cls.lattributes(), cls.lvalues()))

    def addDict(cls):
        """
        This one is a little bit particular, has also nothing to do with drugs
        :return:
        """
        pass

class weirdDataframe(metaclass=MetaDataframe):
    """This class needs more definitions, if this is to be a Dataframe it also needs same length on all attributes"""
    pass


__all__ = ['generic', 'asdict', 'weirdDataframe']


