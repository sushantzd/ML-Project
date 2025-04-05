from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as file_obj:
        requirements = []
        for line in file_obj:
            req = line.strip()
            if req and not req.startswith("-e"):
                requirements.append(req)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='sushant',
    author_email='sushantchoudhary912@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
