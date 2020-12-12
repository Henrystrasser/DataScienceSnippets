import pandas as pd

### basic pd
pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'],
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])
pd.Series([1, 2, 3, 4, 5])
pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
wine_reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv")

### iloc and loc
# iloc ignores index names
reviews.iloc[0]
reviews.iloc[:, 0]
# loc works with index names
reviews.loc[0, 'country']

### sets a column as the index/ID to identify unique rows
reviews.set_index("title")

### searching through the dataset
reviews.country == 'Italy'
reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]
reviews.loc[reviews.country.isin(['Italy', 'France'])]
reviews.loc[reviews.price.notnull()]

### assigning data
reviews['critic'] = 'everyone'

### describe dataset and count values
reviews.points.describe()
reviews.taster_name.describe()
reviews.points.mean()
reviews.taster_name.unique()
reviews.taster_name.value_counts()

### mapping
reviews.points.map(lambda p: p - review_points_mean)

def remean_points(row):
    row.points = row.points - review_points_mean
    return row

reviews.apply(remean_points, axis='columns')

reviews.country + " - " + reviews.region_1

### grouping data
reviews.groupby('points').points.count()
reviews.groupby('points').price.min()
reviews.groupby('winery').apply(lambda df: df.title.iloc[0])
reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])
# grouping the specified row_value versus the aggregated values
reviews.groupby(['country']).price.agg([len, min, max])

### Sorting
countries_reviewed = countries_reviewed.reset_index()
countries_reviewed.sort_values(by='len', ascending=False)

### Type
reviews.price.dtype
reviews.dtypes
reviews.points.astype('float64')
# NaN
reviews[pd.isnull(reviews.country)]
reviews.region_2.fillna("Unknown")
# replace
reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino")

### rename
reviews.rename(columns={'points': 'score'})

### concat
pd.concat([dataset1, dataset2])
# leftjoin
left.join(right, lsuffix='A', rsuffix='B')





