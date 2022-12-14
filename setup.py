import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "gauss-cli",
    version = "1.1.1",
    author = "messabih khalil",
    author_email = "msbih.khalil@gmail.com",
    description = "gussian elimination method package",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    install_requires=['commonmark', 'numpy', 'rich' , 'Pygments'],
)