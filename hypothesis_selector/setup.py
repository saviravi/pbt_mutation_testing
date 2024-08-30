from setuptools import setup, find_packages
setup(
    name="pytest-pbt-finder",
    include_package_data=True,
    python_requires=">=3.10",
    install_requires=[
        "pytest>=7.4.4",
    ],
    setup_requires=["pytest-runner"],
    classifiers=[
        "Framework :: Pytest",
    ],
    packages=find_packages(include=["pytest_find_pbt", "pytest_find_pbt.*"]),
    test_suite="tests",
    entry_points={"pytest11": ["myplugin = pytest_find_pbt.plugin"]},
    version="0.1.0",
)
