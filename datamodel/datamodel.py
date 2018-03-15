from datamodel.classes import Classes

class Car(object):
    make = None
    model = None
    trim = None
    min_year = 0
    max_year = 0

class Mod(object):
    """Modification descriptor class.

    Expected parameters:
        name: Internal name of the modification as a string.
        description: Friendly description of the modification as a string.
        allowed_class: List of Classes that permit this modification. This must
            be one of the parameters of Classes (see classes.py).
    """
    def __init__(self, mod_dict):
        if (not mod_dict.get('name') or not mod_dict.get('description') or
                not mod_dict.get('allowed_class') or
                not mod_dict.get('category')):
            raise ValueError("Mod dictionary missing parameter(s): " +
                    str(mod_dict))

        for k, v in mod_dict.items():
            if k == 'allowed_class':
                if any([c not in Classes.get() for c in v]):
                    raise ValueError("Invalid class for " +mod_dict.get('name'))

            setattr(self, k, v)

    def __str__(self):
        return (str(self.name) + ' (' + str(self.description) + '): ' +
                ', '.join(self.allowed_class))
