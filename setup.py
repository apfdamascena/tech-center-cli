from setuptools import setup, find_packages


def read_requirements():
    with open('requirements.txt') as requirements_file:
        content = requirements_file.read()
        requirements = content.split('\n')
    return requirements


setup(
    name='tech-center-cli',
    version = '0.1',
    packages=find_packages(),
    include_package_data = True,
    install_requires = read_requirements(),
    entry_points = ''' 
        [console_scripts]
        tc = techcenter.cli:cli
    '''
)