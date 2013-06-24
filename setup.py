from distutils.core import setup, Extension

module1 = Extension('hello',
                    sources = ['extensions.c'])

setup (name = 'helloworld_extension',
       version = '0.0',
       description = 'This is a test for comparing Python, Popen, and C extensions',
       ext_modules = [module1])