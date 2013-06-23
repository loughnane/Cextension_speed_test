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

static PyObject *
addition(PyObject *self,PyObject *args)
{
	int a,b,c;
	a=1;
	b=2;
	c= a + b;
	// printf("%d\n",c);
	return Py_None;
}



static PyMethodDef HelloMethods[] = {
    {"hello",  hello, METH_VARARGS,"Print Hello World"},
    {"addition",addition,METH_VARARGS,"Do some simple addition"},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

PyMODINIT_FUNC
inithello(void)
{
    (void) Py_InitModule("hello", HelloMethods);
    (void) Py_InitModule("addition",HelloMethods);
}