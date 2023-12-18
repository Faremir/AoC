from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="AoC",
    version="2023.0.0.0",
    license="GNU 3",
    author="Faremir",
    author_email="j.faremir.b@gmail.com",
    description="Advent of Code solutions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.11",
)
