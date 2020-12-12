import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns


### lineplot
# Set the width and height of the figure
plt.figure(figsize=(16,6))

# plotting each columns against the row (timeline)
sns.lineplot(data=data)


### barplot and heatmap
plt.figure(figsize=(10,6))

# Add title
plt.title("Title")

sns.barplot(x=data.index, y=data['y'])
#sns.heatmap(data=flight_data, annot=True)

# Add label for vertical axis
plt.ylabel("Y Axis")


### scatterplot
sns.scatterplot(x=data['x'], y=data['y'])
# add a regression line
sns.regplot(x=data['x'], y=data['y'])
# add colorcode
hue=data['property'])
# add regressionline for every group with a certain property
sns.lmplot(x="x", y="y", hue="property", data=data)


### histplot
sns.distplot(a=data['x'], kde=False)
# density plot
sns.kdeplot(data=data['x'], shade=True)
# 2D KDE plot
sns.jointplot(x=data['x'], y=data['y'], kind="kde")
# several KDE plots
sns.kdeplot(data=data['x'], label="y", shade=True)
sns.kdeplot(data=data2['x'], label="y", shade=True)
sns.kdeplot(data=data3['x'], label="y", shade=True)



