from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="gceni_testing",
    version="0.0.1",
    author="GCeni",
    author_email="gceni10@gmail.com",
    description="only for testing purpose",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Err0rGCeni/DIOProject_Pacote_de_Processamento",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)