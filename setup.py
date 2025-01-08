from setuptools import setup

setup(
    name='pacmanbar',
    version='0.1',
    description='Load bar in pacman style',
    py_modules=['src.pacman_bar'],
    package_dir={'': 'src'},
    install_requires=[],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Axewood666/pacman_loadbar',
    author='Igor Zhugar'
)