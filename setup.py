try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__about__ = {}

with open("uareach/__about__.py") as fp:
    exec(fp.read(), None, __about__)

setup(
    name="uareach",
    version=__about__["__version__"],
    author="Airship Customer Engineering",
    author_email="customer-engineering@airship.com",
    url="https://airship.com/",
    description="Python package for using the Airship Wallet API",
    long_description=open('README.rst').read(),
    packages=["uareach"],
    license='BSD License',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=[
        'requests>=2.7',
        'six'
    ],
)
