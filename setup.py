from setuptools import setup

import notrequests


try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst').decode('utf-8')
except ImportError:
    long_description = open('README.md', 'rb').read().decode('utf-8')


setup(
    name='notrequests',
    version=notrequests.__version__,
    description='Like Requests, but using urllib / urllib2.',
    long_description=long_description,
    url = 'https://github.com/davidwtbuxton/notrequests',
    author='David Buxton',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
    py_modules=['notrequests'],
    install_requires=['six'],
)
