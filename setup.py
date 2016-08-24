from distutils.core import setup
import io
import os.path

def read(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with io.open(filepath) as fp:
        text = fp.read()
    return text

setup(
    name='fastcomp',
    version='1.1.0',
    py_modules=['fastcomp'],
    author='Fujimoto Seiji',
    author_email='fujimoto@ceptord.net',
    url='https://github.com/fujimotos/fastcomp',
    description='Limited-but-faster computation of Levenshtein distance',
    long_description=read('README.md'),
    license='MIT',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
        'Topic :: Text Processing'
    ]
)
