/**
 *  Python wrapper for libui.
 *
 */

#include <Python.h>
#include "ui.h"


/* ------------------ */
/*      uiWindow      */
/* ------------------ */

typedef struct {
    PyObject_HEAD
    uiWindow *uiWindow;
} py_uiWindow;

static PyTypeObject py_uiWindowType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    "pylibui.uiWindow",        /* tp_name */
    sizeof(py_uiWindow),       /* tp_basicsize */
    0,                         /* tp_itemsize */
    0,                         /* tp_dealloc */
    0,                         /* tp_print */
    0,                         /* tp_getattr */
    0,                         /* tp_setattr */
    0,                         /* tp_as_async */
    0,                         /* tp_repr */
    0,                         /* tp_as_number */
    0,                         /* tp_as_sequence */
    0,                         /* tp_as_mapping */
    0,                         /* tp_hash  */
    0,                         /* tp_call */
    0,                         /* tp_str */
    0,                         /* tp_getattro */
    0,                         /* tp_setattro */
    0,                         /* tp_as_buffer */
    Py_TPFLAGS_DEFAULT,        /* tp_flags */
    "uiWindow object",         /* tp_doc */
};
