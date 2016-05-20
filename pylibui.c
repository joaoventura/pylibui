#include <Python.h>
#include <stdio.h>
#include "ui.h"


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

    uiInitOptions o;
    const char *err;
    uiMenu *menu;
    uiMenuItem *item;
    uiBox *box;
    uiLabel *label;

    memset(&o, 0, sizeof (uiInitOptions));
    err = uiInit(&o);
    if (err != NULL) {
        fprintf(stderr, "error initializing ui: %s\n", err);
        uiFreeInitError(err);
        Py_RETURN_NONE;
    }

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
    uiMain();
    uiUninit();

    Py_RETURN_NONE;
}

static PyMethodDef PylibuiMethods[] = {
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
