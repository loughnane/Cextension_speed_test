def hello_Popen():
	Popen(["./helloworld"])

def addition_Popen():
	Popen(["./addition"])





def hello_cextension():
	hello()

def addition_cextension():
	addition()



def hello_Python():
	print "This is from Python"

def addition_Python():
	a=1
	b=2
	c=a+b



if __name__ == '__main__':
    import timeit
    import time
    from subprocess import Popen
    from hello import hello,addition
    number=100
    sleepy=0.1
    popen_hello_time=(timeit.timeit("hello_Popen()", setup="from __main__ import hello_Popen",number=number))
    popen_addition_time=(timeit.timeit("addition_Popen()",setup="from __main__ import addition_Popen",number=number))
    time.sleep(sleepy)
    cextension_hello_time=(timeit.timeit("hello_cextension()",setup="from __main__ import hello_cextension",number=number))
    cextension_addition_time=(timeit.timeit("addition_cextension()",setup="from __main__ import addition_cextension",number=number))
    time.sleep(sleepy)
    python_hello_time=(timeit.timeit("hello_Python()",setup="from __main__ import hello_Python",number=number))
    python_addition_time=(timeit.timeit("addition_Python()",setup="from __main__ import addition_Python",number=number))


    print "Hello Averages:"
    print "Python: 	{} us per loop".format(python_hello_time/number*1e6)
    print "Popen: 		{} us per loop".format(popen_hello_time/number*1e6)
    print "Cextension:	{} us per loop".format(cextension_hello_time/number*1e6)
    print " "
    print "Addition Averages"
    print "Python: 	{} us per loop".format(python_addition_time/number*1e6)
    print "Popen: 		{} us per loop".format(popen_addition_time/number*1e6)
    print "Cextension:	{} us per loop".format(cextension_addition_time/number*1e6)