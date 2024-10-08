from setuptools import setup, find_packages

setup(
    name="myproject",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'requests',
        'pandas'
    ],
    entry_points={
        'console_scripts': [
            'gab-scraper = cli_tool:main',
        ],
    },
)