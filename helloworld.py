def hello_Popen():
	Popen(["./helloworld"])

def hello_cextension():
	hello()

if __name__ == '__main__':
    import timeit
    import time
    from subprocess import Popen
    from hello import hello
    number=10
    popen_total_time=(timeit.timeit("hello_Popen()", setup="from __main__ import hello_Popen",number=number))
    time.sleep(0.1)
    cextension_total_time=(timeit.timeit("hello_cextension()",setup="from __main__ import hello_cextension",number=number))

    print "Popen Average: 		{} us per loop".format(popen_total_time/number*1e6)
    print "Cextension Average:	{} us per loop".format(cextension_total_time/number*1e6)