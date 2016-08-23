"""
Script to fetch citation data given DOIs
"""

from setuptools import find_packages, setup

package = 'fetch_bibtex_cite'
version = '0.1.0'
dependencies = [
    'click',
    'requests'
]

setup(
    name=package,
    version=version,
    packages=find_packages(),
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'fetch_bibtex_cite = fetch_bibtex_cite.cli:get_cite'
        ]
    }
)
