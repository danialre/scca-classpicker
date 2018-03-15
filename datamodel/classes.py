from collections import namedtuple

# note: using namedtuple instead of enum so we can use integer comparisons
# (this may change in the future)

Cls = namedtuple('Cls', ['name', 'id', 'inherits'])

class _classes(object):
    """SCCA Class definitions.
    """
    def __init__(self):
        self.STREET = Cls('Street', 1, [])
        self.STR_TOURING = Cls('Street Touring', 2, [self.STREET])
        self.STR_PREP = Cls('Street Prepared', 3, [self.STREET, self.STR_TOURING])
        self.STR_MOD = Cls('Street Modified', 4, [self.STREET, self.STR_TOURING, self.STR_PREP])
        self.PREP = Cls('Prepared', 5, [])
        self.XP = Cls('X Prepared', 6, [self.PREP])
        self.MOD = Cls('Modified', 11, [self.PREP])

    def __iter__(self):
        # allows iterating over Classes
        for x in [getattr(self, attrib) for attrib in self.get()]:
            yield x
        
    def get(self):
        """Simple getter for classes.
        """
        return ['STREET', 'STR_TOURING', 'STR_PREP', 'STR_MOD', 'PREP', 'XP', 'MOD']
    
    def ids(self):
        """Get IDs for each class attribute.
        """        
        return { c: getattr(self, c).id for c in self.get() }
Classes = _classes()

#_c = namedtuple('_Classes', ['STREET', 'STR_TOURING', 'STR_PREP', 'PREP',
#        'STR_MOD', 'XP', 'MOD'])

#Classes = _c(1, 2, 3, 4, 5, 6, 11)
