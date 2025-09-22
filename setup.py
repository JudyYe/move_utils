from setuptools import setup, find_packages

setup(
    name='move_utils',  # Name of your package
    version='0.1.0',  # Initial version of your package
    packages=find_packages(),  # Automatically find and include all packages
    description='Utility functions for MPI projects',  # Short description
    author='JudyYe',  # Your name or your organization's name
    author_email='yufeiy2@stanford.edu',  # Your contact email
    install_requires=[
        # Any dependencies your package:
        'hydra-core>=1.2',  # Specify the version you need
        'cloudpickle>=3.0',  # Specify the version you need
        'submitit',
        # Add as many as your package requires
    ],
    extras_require={
        'dev': [
            # Optional dependencies for development
            'pytest>=6.0',
            # etc.
        ],
    },
    # If your package includes data files or other resources, configure them here
    package_data={
        # 'package_name': ['data/*.dat'],
    },
    entry_points={
        # If your package defines any command-line interfaces, define them here
        # 'console_scripts': ['my-command=mpi_utils.module:function'],
    },
)