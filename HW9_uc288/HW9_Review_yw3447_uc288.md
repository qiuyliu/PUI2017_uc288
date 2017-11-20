# Review of Yukun Wan's Visualization for PUI HW8
## Criteria
* **CLARITY**: Is the plot easy to read? Is it clear or confusing? Are the quantities being visualized ambiguous?
* **ESTHETIC**: Beautiful is a subjective judgment: you should not judge the plot on the basis of whether you think it is "beautiful", but you should judge whether its esthetic is functional to what it is meant to communicate. Are the colors chosen appropriately? Are the graphical elements used appropriate to represent the quantities being visualized? Are the graphical choices allowing you to focus on the right elements or are they distracting you?
* **HONESTY**: Is the plot honestly reproducing the data or is it deforming it, perhaps to emphasize a point?

## Original Visualization
![Alt text](https://github.com/YukunVVan/PUI2017_yw3447/blob/master/HW8_yw3447/yw3447_plot.png?raw=true)
**Figure 1**: NYC Energy usage (Site EUI (kBtu/ft_2)) for each Zip Codes. Black shows the areas whose average Site EUI is below 77.05(<25% of the whole). Blue shows the areas whose average Site EUI is between 77.05 and 86.25 (25% ~ 50% of the whole). Green shows the areas whose average Site EUI is between 86.25 and 95.80 (50% ~ 75% of the whole). Yellow shows the areas whose average Site EUI is over 95.80 (>75% of the whole). Some areas have no color because the data there are outliers and are removed.

## Review
### Clarity
Overall, the plot is easy to read because the title and proper legends are rendered. The quantity visualized is obviously the Site Energy Use Intensity and she also included the units of measurement. However, I would have to argue that the title is a bit lacking in terms of what the values actually are. After reading through her caption, she mentions that the values are actually the average Site EUI of all buildings within the zip code. It would provide better clarity if the title also mentions that the plot is the Average Site EUI per Zip Code. 

### Esthetic
I would have to say that this map seems a bit distorted because the figure looks a bit squished on the height aspect. The map is obviously showing New York City and the title of the plot also indicates that it is indeed NYC, so I feel like the axis with the longitude and latitude are no longer necessary. The colors are a bit distracting for me just because I would have to understand which color means a higher value and which color means a lower value. Despite the legend and the caption explaining the association of the values with the color, it would be better to have used the same hue with varying saturation and brightness to denote a less efficient zip code.

### Honesty
To understand the plot further and to see how Yukun derived the values to plot the map of NYC, I read the Jupyter notebook and found that she only included buildings with Site EUI greater than 1,000 kBtu/ft2 and she also only included Multifamily Housing buildings. Since the dataset was reduced, this skews the plot because different building types have different distributions and the title is quite misleading wherein it only says 'NYC Site EUI'. Despite using a good split (quantile) to determine the breaks in the data, the quantile break is biased only towards the Multifamily Housing buildings with more than 1,000 kBtu/ft2.

One other issue with aggregating the energy use intensity to the zip code level is that Yukun only got the mean of the buildings within the zip code. Although she is aggregating the buildings categorized under the same building type only, it seems a bit problematic to aggregate energy data to the zip code level because some areas might not have the same number of buildings. It would be good to have a plot with the count of Multifamily Housing buildings per zip code and apply normalization.
