from .test_pip.version import version

from distutils.core import setup

setup(
    name='test_pip',
    version=version,
    description='description',
    long_description='long description',
    url='https://github.com/Ryszard-Ps/test-pip.git',
    author='Ryszard-Ps',
    author_email='hello@rjbits.com',
    license='MIT',
    package_dir={'': 'test_pip'},
    packages=['test_pip']
)
