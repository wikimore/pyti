from setuptools import setup, find_packages


setup(
    name="pyti",

    version='0.2.2',

    description='Technical Indicator Library',
    long_description="This library contains various financial technical "
                     "indicators that can be used to analyze financial data.",

    url='https://github.com/wikimore/pyti',

    author='Kyle Justice Magnuson',
    author_email='kyle@topsteptrader.com',

    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Software Development',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.6',
    ],

    keywords='financial technical indicator functions',

    packages=find_packages(exclude=['tests']),

    install_requires=['numpy', 'pandas'],

)
