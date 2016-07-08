
from os.path import join, dirname
from setuptools import setup


setup(
    name='pymule',
    version='0.0.0',

    description='a muling tool for Diablo II LoD',
    long_description=open(join(dirname(__file__), 'README.md')).read(),

    packages=[
        'pymule',
    ],

    entry_points={
        'console_scripts': [
            'pymule = pymule.__main__:main'
        ]
    },

    install_requires=[],

    test_suite='tests',
    tests_require=[
        'pytest',
    ],

    setup_requires=['pytest_runner'],
)
