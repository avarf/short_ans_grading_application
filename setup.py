import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="grading_application",
    version="0.0.1",
    author="Ravikiran Bhat",
    author_email="ravikiranbhat243@gmail.com",
    description="Short answer grading assistant with active learning support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://upload.pypi.org/legacy/grading_application",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
