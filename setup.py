from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='numerize',
   version='0.5',
   description='Convert large numbers into readable numbers for humans.',
   long_description=long_description,
   author='David Sa',
   author_email='davidsa03@gmail.com',
   packages=['numerize'],  #same as name
   url='https://github.com/davidsa03/numerize',
   license='MIT',
   install_requires=[
      # -*- Extra requirements: -*-
   ],
)
