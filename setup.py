from setuptools import setup, find_packages

setup(
    name='fanotify',
    version='0.0.2',
    author='Adam Jacob Muller',
    packages=['fanotify'],
    author_email='adam@isprime.com',
    entry_points={
        "console_scripts": [
            "fanotify = fanotify:main"
        ]
    }
)
