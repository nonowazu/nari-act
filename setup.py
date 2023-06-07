from setuptools import setup, find_namespace_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

dev_requirements = [
    'mypy==0.942',
    'pylint==2.13.4',
]

docs_requirements = [
    'sphinx==5.2.3',
    'sphinx-rtd-theme==1.0.0',
    'myst-parser==0.18.1',
]

setup(
    name='nari-act',
    version='0.1.0',
    author='Nonowazu',
    author_email='oowazu.nonowazu@gmail.com',
    description='ACT-specific additions for nari',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.10',
    packages=find_namespace_packages(include=['nari.ext.*']),
    package_data={'nari.ext.act': ['py.typed']},
    install_requires=[
        'nari@git+https://github.com/xivlogs/nari.git@master'
    ],
    extras_require={
        'dev': dev_requirements,
        'docs': docs_requirements,
    },
)
