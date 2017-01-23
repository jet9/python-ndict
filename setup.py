from setuptools import setup, find_packages

setup(
    name="ndict",
    version=__import__("ndict").__version__,
    description="A Python module that allows access to dict keys as object methods",
    long_description="A Python module that allows access to dict keys as object methods",
    author="Dmitry Kurbatov",
    author_email="dk@dimcha.ru",
    license="BSD",
    url="https://github.com/jet9/python-ndict",
    py_modules=['ndict'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
	"Programming Language :: Python :: 3"
    ]
)
