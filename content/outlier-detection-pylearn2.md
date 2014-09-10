Title: Detecting anomalies with Neural newtorks
Date: 2014-09-07 10:20
Category: Data-mining

In this article I will show part of the work I've done during my Master's internship in Amsterdam. The focus of this work was finding outliers in the gas consumption of some buildings. 

Energy consumption in buildings is one of the fastest growing sectors. Approximately __41% of the total energy in Europe is consumed by buildings (households and services)__. It is showed that __commercial buildings consume from 15% to 30% more energy than necessary__ due to poorly maintained, degraded, and improperly controlled equipment. These anomalies can become easy fixable problems with a reliable fault detection and diagnosis (FDD) system. 


An outlier, by definition, is an observation which deviates significantly from other observations so that it creates suspicion that it was created by different dynamics. Despite this general definition, the more appropriate way of defining
outliers is highly application-dependent, because even same scenarios may require different determinations of outliers.

In this paper, outliers are very closed related to the problem of time-series forecasting, since outliers are declared on the basis of deviations from expected (or forecast) value.

![outliers](/images/outliers.png)

The system is composed by 2-phase process where in the first one the short-term (hourly) gas consumption is
forecast thanks to a historical time-series, and in the second phase outliers are detected on the basis of deviations from expected (or forecast) value.

## iPython Notebooks

In these notebooks the dataset is analysed, then it is used by an Artificial Neural Network built in [pylearn2](https://github.com/lisa-lab/pylearn2). This project uses Python with [pandas](http://pandas.pydata.org/).

* [Dataset preparation](http://nbviewer.ipython.org/github/denadai2/energyUva/blob/master/notebooks/0-Data%2BWeather%2BHolidays.ipynb)
* [Dataset cleaning](http://nbviewer.ipython.org/github/denadai2/energyUva/blob/master/notebooks/1-Dataset_cleaning.ipynb)
* [Dataset analysis](http://nbviewer.ipython.org/github/denadai2/energyUva/blob/master/notebooks/2-Dataset%20analysis.ipynb)
* [Feature engineering](http://nbviewer.ipython.org/github/denadai2/energyUva/blob/master/notebooks/3-Feature%20engineering.ipynb). [Short version](http://nbviewer.ipython.org/github/denadai2/energyUva/blob/master/notebooks/3bis-%20Regression%20short%20version.ipynb)
* [pylearn2 YAML file](https://github.com/denadai2/energyUva/blob/master/NN_static_MLSE.yaml)


## Results

This model was able to detect some synthetic and real outliers from the dataset.  Since the predictor is very accurate (with RMSE from 8 m^3 in building 740-NTH, to RMSE 2.5 m^3 in building 761-KMH), the outlier mechanism is able to easily detect strange behaviours defining a threshold value in the confidence interval without the need to possess previous examples of outliers. The scope of this paper was forecasting the highly irregular gas consumption time-series, but it is believed that similar results could be also obtained with electric consumption time-series. It is hoped that this could lead to new analysis of the energy consumption in public buildings.

The draft of the __paper__ can be found [here](https://github.com/denadai2/energyUva/blob/master/paperEnergy/paperv2_2.pdf), while the sources are in this [github project](https://github.com/denadai2/energyUva).

__The paper is still a draft, so I would really like to listen your opinion, notes, doubts. Please, drop a note here!__







