import pathlib
from setuptools import setup, find_packages
from version import __version__ as version


HERE = pathlib.Path(__file__).parent

long_description = (HERE / "readme.md").read_text()


setup(
    name='pearson',
    version=version,
    packages=find_packages(),
    author='mjfactor',
    url='https://github.com/mjfactor/Mr-Pearson',
    author_email='emjayfactor@gmail.com',
    description='A simple chatbot that can be trained to answer questions based on a dataset',
    long_description= long_description,
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
        'nltk',
        'torch'
    ],
    include_package_data=True,
    python_requires='>=3.7',
    package_data={'': ['readme.md']}
)
