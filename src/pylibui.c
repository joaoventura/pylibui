#include <Python.h>
#include <stdio.h>
#include "ui.h"


/* Initialization and main loop functions */

static PyObject *
pylibui_init(PyObject *self)
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
pylibui_uninit(PyObject *self)
{
    uiUninit();
    Py_RETURN_NONE;
}

static PyObject *
pylibui_main(PyObject *self)
{
    uiMain();
    Py_RETURN_NONE;
}

/* Test functions */

static uiWindow *mainwin;

static int onClosing(uiWindow *w, void *data)
{
    uiControlDestroy(uiControl(mainwin));
    uiQuit();
    return 0;
}

static int shouldQuit(void *data)
{
    uiControlDestroy(uiControl(mainwin));
    return 1;
}

static PyObject *
pylibui_test(PyObject *self)
{
    uiMenu *menu;
    uiMenuItem *item;
    uiBox *box;
    uiLabel *label;

    menu = uiNewMenu("File");
    item = uiMenuAppendItem(menu, "Item");
    item = uiMenuAppendQuitItem(menu);
    uiOnShouldQuit(shouldQuit, NULL);

    mainwin = uiNewWindow("Window", 640, 480, 1);
    uiWindowSetMargined(mainwin, 1);
    uiWindowOnClosing(mainwin, onClosing, NULL);

    box = uiNewVerticalBox();
    uiBoxSetPadded(box, 1);
    uiWindowSetChild(mainwin, uiControl(box));

    label = uiNewLabel("Hello, World!");
    uiBoxAppend(box, uiControl(label), 0);

    uiControlShow(uiControl(mainwin));

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
    return PyModule_Create(&pylibuimodule);
}
