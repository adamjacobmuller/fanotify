from setuptools import setup, find_packages

setup(
    name='fanotify',
    version='0.0.1',
    author='Adam Jacob Muller',
    packages=['fanotify'],
    author_email='adam@isprime.com',
    install_requires=[
        'ctypes'
    ]
)
