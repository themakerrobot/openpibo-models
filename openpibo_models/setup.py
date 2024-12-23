from setuptools import setup
from openpibo_models import __version__ as VERSION

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
]

test_requirements = [
]

setup(
    name='openpibo_models',
    version=VERSION,
    description="Models used by the openpibo-python package.",
    long_description=readme,
    author="circulus",
    author_email='leeyunjai@circul.us',
    url='https://github.com/themakerrobot/openpibo_models',
    packages=[
        'openpibo_models',
    ],
    package_dir={'openpibo_models': 'openpibo_models'},
    package_data={
        'openpibo_models': ['models/*']
    },
    install_requires=requirements,
    zip_safe=False,
    keywords='openpibo',
    classifiers=[
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',        
    ],
    test_suite='tests',
    tests_require=test_requirements
)
