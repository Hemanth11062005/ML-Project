from setuptools import find_packages, setup

def get_requirements(file_path):
    """
    Read the requirements file and return a list of dependencies.
    """
    with open(file_path) as file:
        requirements = file.read().splitlines()
        # Remove empty lines and comments
        requirements = [req for req in requirements if req and not req.startswith('#')]
    return requirements

setup(
    name='mlproject',
    version='75.1.0',
    author='Hemanth',
    author_email='hemanthsainagchilukuri@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
