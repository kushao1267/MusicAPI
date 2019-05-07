import io
import os

from setuptools import setup, find_packages

import mozart

here = os.path.abspath(os.path.dirname(__file__))
# Import the README and use it as the long-description.
with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='mozart',
    python_requires='>=3.6.0',
    # If your package is a single module, use this instead of 'packages':
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    entry_points={
        'console_scripts': ['mozart = mozart.cli:app_main']
    },
    version=mozart.__version__,
    description='Nice API for developers who like music™',
    long_description=long_description,
    author=mozart.__author__,
    author_email='jianliu001922@gmail.com',
    url='https://github.com/kushao1267/MusicAPI',

    keywords=['music', 'api', 'mozart'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Multimedia',
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Utilities'
    ],
    install_requires=required,
    include_package_data=True,
)
