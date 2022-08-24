from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "DVC_Tensorflow_AIOPS"
AUTHOR_USER_NAME = "mihr3030"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = [
    "dvc==2.7.2",
    "tqdm==4.62.3",
    "tensorflow==2.5.0",
    "joblib==1.1.0"
]


setup(
    name=SRC_REPO,
    version="0.0.3",
    author="mihir3030",
    description="A small package for DVC",
    long_description="DVC_Tensorflow_AIOPS with Docker",
    long_description_content_type="text/markdown",
    url=f"https://github.com/mihir3030/DVC_Tensorflow_AIOPS",
    author_email="mihirdholakia777@gmail.com",
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.6",
    install_requires=LIST_OF_REQUIREMENTS
)