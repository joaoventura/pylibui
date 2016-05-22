/**
 *  Python wrapper for libui.
 *
 */

#include <Python.h>
#include <stdio.h>
#include "pylibui.h"


/* Initialization and main loop functions */

static PyObject *
pylibui_init(PyObject *m)
{
    uiInitOptions o;
    const char *err;

    memset(&o, 0, sizeof (uiInitOptions));
    err = uiInit(&o);
    if (err != NULL) {
        fprintf(stderr, "error initializing ui: %s\n", err);
        uiFreeInitError(err);
    }

    Py_RETURN_NONE;
}

static PyObject *
pylibui_uninit(PyObject *m)
{
    uiUninit();
    Py_RETURN_NONE;
}

static PyObject *
pylibui_main(PyObject *m)
{
    uiMain();
    Py_RETURN_NONE;
}

/* Module level definitions */

static PyMethodDef PylibuiMethods[] = {

    // Initialization and main loop
    {"init", (PyCFunction) pylibui_init, METH_VARARGS,
    "Initializes pylibui."},
    {"uninit", (PyCFunction) pylibui_uninit, METH_VARARGS,
    "Uninitializes pylibui."},
    {"main", (PyCFunction) pylibui_main, METH_VARARGS,
    "Execute main loop."},

    // Test
    {"test", (PyCFunction) pylibui_test, METH_VARARGS,
    "Tests pylibui."},
    {"test_show_window", (PyCFunction) pylibui_test_show_window, METH_VARARGS,
    "Tests pylibui."},

    // uiWindow functions
    {"uiNewWindow", (PyCFunction) py_uiNewWindow, METH_VARARGS,
    "Returns a uiWindow."},

    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef pylibuimodule = {
    PyModuleDef_HEAD_INIT,
    "pylibui",      /* name of module */
    "pylibui",      /* module documentation, may be NULL */
    -1,             /* size of per-interpreter state of the module,
                       or -1 if the module keeps state in global variables. */
    PylibuiMethods
};

PyMODINIT_FUNC
PyInit_pylibui(void)
{
    PyObject* m;

    m = PyModule_Create(&pylibuimodule);

    register_uiWindowType(m);

    return m;
}
