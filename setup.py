from setuptools import setup

setup(
    name='Flask-Validator',
    version='1.0',
    url='',
    license='BSD',
    author='Ogunbiyi Ibrahim',
    author_email='adwumiogunbiyi@gmail.com',
    description='A Flask request data validator library',
    long_description=__doc__,
    #py_modules=['flask_validator'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    packages=['flask_validator'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)