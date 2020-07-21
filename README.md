<img src="https://github.com/sinanozaydin/MATE/blob/master/mate_src/mate_full.png">
<a href="https://zenodo.org/badge/latestdoi/255912421"><img src="https://zenodo.org/badge/255912421.svg" alt="DOI"></a>

MATE is an easy-to-use piece of software written in python3 for making interpretations of magnetotelluric models of the mantle. The software does this by combining the information of many high-pressure and temperature experimental studies (e.g., conductivity, hydrogen diffusion, hydration of minerals) for given compositional and thermal profile.

The program is developed in such a way that adding new experimental models to it is a fairly easy process and can be done through adding entries in external csv files and python scripts. 

Who would be interested in using this program?
- Magnetotelluricists who wants to make interpretations on their models.
- Petrologists who conduct high-pressure and temperature conductivity and/or hydrogen diffusion studies to make comparisons with real data and other studies.


Installation
==========

Copying the files to a directory will do the job. However, the structure of the source folder should not be changed. Exporting the source folder is recommended.

The program could simply run by the command:


```bash
python3(or python if python3 is the default) MATE
```

**Required Libraries**

Software requires very few libraries including: numpy, scipy, matplotlib, pyQt5

These can be installed easily via **pip3** using the terminal on a Linux distribution or macOS:

```bash
sudo pip3 install numpy, scipy, matplotlib, pyQt5
```
On Windows, pip3 comes automatically with the python3 distribution package. Using command prompt:

```bash
pip3 install numpy, scipy, matplotlib, pyQt5
```

**Creating Exe file**

One could also create an exe file if they want to. This requires the installation of the python module pyinstaller first. This could be done by typing the following command in terminal or command prompt:

```bash
pip3 install pyinstaller
```

Then through command prompt (in Windows) or terminal (linux or macOS), typing the following command in the source directory will create the executable file:


```bash
python3(or python if the default is python3>) setupexe.py
```
 
 Executable file has to be run within the directory. It will not work if it is copied elsewhere.

Adding new models to the program
==========

Please submit experimental models that can be added in the master branch of the program.

Contact
==========
**Sinan Özaydın**

sinan.ozaydin@hdr.mq.edu.au
