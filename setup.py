from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path):
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements if HYPEN_E_DOT not in requirements]
    
    return requirements

setup(
name='mlproject',
version='0.1',
author='Dev',
author_email='devgrt8@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)