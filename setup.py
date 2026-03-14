from setuptools import setup, find_packages

setup(
    name='scan_cards',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'scan-cards = main:main_function',
        ],
    },
    install_requires=[
        # Add your dependencies here
    ],
    python_requires='>=3.6',
)