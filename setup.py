from setuptools import setup, find_packages

setup(
    name='morepath_reactredux',
    version='0.1.dev0',
    description="Morepath example of using React & Redux",
    author="Martijn Faassen",
    author_email="faassen@startifact.com",
    license="BSD",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'morepath',
        'webtest',
        'pytest'
    ],
    entry_points={
        'console_scripts': [
            'start = morepath_reactredux.main:main',
        ]
    },
)
