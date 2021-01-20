# Week 1

## Installing Python

### Windows 10

1. Download and Install Anaconda

   - Go [Here](https://docs.anaconda.com/anaconda/install/windows/) and follow the steps

   _IMPORTANT NOTE_

   - Select the right version

   - Be sure to SELECT "Add Anaconda to the PATH environment variable"

     ![anaconda add path](images/anaconda-add-path.jpeg)

   - don't need to install PyCharm

   - Install Anaconda to a directory path that does not contain spaces or unicode characters.

     ![anaconda add path](images/anaconda-no-space.jpeg)

   - Verify: Open Anaconda Navigator

   - Close Anaconda navigator

2. Open Comman prompt and type:

   ```bash
   python
   ```

   Should look like this:

   ![python cli](images/python-cli.png)

3. To install additional dependencies, simple do

   ```
   conda install [name of package]
   ```

4. For user guide and list of pre installed packages, visit [here](https://docs.anaconda.com/_downloads/9ee215ff15fde24bf01791d719084950/Anaconda-Starter-Guide.pdf).

## For Mac

1. Python is usually pre-installed on mac. To check (note tha capitalised V):

   ```bash
   python -V
   ```

   if you get something like this:

   ```
   Python 3.7.7
   ```

   then congratulations! You already have python installed

2. Otherwise,

3. Verify you have Pip, which is a dependency manager.

   ```bash
   pip -V
   ```

   You should get something like this:

   ```bash
   pip 20.1.1 from /opt/anaconda3/lib/python3.7/site-packages/pip (python 3.7)
   ```

<br/>

## Installing an IDE
