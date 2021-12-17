import setuptools
from distutils.version import StrictVersion
from importlib import import_module
from idtpy.version import __version__, __author__, __email__

with open("README.md", "r") as fh:
    long_description = fh.read()

short_description = """
Simple Python package for the design and modelling of Interdigital Transducers (IDTs).
"""

extras = {
    'numpy': ('numpy', '1.18', 'conda'),
    'scipy': ('scipy', '1.7', 'conda'),
    'gdspy': ('gdspy', '1.6', 'pip'),
    'matplotlib': ('matplotlib', '3.2', 'conda'),
}
extras_require = {k: '>='.join(v[0:2]) for k, v in extras.items()}

install_requires = [
    'numpy>=1.18',
    'scipy>=1.7',
]

setuptools.setup(
    name="idtpy",
    version=__version__,
    author=__author__,
    author_email=__email__,
    license='BSD-3-Clause',
    description=short_description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="",
    url="https://github.com/Junliang-Wang/idtpy",
    packages=setuptools.find_packages(exclude=["tests"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Intended Audience :: Customer Service",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
    ],
    python_requires='>=3.8',
    install_requires=install_requires,
    extras_require=extras_require
)

# Code below adapted from QCoDeS (https://qcodes.github.io/)

version_template = '''
*****
***** package {0} must be at least version {1}.
***** Please upgrade it (pip install -U {0} or conda install {0})
***** in order to use {2}
***** Recommended method: {3}
*****
'''

missing_template = '''
*****
***** package {0} not found
***** Please install it (pip install {0} or conda install {0})
***** Recommended: {2} install {0}
***** in order to use {1}
*****
'''

valueerror_template = '''
*****
***** package {0} version not understood
***** Please make sure the installed version ({1})
***** is compatible with the minimum required version ({2})
***** in order to use {3}
*****
'''

othererror_template = '''
*****
***** could not import package {0}. Please try importing it from
***** the commandline to diagnose the issue.
*****
'''

# now test the versions of extras
for extra, (module_name, min_version, install_method) in extras.items():
    try:
        module = import_module(module_name.lower())
        if StrictVersion(module.__version__) < StrictVersion(min_version):
            print(version_template.format(module_name, min_version, extra, install_method))
    except ImportError:
        print(missing_template.format(module_name, extra, install_method))
    except ValueError:
        print(valueerror_template.format(
            module_name, module.__version__, min_version, extra))
    except:
        print(othererror_template.format(module_name))
