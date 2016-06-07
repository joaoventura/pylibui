"""
 Generate the basic structure of pylibui binding files
 from the libui header file.

 The output of this script is not guaranteed to be correct
 python scripts but are nevertheless better than writing
 everything manually.

"""


def return_lines(filename, start, end):
    """
    Returns only the lines of a file between start and end.

    :param filename: the filename
    :param start: first line
    :param end: last line
    :return: list of lines
    """

    lines = []

    with open(filename, 'r') as fin:

        for lineno, line in enumerate(fin, 1):
            if start <= lineno <= end:
                lines.append(line.strip())

    return lines


def generic_head():
    """
    Generates a generic header of a pylibui wrapper file.

    :return: string
    """

    return (
        '"""\n'
        ' Python wrapper for libui.\n'
        '\n'
        '"""\n'
        '\n'
        'import ctypes\n'
        'from . import clibui\n\n\n'
    )


def generic_struct(name):
    """
    Wraps a C struct in an empty ctypes class.

    :param name: the struct name
    :return: string
    """

    text = (
        'class {name}(ctypes.Structure):\n'
        '    """Wrapper for the {name} C struct."""\n'
        '\n'
        '    pass\n\n\n'
    )

    return text.format(name=name)


def generic_cast(name):
    """
    Generates a function to cast pointers.

    :param name: the pointer name
    :return: string
    """

    text = (
        'def {name}Pointer(obj):\n'
        '    """\n'
        '    Casts an object to {name} pointer type.\n'
        '\n'
        '    :param obj: a generic object\n'
        '    :return: {name}\n'
        '    """\n'
        '\n'
        '    return ctypes.cast(obj, ctypes.POINTER({name}))\n\n\n'
    )

    return text.format(name=name)


def generic_function(function):
    """
    Generates a generic function from function declaration

    :param function: function declaration
    :return: string
    """

    signature = function
    rtype, function = function.split(' ', 1)
    fname, fargs = function.split('(', 1)

    fname = fname.replace('*', '')
    fargs = fargs.replace(');', '')

    text = (
        '# - {signature}\n'
        'def {fname}(*args):\n'
        '    """\n'
        '    Describe the function.\n'
        '\n'
        '    :param args: arguments\n'
        '    :return: value\n'
        '    """\n'
        '\n'
        '    # TODO\n'
        '    return clibui.{fname}()\n\n\n'
    )

    return text.format(fname=fname, signature=signature, args=fargs)


def parse_lines(lines):
    """
    Parses the lines of a header file.

    :param lines: list of lines
    :return: string
    """

    contents = generic_head()

    for line in lines:

        # Definition of structs
        if line.startswith('typedef struct'):
            name = line.split()[2].strip()
            contents += generic_struct(name)

        # Definition of pointer casts
        elif line.startswith('#define') and '(this)' in line:
            fname = line.split()[1].strip()
            name = fname.split('(this)')[0]
            contents += generic_cast(name)

        # Functions
        elif line.startswith('_UI_EXTERN'):
            function = line.split(' ', 1)[1].strip()
            contents += generic_function(function)

    return contents


def parse_content(filename, start, end):
    """
    Parses the content of the libui header file between the
    start and end lines.

    :param filename: libui header file
    :param start: start line
    :param end: end line
    :return: string
    """

    lines = return_lines(filename, start, end)
    return parse_lines(lines)


def parse_section(name, filename):
    """
    Parses a section of the libui header as defined in the
    sections dictionary.

    :param name: section name
    :param filename: libui header file
    :return: string
    """

    global sections
    section = sections[name]

    return parse_content(filename, section[0], section[1])


# You should regularly check the sections for the target 'ui.h' file.

sections = {
    'main': [28, 46],
    'control': [48, 87],
    'window': [89, 97],
    'button': [99, 104],
    'box': [106, 113],
    'entry': [115, 122],
    'checkbox': [124, 131],
    'label': [133, 137],
    'tab': [139, 147],
    'group': [149, 156],
    'spinbox': [163, 168],
    'progressbar': [170, 175],
    'slider': [177, 181],
    'separator': [183, 185],
    'combobox': [187, 193],
    'editablecombobox': [195, 202],
    'radiobuttons': [204, 207],
    'datetimepicker': [209, 213],
    'multilineentry': [215, 225],
    'menuitem': [227, 233],
    'menu': [235, 248],
}


contents = parse_section('window', 'ui.h')
print(contents)
