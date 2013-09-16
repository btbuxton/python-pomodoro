from setuptools import setup, find_packages

setup(
    name="pomodoro",
    packages=find_packages(exclude="tests"),
    package_data = {'': ['*.xml']},
    install_requires=["mock>=1.0.1",],
)
