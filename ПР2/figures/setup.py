from setuptools import setup, find_packages

setup(
    name="geometry-figures",
    version="0.1.0",
    description="Геометрические фигуры: Circle и Triangle",
    packages=find_packages(),
    python_requires='>=3.8',
    install_requires=[],
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'mutpy==0.6.1',
        ],
    },
)
