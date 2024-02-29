from setuptools import setup,find_packages

'''
ModuleNotFoundError: No module named 'setuptools'
it's working fine after making some changes in the interpreter settings
refer YouTube: https://youtu.be/d_viFr3w4g8?si=66XckeDsEG2kHsqo
'''

setup(name='patternsextra',
      version='1.2',
      # packages=['patterns','com']
      packages=find_packages()
)