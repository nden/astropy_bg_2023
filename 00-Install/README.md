# Astropy Workshop Installation and Setup

Install Miniconda by following the instructions for your platform here

https://docs.conda.io/projects/miniconda/en/latest/

This involves 3 steps:

1. Download the Miniconda installer for your platform
2. Running the installer
3. Check installation with `conda --version`

## Conda as an environment manager

We will use

    conda create -n <environment_name> <software_package(s)>
    conda activate <environment_name>
    conda deactivate <environment_name>

We will _not_ use

    conda install <package>

for python software.

