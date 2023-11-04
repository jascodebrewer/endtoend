from typing import List
from setuptools import setup, find_packages

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='Jas Kaur',
    author_email='jasofficial1214@gmail.com',
    # install_requires=["scikit-learn","pandas","numpy"],
    # or you can create a function as shown above to install requirements for all the 
    # components
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)