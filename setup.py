from setuptools import setup, find_packages
from os import path
from codecs import open

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pearson',
    version='1.1',
    packages=find_packages(),
    author='mjfactor',
    author_email='emjayfactor@gmail.com',
    description='A Dumb Chatbot, Please dont install me',
    long_description=open('readme.md').read(),
    long_description_content_type='text/markdown',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.10',
        "Operating System :: OS Independent"
    ],
    install_requires=[
        'numpy',
        'nltk',
        'torch'
    ],
    include_package_data=True
)