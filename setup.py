from setuptools import setup, find_packages


setup(name='vaporwavely',
    version='1.0.1',
    url='https://github.com/Owanesh/vaporwavely',
    license='MIT',
    author='Owanesh',
    description='An extremely fast library to vaporize your text and many more!',
    long_description=open('README.rst').read(),
    install_requires=[],
	packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
    ])
