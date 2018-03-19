import jinja2, json, os
from datamodel.datamodel import Car, Mod
from datamodel.classes import Classes

def parse_mod_json():
    """Reads the generated JSON file for modifications.

    Returns:
        A dictionary of Mod objects as values, with categories as keys.
    """
    with open(os.path.join('datamodel', 'mods.json')) as mod_f:
        mod_json = json.loads(mod_f.read())
    
    lastupdate = mod_json.get('lastupdate')
    modnames = [] # used to make sure mod names are unique
    mods = {}
    for m in mod_json.get('mods', []):
        if m.get('name') in modnames:
            raise ValueError("Mod name " + str(m.get('name'))+" already in use")
        modnames.append(m.get('name'))
        category = m.get('category', 'unspecified').title()
        if mods.get(category):
            mods[category].append(Mod(m))
        else:
            mods[category] = [Mod(m)]

    return mods, lastupdate

def generate_classmap():
    """Create a map of classes and their allowances inherited in other classes.
    
    Returns:
        A dictionary map.
    """
    classmap = {}
    for thisclass in Classes.get():
        # check other classes and add if this class is in their inherits list
        classmap[thisclass] = [c for c in Classes.get() if thisclass in
                [cc.shortname for cc in Classes.get(c).inherits]]
    return classmap

def generate_html(classlist, modlist):
    """Generate the HTML file given class and mod information.
    
    Returns:
        HTML file as a string.
    """
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(
            os.getcwd(), 'templates')))
    template = env.get_template('classpicker.j2')

    javascript_code = [] # used to generate javascript for the HTML template
    classmap = generate_classmap()
    for category in modlist:
        for mod in modlist[category]:
            # get full list of allowed classes
            allowed_classes = set(mod.allowed_class)
            for ac in mod.allowed_class:
                allowed_classes.update(classmap[ac])

            # add javascript for this mod
            javascript_code.append('if(is_c("' + mod.name + '")) set_class([' +
                    ', '.join([('"' + c + '"') for c in allowed_classes]) +
                    ']);')
            
    html_vars = {
        'modlist': modlist,
        'classes': Classes.ids(),
        'js': '\n'.join(javascript_code),
    }
    return template.render(html_vars)

if __name__ == '__main__':
    mods, mod_lastupdate = parse_mod_json()
    htmlstring = generate_html(None, mods)
    with open(os.path.join('html', 'classpicker.html'), 'w') as html_f:
        html_f.write(htmlstring)
