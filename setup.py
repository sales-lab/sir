from setuptools import setup, find_packages

setup(
    name='sir',
    version='0.4.0',
    description='SIR Infection Model',
    long_description="""\
Numerical solver for the SIR infection model by Kermack and McKendrick.
""",
    author='Gabriele Sales',
    author_email='gabriele.sales@unipd.it',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'ipywidgets',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
)
