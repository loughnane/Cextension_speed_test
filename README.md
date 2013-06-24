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
Python:   80.4686546326 us per loop
Popen: 		1529.25014496 us per loop
Cextension:	48.5014915466 us per loop
 
Addition Averages
Python: 	0.369548797607 us per loop
Popen: 		1381.39009476 us per loop
Cextension:	0.400543212891 us per loop
 
Addition with Input Averages
Python:  0.379085540771 us per loop
Popen:       65901.2103081 us per loop
Cextension:  657.98997879 us per loop
```
