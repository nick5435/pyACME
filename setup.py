import setuptools
from setuptools import find_packages, setup
import os, platform


if platform.system() == "Linux":
    ACME_EXE = r"pyACME/bin/acme"
elif platform.system() == "Windows":
    ACME_EXE = r"pyACME/bin/acme.exe"



# def readme():
#     """Where the README file is."""
#     with open('README.md') as f:
#         return f.read()


setup(
    name='pyACME',
    version='0.1.0',
    description='Python interface to ACME',
    # long_description=readme(),
    url='https://github.com/nick5435/pyACME',
    author='Nick Meyer',
    author_email='nmeyer5435@gmail.com',
    license='GPLv3+',
    packages=find_packages(),
    zip_safe=False,
    setup_requires=[],
    install_requires=[
    ],
    extras_require={
        'dev': [],
    },
    python_requires='>=3.8.0',
    include_package_data=True,
    package_data={
        'bin': [ACME_EXE]
    },
    keywords="mathematics group-theory andrews-curtis",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3',
        'Natural Language :: English',
        'Environment :: Console',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
    )