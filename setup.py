from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str) ->List[str]:
    """ 
    function wil returm list of reaquirments
    """
    requirments=[]
    with open(file_path) as file:
        requirments=file.readline()
        requirments=[req.replace("\n","") for req in requirments]

        if HYPEN_E_DOT in requirments:
            requirments.remove(HYPEN_E_DOT)
    return requirments

setup(
    name='mlproect',
    version='0.0.1',
    author='vikas',
    author_email='alml9.vikas@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)