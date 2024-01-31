from setuptools import setup, find_packages

setup(
    name='quartoquest',
    version='0.1.0',  # Replace with your version
    packages=find_packages(),
    install_requires=[
        "radon",
        "GitPython"
    ],
    entry_points={
        'console_scripts': [
            'quartoquest-autograder = quartoquest.autograder:main',
        ],
    },
)

