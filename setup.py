from setuptools import setup

setup(
    name = "ukraine",
    version = "0.1.0",
    description = "Prints USA flag",
    author = "AitzazImtiaz",
    url = "https://github.com/AitzazImtiaz/ukraine",
    packages = ["ukraine"],
    entry_points = {
        'console_scripts': [
            'ukraine = ukraine.__main__:main'
        ]
    },
)
