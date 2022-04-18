from setuptools import setup, find_packages

setup(
    name="serializer",
    packages=find_packages(),
    version="1.0.0",
    author="Eroschenko",
    author_email='deniserochenko@gmail.com',
    url='https://github.com/denisero21/ISP-2022-053503',
    scripts=["serializer/serializer.py", "__main__.py", "tests.py"]
)
