
"""
Flask-Redis-Session
-------------

The users can use this extension to add server-side session to your application.
"""
from setuptools import setup


setup(
    name='Flask-Redis-Session',
    version='0.1',
    url='https://github.com/EricQAQ/Flask-Redis-Session',
    license='MIT',
    author='Eric Zhang',
    author_email='zhangzy93@163.com',
    description='add server-side session, stored by Redis',
    long_description=__doc__,
    py_modules=['flask_redisSession'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask>=0.9'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)