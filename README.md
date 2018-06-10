# Bip xTech: Hands-on Challenge




## Credits
##### Team Aspromonte
* Claudia Chianella ([@clauchian](https://github.com/clauchian))
* Yannick Giovanakis ([@yangvnks](https://github.com/yangvnks))
* Flavio Primo ([@flaprimo](https://github.com/flaprimo/))
* Francesco Zinnari ([@FrancescoZinnari](https://github.com/FrancescoZinnari))

## Method
Below are provided the steps that were followed for this project. Each step and classifiers have their own document.

1. **Load Dataframes**: load the csv data into Pandas Dataframes and save it for quick use later
1. **Data visualization**: data analysis to understand missing values, data relations and usefulness of features
2. **Preprocessing**: with the knowledge acquired with the preceding step, apply preprocessing of data including dealing with missing values and build new features
3. **Ensemble**: build the model to predict NumberOfSales on test set

## Folder structures
* `\` contains all of the jupyter's notebooks including models, preprocessing and data visualization
* `\Data\input` contains the original dataset provided by Bip.
* `\Data\output` to save the outputs given by intermediate steps (load-dataframes, preprocessing) as well as the final prediction given by the model for the test set (submission.csv

## Instructions

### Installation instructions
1. Install Python and clone this repository
2. Install required Python modules with `pip install -r requirements.txt`

to run the [jupyter](http://jupyter.org/)'s notebooks just go with `jupyter notebook`

### Run instructions
To run the notebooks follow these steps:
1. Execute load-dataframes notebook
2. Execute data-visualization notebook
3. Execute preprocessing notebook
4. Execute Ensemble notebook


## Warning
Intermediate results obtained by the various notebooks were not saved in the current repository. If you want to try the code you have to execute it from the beginning!