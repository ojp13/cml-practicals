from setuptools import setup, find_packages

setup(
    name="01 - MONDAY",
    version="1.0",
    description="Monday",
    packages=find_packages("src", exclude=["test"]),
    install_requires=[
        "pandas",
        "seaborn",
        "ipympl",
        "matplotlib",
        "missingno",
        "cython",
        "joblib",
        "ipykernel",
        "scipy",
        "jupyter",
        "scikit-learn",
        "jupyterlab",
        "ipywidgets",
    ],
)
