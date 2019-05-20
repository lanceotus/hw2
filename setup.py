from setuptools import setup, find_packages

setup(
    name='words_count',
    version='2.0',
    packages=find_packages(),
    install_requires=[
        'nltk ~= 3.4',
    ],
    entry_points={
        'console_scripts': ['words_count=words_count:main'],
    }
)
