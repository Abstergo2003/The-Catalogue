from setuptools import setup, find_packages
import os

# We will read the README file if it exists
long_description = ""
if os.path.exists("README.md"):
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

setup(
    name="pamd_eurocodes",  # The pip install name
    version="0.3.0",
    author="Abstergo2003",
    description="Eurocodes ported to python library.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Abstergo2003/PyAct",
    # find_packages will search for any folders with an __init__.py file
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[],
)
