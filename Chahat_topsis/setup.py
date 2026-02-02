from setuptools import setup, find_packages

setup(
    name="Topsis-Chahat-102303831",
    version="1.0.2",
    author="Chahat",
    description="A Python package implementing TOPSIS for MCDM problems",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["pandas", "numpy", "openpyxl"],
    entry_points={
        "console_scripts": [
            "topsis=topsis.topsis:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
