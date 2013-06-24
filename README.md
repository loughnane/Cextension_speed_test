Cextension_speed_test
=====================

A quick performance comparison of using native Python, Python's `Popen` function, and custom 
C extensions to run small chunks of code. Specifically:

*A function that prints a small string
*A function that adds two hard-coded integers
*A function that adds to integers taken as arguments

Instructions
----

First, make the files that will be called from python via `Popen`

```
$ make all
```

Next, install the C extension

```
$ sudo python setup.py install
```

Lastly, run `speedTest.py`. This will compare the `Popen` method and the C extension method.

```
$ python speedTest.py
```

Sample Output
----
```
$ python helloworld.py 
This is from Popen
...
...
This is from the extension
...
...
This is from Python
...
...
Hello Averages:
Python: 	9.79900360107 us per loop
Popen: 		1905.10749817 us per loop
Cextension:	8.79764556885 us per loop
 
Addition Averages
Python: 	0.810623168945 us per loop
Popen: 		1633.50105286 us per loop
Cextension:	0.786781311035 us per loop
 
Addition with Input Averages
Python:          0.691413879395 us per loop
Popen:           6317.59166718 us per loop
Cextension:      1.19209289551 us per loop

```