
#These functions use Popen to call compiled C functions
def hello_Popen():
    '''Starts a new process that calls the file compiled from hello.c'''
    Popen(["./hello"])

def addition_Popen():
    '''Starts a new process that calls the file compiled from addition.c'''
    Popen(["./addition"])

def addition_with_inputs_Popen():
    '''Starts a new process that calls the file compiled from addition_with_inputs.c'''
    Popen(["./addition_with_inputs"])


#These functions use C extensions that have been imported separately
def hello_cextension():
    '''calls the `hello` function from the cextension module'''
    hello()

def addition_cextension():
    '''calls the `addition` function from the cextension module'''
    addition()

def addition_with_inputs_cextension(a,b):
    '''calls the `addition_with_inputs` function from the cextension module'''
    addition_with_inputs(a,b)

#These are standard python functions

def hello_Python():
    '''implements a function analagous to hello.c and the `hello` function from the cextensions module'''
    print "This is from Python"

def addition_Python():
    '''implements a function analagous to addition.c and the `addition` function from the cextensions module'''
    a=1
    b=2
    c=a+b
def addition_with_inputs_Python(a,b):
    '''implements a function analagous to addition_with_inputs.c and the `addition_with_inputs` function from the cextensions module'''
    c=a+b


#this is run when speedTest.py is called from thecommand line
if __name__ == '__main__':
    from timeit import timeit #this module lets us time code
    from time import sleep
    from subprocess import Popen
    from cextension import hello,addition,addition_with_inputs

    number=10 #number of times to execute each code snippet
    sleepy=0.1 #dwell time to let the slower code finish


    #run the Popen versions of the functions
    popen_hello_time=(timeit("hello_Popen()", setup="from __main__ import hello_Popen",number=number))
    popen_addition_time=(timeit("addition_Popen()",setup="from __main__ import addition_Popen",number=number))
    popen_addition_with_inputs_time=(timeit("addition_with_inputs_Popen()",setup="from __main__ import addition_with_inputs_Popen",number=number))
    
    sleep(sleepy)
    
    #run the C extension versions of the functions
    cextension_hello_time=(timeit("hello_cextension()",setup="from __main__ import hello_cextension",number=number))
    cextension_addition_time=(timeit("addition_cextension()",setup="from __main__ import addition_cextension",number=number))
    cextension_addition_with_inputs_time=(timeit("addition_with_inputs_cextension(1,2)",setup="from __main__ import addition_with_inputs_cextension",number=number))
    
    sleep(sleepy)
    
    #run the native python versions of the functions
    python_hello_time=(timeit("hello_Python()",setup="from __main__ import hello_Python",number=number))
    python_addition_time=(timeit("addition_Python()",setup="from __main__ import addition_Python",number=number))
    python_addition_with_inputs_time=(timeit("addition_with_inputs_Python(1,2)",setup="from __main__ import addition_with_inputs_Python",number=number))



    #print out the results
    print "Hello Averages:"
    print "Python: 	{} us per loop".format(python_hello_time/number*1e6)
    print "Popen: 		{} us per loop".format(popen_hello_time/number*1e6)
    print "Cextension:	{} us per loop".format(cextension_hello_time/number*1e6)
    print " "
    print "Addition Averages"
    print "Python: 	{} us per loop".format(python_addition_time/number*1e6)
    print "Popen: 		{} us per loop".format(popen_addition_time/number*1e6)
    print "Cextension:	{} us per loop".format(cextension_addition_time/number*1e6)
    print " "
    print "Addition with Input Averages"
    print "Python:          {} us per loop".format(python_addition_with_inputs_time/number*1e6)
    print "Popen:           {} us per loop".format(popen_addition_with_inputs_time/number*1e6)
    print "Cextension:      {} us per loop".format(cextension_addition_with_inputs_time/number*1e6)
