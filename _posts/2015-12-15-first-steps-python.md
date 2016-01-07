---
layout: post
title: First Steps in Python for Data Science
synopsis: Thankfully, it's not difficult to start using Python for data analysis. If you're brand new to Python I want to share a couple of notes to get you up and running.
---

Thankfully, it's not difficult to start using Python for data science. If you're brand new to Python (and/or the concept of using a scripting language for analyzing data) I want to share a couple of notes to get you up and running.

## 1) The Anaconda Distribution

Anaconda is a Python distribution, which means that it is not just Python, but also [several packages](http://docs.continuum.io/anaconda/pkg-docs) and tools frequently used in association with data analysis such as package management tools, alternative python interpreters, and text editors. There are other distributions out there, but Anaconda seems to be the most popular distribution and it is the one I recommend. You can download the Anaconda distribution [here](https://www.continuum.io/downloads). Personally, Anaconda was my first distribution to download, both for personal and professional use, and I haven't found the need to use a different distribution.

## 2) Spyder and IPython Notebook

[Spyder](https://en.wikipedia.org/wiki/Spyder_(software)) is an Integrated Development Environment (IDE) built for data science. At a basic level, it gives you the ability to develop, save, and execute your code from within the same interface. The [IPython notebook](http://ipython.org/notebook.html) is an "interactive computational environment, in which you can combine code execution, rich text, mathematics, plots...". These are not the only code editors (you could use Atom, Brackets, or Sublime, for instance), but these require the least up-front effort to get started. To use either of these options, simply type ```IPython notebook``` or ```Spyder``` from your terminal / command line and the application will launch. Note that when you type IPython notebook from the terminal / command line this will not only launch the notebook, but it will also start the IPython notebook server which will run in the background. Personally, I typically like using the IPython notebook for developing and presenting code.

## 3) Base Python Data Structures

Before getting into the python's rich package ecosystem, there are a couple of base python data structures you should be aware of right off the bat: the tuple, the dictionary, and the list. Here's how they are defined:

* The **list** is a mutable, iterable data structure. This is a simple list: ```['drinks', 'food', 'desert']```. You can learn about lists from [Section 3.1.4.](https://docs.python.org/2/tutorial/introduction.html#lists) [](https://docs.python.org/2/tutorial/introduction.html#lists) and [Section 5.1.](https://docs.python.org/2/tutorial/datastructures.html#more-on-lists) of the Python Software Foundation tutorial.
* The **tuple** is an immutable, iterable data structure. This is a simple tuple: ```('drinks', 'food', 'desert')```. You can learn about tuples from [Section 5.3.](https://docs.python.org/2/tutorial/datastructures.html#tuples-and-sequences) [](https://docs.python.org/2/tutorial/introduction.html#lists)of the Python Software Foundation tutorial.
* The **dictionary** is "an unordered set of key: value pairs, with the requirement that the keys are unique (within one dictionary)." This is a simple dictionary: ```{'drinks': 'coffee', 'food': 'sandwhich', 'desert': 'pecan pie'}```. You can learn about dictionaries from [Section 5.5.](https://docs.python.org/2/tutorial/datastructures.html#dictionaries) [](https://docs.python.org/2/tutorial/introduction.html#lists)of the Python Software Foundation tutorial.

Each of these data structures are important in it's own way, however, for now it is good enough to know that these data structure exist in base python. Any additional knowledge is a plus. On a personal note, when I use base Python data structures it is often in the context of packages that provide much richer functionality... such as NumPy and Pandas.

## 4) NumPy and Pandas

Python does not automatically vectorize operations within its core data structures. This means, for instance, that if you try to add 1 to a python list of numbers, it won't go through each list element and add 1 to it. Depending on your background, this may or may not come as a shock to you. If you're coming from a engineering background and have used [MATLAB](http://www.mathworks.com/products/matlab/), or if you're coming from a Statistics / Econometrics backround and have used [R](https://en.wikipedia.org/wiki/R_(programming_language)) or [SAS](https://www.sas.com/en_us/home.html) you'll be accustomed to languages that "think" in terms of tabular data structures. To get the equivalent behavior in Python, you're going to want to use NumPy (pronounced "Numb-Pie", not "Num-Pee") and Pandas.

NumPy's base data structure is a homogeneously typed n-dimensional array (i.e., you can't have strings and integers in the same array, for instance). NumPy arrays do not have labels or the rows or columns. If you have a engineering background and are familiar with MATLAB, you might find it easiest to start with NumPy. Here is an example of a simple NumPy array:

``` python
# NumPy Array
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])
```

To learn more about NumPy arrays check out this [comparison](https://docs.scipy.org/doc/numpy-dev/user/numpy-for-matlab-users.html) between MATLAB and NumPy or this  [tutorial](https://docs.scipy.org/doc/numpy-dev/user/quickstart.html) to get started.

Pandas stands for Panel Data Analysis Structures. As the name implies, the base data structure in Pandas is a two dimensional table. This table contains a number of properties that NumPy arrays do not contain, namely, row and column labels (called indexes), and the ability to store different data types in each column (within a column, all data must have the same data type, however). In pandas, these tables are called Dataframes. Here is an example of a pandas dataframe:

``` python
# Pandas DataFrame
   A          B  C  D      E    F
0  1 2013-01-02  1  3   test  foo
1  1 2013-01-02  1  3  train  foo
2  1 2013-01-02  1  3   test  foo
3  1 2013-01-02  1  3  train  foo
```

If you have a statistics background and are familiar with R or SAS, you might find it easiest to start with Pandas. If you have a business analyst background and are familiar with excel and SQL, you might find it easiest to start with Pandas as well. The Pandas website has [tutorials](http://pandas.pydata.org/pandas-docs/stable/tutorials.html) as well.

## 5) Packages

A python package is a collection of functionality that you may find useful. In order to use Pandas or NumPy or any other package, you must first have it installed (If you downloaded the anaconda distribution you already have Pandas and NumPy installed), and then you must also import it into your working session.  Importing a python package gives you access to all of the functionality defined in that package. There are two package management systems that I use: **conda**, and **pip**. In order to check which packages you have installed on your computer you either type ```conda list``` or ```pip freeze``` into your terminal/command line. If you find you need to update to the latest version of a package, for instance pandas, you can simply type ```conda update pandas``` or ```pip install pandas --upgrade```. If you have the Anaconda distribution installed, either of these commands should work. Once you have a package installed, you will need to import it into your working session before you can use the functions that the package defines. ```import pandas as pd``` imports the full functionality of pandas and assigns the ```pd``` alias which is a common convention used for this package. For additional information about packages you may find this [conda reference guide](http://conda.pydata.org/docs/_downloads/conda-cheatsheet.pdf) or [pip reference guide](http://pip.readthedocs.org/en/stable/reference/) to be helpful.

## Going from here

We've only scratched the surface of what it means to use Python for Data Science. We haven't discussed *how* to use Pandas or NumPy for data analysis, and we haven't discussed other aspects of Data Science such as Data Visualization, Machine Learning or Statistical Inference. However, time spent learning Pandas and NumPy is time well spent, since these packages are  foundational to using the more advanced topics in Data Science.

Was this information useful? What did I miss? Let me know what you think on [twitter](https://twitter.com/josiahjdavis) or send me an [e-mail](mailto:josiah.j.davis@gmail.com).
