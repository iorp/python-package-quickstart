from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'mypackage_hello = mypackage.hello:hello',
        ],
    },
)