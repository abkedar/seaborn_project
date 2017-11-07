# Create a Jointplot to see the Pearson correlation between numeric features

* So, we know from the previous lecture how to find out the pearson correlaton value and plot it using matplotlib.
* Seaborn gives a very flexible method to both in a single line of code.

## Write a Function `joinplot()` :

* Will take following parameters and return a plot with pearson correlation coeffient and p-value with two plots one with scatter and other with contour plot.
* Plot will be looking some what similar to link given below.


### Parameter:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| df| dataframe | compulsory |  | dataframe containing the above variables |
| col1| str | compulsory |  | Its a categorical feature name |
| col2| str | compulsory |  | Its a continous feature name |
| quantile| float | Optional | 0.95 | quantile value to remove outlier |
| kind| str | Optional | hex | kind of plot to display(eg. hex, scatter, hist...) |
| n_levels | int | Optional | 10 | plotting the contour plot |

### Return:

None
