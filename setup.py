from setuptools import setup

setup(
    name='hyp',
    version='0.3.1-fb',
    packages=['hyp', 'hyp.adapters'],
    license='MIT',
    author='Joakim Ekberg',
    author_email='jocke.ekberg@gmail.com',
    url='https://github.com/kalasjocke/hyp',
    description='Partial JSON API implementation in Python on top of Schematics',
    long_description=open('README.md').read(),
    install_requires=open('requirements.txt').read().split(),
)
