/**
 *  Python wrapper for libui.
 *
 */

#include "pylibui.h"


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
    "uiWindow objects",        /* tp_doc */
};


void register_uiWindowType(PyObject *m) {

    py_uiWindowType.tp_new = PyType_GenericNew;
    if (PyType_Ready(&py_uiWindowType) < 0)
        return;

    Py_INCREF(&py_uiWindowType);
    PyModule_AddObject(m, "uiWindow", (PyObject *) &py_uiWindowType);
}


PyObject *
py_uiNewWindow(PyObject *m, PyObject *args)
{
    py_window = PyObject_CallObject((PyObject *) &py_uiWindowType, NULL);
    if (py_window != NULL) {
        py_window->uiWindow = uiNewWindow("Window", 640, 480, 1);
    }

    return py_window;
}
