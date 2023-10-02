from setuptools import setup

setup(
    name='PyPushBullet',
    version='0.2.1',
    description='A simple library to push notification using PushBullet. You need a pushbullet API key for this',
    long_description=open('README.md').read(),
    author='Balla Vamsi Srinivas',
    author_email='ballavamsisrinivas@gmail.com',
    url='https://github.com/ballavamsi/PyPushBullet',
    packages=['PyPushBullet'],
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
