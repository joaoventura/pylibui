/**
 *  Python wrapper for libui.
 *
 */

#include <Python.h>
#include "ui.h"


// Test functions
extern PyObject *pylibui_test(PyObject *m);
extern PyObject *pylibui_test_show_window(PyObject *m, PyObject *args);

// uiWindow functions
extern void register_uiWindowType(PyObject *m);
extern PyObject *py_uiWindowSetMargined(PyObject *m, PyObject *args);
extern PyObject *py_uiNewWindow(PyObject *m, PyObject *args);
