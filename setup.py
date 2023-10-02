from setuptools import setup
from pathlib import Path

setup(
    name='PyPushBullet',
    version='0.2.4',
    description='A simple library to push notification using PushBullet. You need a pushbullet API key for this',
    long_description=Path('PYPIREADME.md').read_text(),
    long_description_content_type='text/markdown',
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
