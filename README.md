<img src="https://github.com/sinanozaydin/MATE/blob/master/mate_src/mate_full.png">
<a href="https://zenodo.org/badge/latestdoi/255912421"><img src="https://zenodo.org/badge/255912421.svg" alt="DOI"></a>

MATE is an easy-to-use piece of software written in python3 for making interpretations of magnetotelluric models of the mantle. The software does this by combining the information of many high-pressure and temperature experimental studies (e.g., conductivity, hydrogen diffusion, hydration of minerals) for given compositional and thermal profile.

The program is developed in such a way that adding new experimental models to it is a fairly easy process and can be done through adding entries in external csv files and python scripts. 

Who would be interested in using this program?
- Magnetotelluricists who wants to make interpretations on their models.
- Petrologists who conduct high-pressure and temperature conductivity and/or hydrogen diffusion studies to make comparisons with real data and other studies.

We also suggest that the users should keep using an up-to-date version of the software to exploit the newer models included and benefit from the functionality updates made on the software.

How to cite
========== 
- Özaydın, S., & Selway, K. (2020). MATE: An analysis tool for the interpretation of magnetotelluric models of the mantle. Geochemistry, Geophysics, Geosystems, 21, e2020GC009126. https://doi.org/10.1029/2020GC009126 

Webinar content
==========

There is now a presentation (EMinar Series) on how to use MATE, which can be watched on YouTube via the following link.

https://www.youtube.com/watch?v=UirVvO7k0Ls

Installation
==========

Copying the files to a directory will do the job. However, the structure of the source folder should not be changed. Exporting the source folder is recommended.

The program could simply run by the command:

```bash
python3 MATE
```

**Required Libraries**

Software requires very few libraries including: numpy, scipy, matplotlib, pyQt5

These can be installed easily via **pip3** using the terminal on a Linux distribution or macOS:

```bash
sudo pip3 install numpy scipy matplotlib pyQt5
```
On Windows, pip3 comes automatically with the python3 distribution package. Using command prompt:

```bash
pip3 install numpy scipy matplotlib pyQt5
```

If the user uses Anaconda package management system, required libraries can be installed with:

```bash
conda install numpy scipy matplotlib pyQt5

```

**Running MATE_BATCH**

With the MATE_BATCH, the user have two options currently.


```bash
MATE_BATCH -modem

```

This command takes the input ModEM format model and data files alongside a thermal model entered in XYZ format to make water content maps.
In order to carry this out, the user has to take an output of the parameter file from GUI MATE>Solver>Export batch process parameter selection file.
This command will output the selections made in the MATE by the user and outputs them as a parameter file.

```bash
MATE_BATCH -forward

```

This command is to make batch-process forward calculations with MATE without dealing with GUI for certain compositions and temperatures. The user needs to enter the parameter file output from the GUI MATE like the "-modem" method and calculation file. An example of the calculation file can be found in the "example_calculation_file" directory.


**Creating Exe file**

One could also create an exe file if they want to. This requires the installation of the python module pyinstaller first. This could be done by typing the following command in terminal or command prompt:

```bash
pip3 install pyinstaller
```

Then through command prompt (in Windows) or terminal (linux or macOS), typing the following command in the source directory will create the executable file:


```bash
python3 setupexe.py
```
or (sometimes python can be the default python3, especially on Windows)

```bash
python setupexe.py
```

 
 Executable file has to be run within the directory. It will not work if it is copied elsewhere.
 
Citable content
==========
The bibliographies of studies used in this software is collected in .bib files located at "mate_src/citations" folder. The names of the references are selected as how they appear on the software.

Adding new models to the program
==========

Please submit experimental models that can be added in the master branch of the program. I would also encourage users to inform me about additional features that could be added to the software.


Contact
==========
**Sinan Özaydın**

sinan.ozaydin@protonmail.com
sinan.ozaydin@sydney.edu.au
