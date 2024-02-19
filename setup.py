from setuptools import find_packages, setup
from typing import List


HANDLE_E = "-e ."

def get_requirement(file_path)->List[str]:

    requirements= []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        
    if HANDLE_E in requirements:
        requirements.remove(HANDLE_E)

    return requirements


setup(

    name="Student Performance Prediction",
    version="1.0.0",
    description="...",
    author="Devang Shah",
    author_email="heydevang@gmail.com",
    packages=find_packages(),
    install_requires=get_requirement("requirements.txt")

)