from setuptools import setup, find_packages

setup(
    name='dashboard_project1',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        # Add your dependencies here, for example:
        'Django>=3.0',
        'djongo>=1.3',
        'rest_framework>=3.12',
        # Add more dependencies as needed
    ],
)
