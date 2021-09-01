from setuptools import setup

# with open("README", 'r') as f:
#     long_description = f.read()
long_description = """README"""
setup(
    name='scikit-learn',
    version='0.22',
    description='Contains tools for statistical modelling, regression and clustering',
    license="MIT",
    long_description=long_description,
    author='David Cournapeau',
    url='https://scikit-learn.org/stable/',
    packages=['scikit-learn'],
    classifiers=[
        "License:: New BSD license",
        "Programming Language:: Python, C, C++, Cython",
        "Intended Audience :: Developers"
    ],
    install_requires=[
        'numpy',
        'scipy',
        'joblib',
        'threadpoolctl',
        'cython',
        'matplotlib',
        'scikit-image',
        'pandas',
        'seaborn',
        'memory_profiler'
      ],
)