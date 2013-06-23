#include <Python.h> 
/*
This pulls in the python API, which includes
<stdio.h>,<string.h>, <errno.h>, and <stdlib.h> 
*/

static PyObject *
hello(PyObject *self,PyObject *args)
{
	puts("This is from the extension");
	return Py_None;
}

static PyMethodDef HelloMethods[] = {
    {"hello",  hello, METH_VARARGS,
     "Execute a shell command."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

PyMODINIT_FUNC
inithello(void)
{
    (void) Py_InitModule("hello", HelloMethods);
}