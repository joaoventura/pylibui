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
    :param start: text of first line to match
    :param end: text of last line match
    :return: generator of lines between and including the matching lines
    """

    accumulate = False

    with open(filename, 'rt', encoding='utf-8') as fin:

        for line in fin:
            if not accumulate and start in line:
                accumulate = True
            if accumulate:
                yield line.strip()
            if accumulate and end in line:
                break


def generic_head():
    """
    Generates a generic header of a pylibui wrapper file.

    :return: string
    """

    return '''"""
 Python wrapper for libui.

"""

import ctypes
from . import clibui


'''


def generic_struct(name):
    """
    Wraps a C struct in an empty ctypes class.

    :param name: the struct name
    :return: string
    """

    return '''\
class {name}(ctypes.Structure):
    """Wrapper for the {name} C struct."""

    pass


'''.format(name=name)



def generic_cast(name):
    """
    Generates a function to cast pointers.

    :param name: the pointer name
    :return: string
    """

    return '''\
def {name}Pointer(obj):
    """
    Casts an object to {name} pointer type.

    :param obj: a generic object
    :return: {name}
    """

    return ctypes.cast(obj, ctypes.POINTER({name}))


'''.format(name=name)



def generic_function(function):
    """
    Generates a generic function from function declaration

    :param function: function declaration
    :return: string
    """

    signature = function
    rtype, function = function.split(None, 1)
    fname, fargs = function.split('(', 1)

    fname = fname.replace('*', '')
    fargs = fargs.replace(');', '')

    return '''\
# - {signature}
def {fname}(*args):
    """
    Describe the function.

    :param args: arguments
    :return: value
    """

    # TODO
    return clibui.{fname}()


'''.format(fname=fname, signature=signature, args=fargs)


def parse_lines(lines):
    """
    Parses the lines of a header file.

    :param lines: list of lines
    :return: string
    """

    contents = [generic_head()]

    for line in lines:

        # Definition of structs
        if line.startswith('typedef struct'):
            name = line.split()[2].strip()
            contents.append(generic_struct(name))

        # Definition of pointer casts
        elif line.startswith('#define') and '(this)' in line:
            fname = line.split()[1].strip()
            name = fname.split('(this)')[0]
            contents.append(generic_cast(name))

        # Functions
        elif line.startswith('_UI_EXTERN'):
            function = line.split(' ', 1)[1].strip()
            contents.append(generic_function(function))

    return ''.join(contents)


def parse_content(filename, start, end):
    """
    Parses the content of the libui header file between the
    start and end lines.

    :param filename: libui header file
    :param start: text of first line to match
    :param end: text of last line match
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

    section = sections[name]

    return parse_content(filename, section[0], section[1])


# You should regularly check the sections for the target 'ui.h' file.

# A section is from and including the first line that matches the first
# text up to and including the first line that matches the second text.
# Two or more words are used to make it more robust.
sections = {
    'main': ("uiInitOptions uiInitOptions;", "void uiFreeText(char"),
    'control': ("uiControl uiControl;",
                "void uiUserBugCannotSetParentOnToplevel(const"),
    'window': ("uiWindow uiWindow;", "uiWindow *uiNewWindow"),
    'button': ("uiButton uiButton;", "uiButton *uiNewButton"),
    'box': ("uiBox uiBox;", "uiBox *uiNewVerticalBox"),
    'entry': ("uiEntry uiEntry;", "uiEntry *uiNewEntry"),
    'checkbox': ("uiCheckbox uiCheckbox/", "uiCheckbox *uiNewCheckbox"),
    'label': ("uiLabel uiLabel;", "uiLabel *uiNewLabel"),
    'tab': ("uiTab uiTab;", "uiTab *uiNewTab"),
    'group': ("uiGroup uiGroup;", "uiGroup *uiNewGroup"),
    'spinbox': ("uiSpinbox uiSpinbox;", "uiSpinbox *uiNewSpinBox"),
    'progressbar': ("uiProgressBar uiProgressBar;",
                    "uiProgressBar *uiNewProgressBar"),
    'slider': ("uiSlider uiSlider;", "uiSlider *uiNewSlider"),
    'separator': ("uiSeparator uiSeparator;",
                  "uiSeparator *uiNewHorizontalSeparator"),
    'combobox': ("uiCombobox uiCombobox;", "uiCombobox *uiNewCombobox"),
    'editablecombobox': ("uiEditableCombobox uiEditableCombobox;",
                         "uiEditableCombobox *uiNewEditableCombobox"),
    'radiobuttons': ("uiRadioButtons uiRadioButtons;",
                     "uiRadioButtons *uiNewRadioButtons"),
    'datetimepicker': ("uiDateTimePicker uiDateTimePicker;",
                       "uiDateTimePicker *uiNewTimePicker"),
    'multilineentry': ("uiMultilineEntry uiMultilineEntry;",
                       "uiMultilineEntry *uiNewNonWrappingMultilineEntry"),
    'menuitem': ("uiMenuItem uiMenuItem;", "void uiMenuItemSetChecked"),
    'menu': ("uiMenu uiMenu;", "void uiMsgBoxError"),
}


contents = parse_section('window', 'ui.h')
print(contents)
