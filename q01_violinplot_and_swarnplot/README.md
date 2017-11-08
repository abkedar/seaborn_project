# Create a Violinplot and Swarnplot to see the distribution

* With this assignment we will come to know the distribution between the categorical and numerical data with respect to second categorical feature.
* Here we will be considering `Property_Area`, `LoanAmount` and `Gender` to understand how LoanAmount is distributed with Gender within Property_Area.

## Write a function `plot()` :

* Which takes the below parameter and return a Violinplot and Swarnplot.
* Plot will be looking some what similar to link given below.

### Parameters:


| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| df| dataframe | compulsory |  | dataframe containing the above variables |
| col1| str | compulsory |  | Its a categorical feature name |
| col2| str | compulsory |  | Its a continous feature name |
| col3| str | compulsory |  | Its a categorical feature name |

### Returns:

None


**Please Compare your plot with the violin_plot_q01.png in the images directory** - https://github.com/commit-live-students/seaborn_project/blob/master/images/violin_plot_q01.png
