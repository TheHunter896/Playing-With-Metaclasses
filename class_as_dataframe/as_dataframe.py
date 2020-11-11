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
        if not isinstance(value, list):
            raise TypeError("Column has to be a list class, or subclass.")

        if isinstance(key, int):
            key = str(key)

        return object.__setattr__(cls, key, value)

    def __iter__(cls): #Return a tuple of values (lists) per attribute, can also define __next__ on next iterations (of the code, not the loop lol)
                       # Curiously this does not work with ```return cls.lvalues()``` (which returns a list), it needs an iterator, why is a list not an iterator?
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

class asDataframe(metaclass=MetaDataframe):
    """This class needs more definitions, if this is to be a Dataframe it also needs same length on all attributes"""
    pass

__all__ = ['asDataframe']