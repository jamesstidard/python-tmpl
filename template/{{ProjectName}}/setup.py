import re
from distutils.core import setup


with open('{{PackageName}}/__init__.py', 'r') as fd:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
        fd.read(), re.MULTILINE).group(1)


test_requirements = ['pytest']

setup(
    name='{{PackageName}}',
    version=version,
    description='{{Description}}',
    url='https://github.com/{{GitHubRepository}}',
    license='{{License}}',
    packages=['{{PackageName}}'],
    author='{{Author}}',
    author_email='{{Email}}',
    platforms=['any'],
    tests_require=test_requirements,
    extras_require={'test': test_requirements},
    classifiers=(
        'Natural Language :: English',
        'Programming Language :: Python'))
