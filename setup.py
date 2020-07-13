import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="nbcheck",
    version="0.0.1",
    author="Tan Nian Wei",
    author_email="tannianwei@aggienetwork.com",
    description="Simple CLI tool to highlight Jupyter cells run out of order",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tnwei/nbcheck",
    package_dir={"": "src"},
    packages=setuptools.find_namespace_packages(where="src"),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        "console_scripts": [
            "nbcheck = nbcheck:cli_nbcheck",
         ]
    }
)
