from setuptools import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
   name='numerize',
   version='0.11',
   description='Convert large numbers into readable numbers for humans.',
   long_description=long_description,
   long_description_content_type='text/markdown',
   author='David Sa',
   author_email='davidsa03@gmail.com',
   packages=['numerize'],  #same as name
   url='https://github.com/davidsa03/numerize',
   license='MIT',
   install_requires=[
      # -*- Extra requirements: -*-
   ],
)
