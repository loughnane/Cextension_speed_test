Cextension_speed_test
=====================

A quick example of the kind of speedup you can achieve by using C extensions in place of using 
`Popen` to call separate C functions.


Instructions
----

First, compile the helloworld.c example. This is what is going to be called from python via `Popen`

```
$ make helloworld
```

Next, build and install the C extension

```
$ python setup.py build
$ sudo python setup.py install
```

Lastly, run `helloworld.py`. This will compare the `Popen` method and the C extension method.

```
$ python helloworld.py
```

Sample Output
----
```
$ python helloworld.py 
This is from Popen
This is from Popen
This is from Popen
This is from Popen
This is from Popen
This is from Popen
This is from Popen
This is from Popen
This is from Popen
This is from Popen
This is from the extension
This is from the extension
This is from the extension
This is from the extension
This is from the extension
This is from the extension
This is from the extension
This is from the extension
This is from the extension
This is from the extension
Popen Average:   	1757.69329071 us per loop
Cextension Average:	13.0891799927 us per loop
```
