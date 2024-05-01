import setuptools

with open("README.md", 'r', encoding="utf-8") as f:
    long_description = f.read()

__verion__ = "0.0.0"

REPO_NAME = "CNN-Classifier-End-to-end"
AUTHOR_USER_NAME = "Pavun-KumarCH"
SRC_REPO = "CNN_CLASSIFIER"
AUTHOR_EMAIL = "pavun9848@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version= __verion__,
    author= AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description= "A Small python package for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url = "https://github.com/Pavun-KumarCH/CNN-Classifier-End-to-end",
    project_urls = {
        "Bug Tracker": "https://github.com/Pavun-KumarCH/CNN-Classifier-End-to-end/issues",   
    },
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src")
)

