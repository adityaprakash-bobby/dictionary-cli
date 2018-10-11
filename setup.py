from setuptools import setup

setup (
    name="Dictionary-CLI",
    version="1.0.0",
    py_modules="diction",
    install_requires=[
        "Click",
        "requests",
    ],
    entry_points='''
        [console_scripts]
        diction=diction:cli
    ''',
)
