#This is the file that needs to be run to install a python module

from distutils.core import setup, Extension
#the 'cextension' string on the line below is what we are going to "import" in our code.
module1 = Extension('cextension',
                    sources = ['extensions.c'])

setup (name = 'cextension',
       version = '0.0',
       description = 'This is a test for comparing Python, Popen, and C extensions',
       ext_modules = [module1])