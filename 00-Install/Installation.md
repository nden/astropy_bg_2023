# Astropy Workshop Installation and Setup

These instructions describe setup using `Miniconda` and `git` for downloading the workshop materials. It is
not strictly necessary to use either of these, though these are the recommended and most flexible way. It is 
possible to download the materials using a zip file (see below) and any Python installation should be usable
with the workshop materials as long as the packages necessary to run the notebooks are installed. The minimum 
list of packages is : 

- Python (supported versions are 3.9, 3.10 and 3.11)
- numpy
- jupyter
- astropy >=5.3
- ccdproc
- pandas

The detailed instructions are below.

## 0. (Only for Windows) Install WSL

*If you are using Linux skip this step.*

> *If you are using Windows, we now recommend using the Windows Subsystem for Linux (WSL) instead of using native
Windows tools. WSL is now fully supported by Microsoft and tends to result in fewer install headaches, and lets you use
tools that were developed for Linux seamlessly in windows. While you still may be able to use the Windows-native
installation of Miniconda, these instructions focus on the WSL approach for the above reasons.*

To install WSL, you should follow the instructions provided by Microsoft:

https://docs.microsoft.com/en-us/windows/wsl/install

While you may choose an alternative Linux distribution from the default Ubuntu, the instructions below have been tested
on Ubuntu, so unless you have a specific reason, we suggest you stick with the default. Once you reach the point in the
instructions with a working Linux terminal prompt, you can proceed to step 1 of these instructions.

> **Optional** While you can run a WSL terminal with the command prompt built into Windows, it's rather bare-bones and
> you
> may not have the best experience. For WSL on Windows you'll probably want
> to [install Windows Terminal](https://docs.microsoft.com/en-us/windows/terminal/install) to have a terminal experience
> closer to what you'd see on Mac or Linux.

## 1. Install Miniconda (if needed)

> *Miniconda is a free minimal installer for `conda`. It is a small, bootstrap version of Anaconda that includes
only `conda`, Python, the packages they depend on, and a small number of other useful packages like `pip`, `zlib` etc.
If you have already installed Miniconda or Anaconda, you can skip to the next step.*

In a terminal window, check if Miniconda is already installed:

```shell
conda info
```

If Miniconda is not already installed, follow these instructions for your operating system:

https://conda.io/projects/conda/en/latest/user-guide/install/index.html

> Please be sure to install a **64-bit version** of Miniconda to ensure that all packages work correctly.

## 2. Open the conda command prompt

> *Miniconda includes an environment manager called `conda`. An environment manager allows you to have multiple
installations of Python, including packages and versions, installed on your computer. You can create, export, list,
remove, and update environments that have different versions of Python and / or packages installed in them. For this
workshop, we will configure an environment using the `conda` command line utility.*

Open a terminal window and verify that conda is working:

```shell
conda info
```

If you are having trouble, check your shell in a terminal window:

```shell
echo $SHELL
```

then run the initialization, if needed, in that same terminal window:

```shell
conda init $SHELL
```

## 3. Download the workshop materials

### Using Git

#### Install Git (optional, recommended)

At the prompt, check whether Git is already installed:

```shell
git --version
```

If the output shows a Git version, skip to the next step. Otherwise, install Git:

```shell
conda install git
```

#### Clone this repository

If using `git`, clone the workshop repository using
[git](https://help.github.com/articles/set-up-git/):

```shell
git clone https://github.com/nden/astropy_bg_2023.git
```

### Download and extract a ZIP file, from GitHub

If you elect not to use `git`, you can download the ZIP file by opening the green `Code` button at
 https://github.com/nden/astropy_bg_2023.git and selecting `Download ZIP`.

Unzip the file in a location of your preference.

## 4. Create a `conda` environment for the workshop

> *Miniconda includes an environment manager called conda. Environments allow you to have multiple sets of Python
packages installed at the same time, making reproducibility and upgrades easier. You can create, export, list, remove,
and update environments that have different versions of Python and/or packages installed in them.*

[Create a conda environment for this workshop using a yml file](https://conda.io/docs/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file)
. The python version and all needed packages are listed in
[`environment.yml`](https://github.com/nden/astropy_bg_2023/blob/main/00-Install/environment.yml).

Open a terminal window using the appropriate one for your operating system.

Now navigate to this directory in the terminal:

```shell
cd astropy_bg_2023
```

If you downloaded the zip file instead the directory name will include the name of the branch on Github.

```shell
cd astropy_bg_2023-main
```

And finally, on any platform, to install and activate the `astropy-workshop-env` environment, type:

```shell
conda env create --file 00_Install/environment.yml
conda activate astropy-workshop-env
```

The name of the new conda environment created above should now be displayed next to the terminal
prompt: `(astropy-workshop-env)`

## 7. Check Installation

In the terminal you used in the preceding step, run the `verify_install.py` script to check the Python environment and
some required dependencies:

```shell
python 00_Install/verify_install.py
```

If the script reports that some versions do not match for a specific package (for example `numpy`), check first whether
the package was installed using `conda` or `pip` by using `conda list <package>`:

```shell
conda list numpy
```
