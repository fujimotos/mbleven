from distutils.core import setup


setup(
    name='fastcomp',
    version='1.2.0',
    py_modules=['fastcomp'],
    author='Fujimoto Seiji',
    author_email='fujimoto@ceptord.net',
    url='https://github.com/fujimotos/fastcomp',
    description='Limited-but-faster computation of Levenshtein distance',
    long_description="""The fastcomp is an efficient algorithm for computing (Damerau-)
Levenshtein distance **up to two**.

Given two strings of length m and n (m <= n), the
computation requires O(1) space and O(n) time, which is
much smaller and faster than well-known Wagner-Fisher algorithm.""",
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
    ]
)
