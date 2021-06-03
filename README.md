# rice-crop-fba-model
# Tested on Python 2.7.17 / IPython 5.10.0
Codes to simulate growth under normal and stress conditions 

1. Install cobra version = 0.4.1, pandas version = 0.13.1 or 0.17.1, xlrd version = 0.9.0
2. Cobrapy is provided with this repository (version 0.4.1) that might require manual setup. It is recommended to install through proper channel (see https://pypi.org/project/cobra/).
3. Install other packages like scipy, matplotlib, libsbml, lxml etc. (see scobra documentation)
4. Use the existing Scobra with this code (unzip, no installation required)



Example to obtain FBA solutions and growth curves:

#to run

In [1]: import rice_growth_model_with_WOFOST

In [2]: normal_growth = rice_growth_model_with_WOFOST.Growth() #use WOFOST_rates_one_plant.csv

In [3]: water_limited_growth = rice_growth_model_with_WOFOST.Growth() # use WOFOST_rates_one_plant_stress.csv (reload)


#to load

In [1]: import pickle
In [2]: f = open('normal.pkl','rb')
In [3]: normal_growth  = pickle.load(f)
In [4]: f.close()


In [5]: f = open('stress.pkl','rb')
In [6]: water_limited_growth  = pickle.load(f)
In [7]: f.close()
