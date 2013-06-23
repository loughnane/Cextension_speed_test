from distutils.core import setup, Extension

module1 = Extension('hello',
                    sources = ['helloworld_extension.c'])

setup (name = 'helloworld_extension',
       version = '0.0',
       description = 'This is a test for comparing Popen vs c extensions',
       ext_modules = [module1])