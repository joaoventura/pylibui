/**
 *  Python wrapper for libui.
 *
 */

#include <Python.h>
#include "ui.h"


// Test functions
extern PyObject *pylibui_test(PyObject *m);

// uiWindow functions
extern void register_uiWindowType(PyObject *m);
extern PyObject *py_uiNewWindow(PyObject *m, PyObject *args);
