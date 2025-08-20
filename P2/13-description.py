# pip install pandas
import pandas as pd     # Importing pandas for data manipulation

df = pd.read_csv("./data/restaurant_reviews.csv")
print(df)

def generate_description(row):
    description = f"""{row['ID']} 레스토랑은 맛에 대한 평가는 {row['Taste']}점이며, 
        분위기에 대한 평가는 {row['Ambiance']}점이고, 
        서비스에 대한 평가는 {row['Service']}점이고,
        가격 대비 가치는 {'그만한 가치가 있습니다' if row['Worth_the_price'] == 'yes' else '그만한 가치가 없습니다'}, 그리고
        메뉴 다양성에 대한 평가는 {row['Menu_variety']}점이며, 위생 상태에 대한 평가는 {row['Hygienic']}점입니다, 그리고
        비건 옵션은 {'가능합니다' if row['Vegan_options'] == 'yes' else '가능하지 않습니다'}, 그리고
        흡연은 {'가능합니다' if row['Smoking_area'] == 'yes' else '가능하지 않습니다'}, 그리고
        주차는 {'가능합니다' if row['Parking'] == 'yes' else '가능하지 않습니다'}, 그리고
        반려동물 출입은 {'가능합니다' if row['Pet_friendly'] == 'yes' else '가능하지 않습니다'}."""
    return description

# apply the function to each row and create a new column
df["Description"] = df.apply(generate_description, axis=1)

df.to_csv("restaurant_reviews_with_descriptions.csv", index=False)
