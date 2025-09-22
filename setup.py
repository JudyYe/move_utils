from setuptools import setup, find_packages

setup(
    name='move_utils',
    version='0.1.0',
    packages=find_packages(),
    description='Utility functions for move cluster',
    author='JudyYe',
    author_email='yufeiy2@stanford.edu',
    install_requires=[
        'hydra-core>=1.2',
        'cloudpickle>=3.0',
        'submitit',
    ],
    extras_require={
        'dev': [
            'pytest>=6.0',
        ],
    },
    package_data={
    },
    entry_points={
    },
)