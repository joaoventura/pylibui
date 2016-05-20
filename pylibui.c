#include <Python.h>
#include <stdio.h>


static PyObject *
pylibui_hello(PyObject *self)
{
    return Py_BuildValue("s", "Hello World");
}

static PyObject *
pylibui_greet(PyObject *self, PyObject *args)
{
    char *name;
    char message[50];

    if (!PyArg_ParseTuple(args, "s", &name))
        return NULL;

    sprintf(message, "Hello %s!", name);
    return Py_BuildValue("s", message);
}

static PyMethodDef PylibuiMethods[] = {
    {"hello", (PyCFunction) pylibui_hello, METH_VARARGS,
     "Returns an hello message."},
    {"greet", (PyCFunction) pylibui_greet, METH_VARARGS,
     "Greets the user."},

    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef pylibuimodule = {
   PyModuleDef_HEAD_INIT,
   "pylibui",         /* name of module */
   "pylibui",         /* module documentation, may be NULL */
   -1,                /* size of per-interpreter state of the module,
                         or -1 if the module keeps state in global variables. */
   PylibuiMethods
};

PyMODINIT_FUNC
PyInit_pylibui(void)
{
    return PyModule_Create(&pylibuimodule);
}
