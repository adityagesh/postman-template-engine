from setuptools import find_packages, setup
setup(
    name='postmanrenderer',
    packages=find_packages(include=['postmanrenderer']),
    version='0.1.0',
    description='Create and Export Postman collections',
    author='Aditya Nagesh',
    license='MIT',
    install_requires=['Jinja2'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
