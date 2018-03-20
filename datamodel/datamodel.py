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
                if any([c not in Classes.getlist() for c in v]):
                    raise ValueError("Invalid class for " +mod_dict.get('name'))

            setattr(self, k, v)

    def __str__(self):
        return (str(self.name) + ' (' + str(self.description) + '): ' +
                ', '.join(self.allowed_class))

class Vehicle(object):
    """Vehicle descriptor class.
    
    Expected parameters:
        yearmin: Earliest year to match this vehicle.
        yearmax: Latest year to match this vehicle.
        make: Make of the vehicle.
        model: Model of the vehicle.
        trim: Trim level of the vehicle.
        class_street: Street class for this vehicle.
        class_str_touring: Street Touring class for this vehicle.
        class_str_prep: Street Prepared class for this vehicle.
        class_str_mod: Street Modified class for this vehicle.
        class_prep: Prepared class for this vehicle.
        class_mod: Modified class for this vehicle.
    """
    def __init__(self, vehicle_dict):
        if (not vehicle_dict.get('make') or not vehicle_dict.get('model') or
                not vehicle_dict.get('class_street')):
            raise ValueError("Vehicle dictionary missing parameter(s): " +
                    str(vehicle_dict))
        for k, v in vehicle_dict.items():
            setattr(self, k, v)

        if not hasattr(self, "yearmin"):
            self.yearmin = None
        if not hasattr(self, "yearmax"):
            self.yearmax = None
        if not hasattr(self, "class_str_touring"):
            self.class_str_touring = None
        if not hasattr(self, "class_str_prep"):
            self.class_str_prep = None
        if not hasattr(self, "class_str_mod"):
            self.class_str_mod = None
        if not hasattr(self, "class_prep"):
            self.class_prep = None
        if not hasattr(self, "class_mod"):
            self.class_mod = None

    def __str__(self):
        return (str(self.yearmin) + '-' + str(self.yearmax) + ' ' +
                str(self.make) + ' ' + str(self.model) + ' ' +
                (str(self.trim) if hasattr(self, 'trim') else ''))

class VehicleData(object):
    """A collection of Vehicle objects.  This class provides functions to
    search, reorder or collect data in different ways.    
    """
    def __init__(self, vehiclelist):
        self.vehiclelist = vehiclelist

    def __iter__(self):
        return iter(self.vehiclelist)

    def search(self, make=None, model=None):
        foundlist = []
        for vehicle in self.vehiclelist:
            if (((make and vehicle.make == make) or not make) and
                    ((model and vehicle.model == model) or not model)):
                foundlist.append(vehicle)
        return foundlist
