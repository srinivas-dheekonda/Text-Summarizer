import setuptools

with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()

__version__ ="0.0.0"
REPO_NAME = "Text_summarization"
AUTHOR_USERNAME ="srirao"
SRC_REPO = "textsummarizer"
AUTHOR_EMAIL = "vasuvasu.srinu1996@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USERNAME,
    author_email=AUTHOR_EMAIL,
    description="a samll python pakceges for NLP project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/srirao/Text_summarization",
    project_urls={
        "Bug tracker": "https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}/issues",

    })