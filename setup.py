import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pinmypy",
    version="0.1.0",
    author="Raphael \"rGunti\" Guntersweiler",
    author_email="raphael@rgunti.ch",
    description="PinMyPy is a python-based client for PinMyPi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rGunti/PinMyPy",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Languages :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    )
)
