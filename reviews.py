import pandas as pd

df = pd.read_csv(r"C:\Users\dnoe1\OneDrive\Documents\Projects\Wine\wine-reviews-exercise-DerekNoe\data\winemag-data-130k-v2.csv.zip", compression="zip")

grouped_df = df.groupby('country').agg(count=('points', 'count'), average_points=('points', 'mean'))
grouped_df.reset_index(inplace=True)
final_df = grouped_df.set_index("country").sort_values(by="count", ascending=False)

final_df.to_csv("reviews-per-country.csv", sep=",", encoding="utf-8")

