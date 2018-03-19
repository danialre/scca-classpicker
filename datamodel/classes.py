from collections import namedtuple

# note: using namedtuple instead of enum so we can use integer comparisons
# (this may change in the future)

Cls = namedtuple('Cls', ['name', 'shortname', 'id', 'inherits'])

class _classes(object):
    """SCCA Class definitions.
    """
    def __init__(self):
        self.STREET = Cls('Street', 'STREET', 1, [])
        self.STR_TOURING = Cls('Street Touring', 'STR_TOURING', 2,[self.STREET])
        self.STR_PREP = Cls('Street Prepared', 'STR_PREP', 3,
                [self.STREET, self.STR_TOURING])
        self.STR_MOD = Cls('Street Modified', 'STR_MOD', 4,
                [self.STREET, self.STR_TOURING, self.STR_PREP])
        self.PREP = Cls('Prepared', 'PREP', 5, [])
        self.XP = Cls('X Prepared', 'XP', 6, [self.PREP, self.STR_MOD])
        self.MOD = Cls('Modified', 'MOD', 11, [self.PREP])

    def __iter__(self):
        # allows iterating over Classes
        for x in [getattr(self, attrib) for attrib in self.get()]:
            yield x
    
    def getlist(self):
        """Simple getter for classes.
        """
        return ['STREET', 'STR_TOURING', 'STR_PREP', 'STR_MOD', 'PREP', 'XP', 'MOD']
        
    def get(self, name=None):
        """Get information about a specific class.
        """
        if not name:
            return { c: getattr(self, c) for c in self.getlist() }
        else:
            try:
                return getattr(self, name)
            except:
                return
        
    def ids(self):
        """Get IDs for each class attribute.
        """        
        return { c: getattr(self, c).id for c in self.getlist() }
Classes = _classes()
