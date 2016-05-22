/**
 *  Python wrapper for libui.
 *
 */

#include "pylibui.h"
#include "objects.h"


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
    py_uiWindow *window;
    const char *title;
    int width, height, hasMenubar;

    if (!PyArg_ParseTuple(args, "siii", &title, &width, &height, &hasMenubar))
        return NULL;

    window = PyObject_New(py_uiWindow, &py_uiWindowType);
    if (window == NULL)
        return NULL;

    window->uiWindow = uiNewWindow(title, width, height, hasMenubar);

    return (PyObject *) window;
}
