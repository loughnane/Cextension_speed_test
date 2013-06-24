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


static PyObject *
addition_with_inputs(PyObject *self,PyObject *args)
{
	int a;
	int b;
	int c;
	if (!PyArg_ParseTuple(args, "ii", &a, &b))
		return NULL;
	c=a+b;
	return Py_BuildValue("i",c);
}



static PyMethodDef HelloMethods[] = {
    {"hello",  hello, METH_VARARGS,"Print Hello World"},
    {"addition",addition,METH_VARARGS,"Do some simple addition"},
    {"addition_with_inputs",addition_with_inputs,METH_VARARGS,"Add some inputs together"},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

PyMODINIT_FUNC
inithello(void)
{
    (void) Py_InitModule("hello", HelloMethods);
    (void) Py_InitModule("addition",HelloMethods);
    (void) Py_InitModule("addition_with_inputs",HelloMethods);
}