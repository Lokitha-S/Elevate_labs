import pandas as pd
from sklearn.datasets import load_iris

def run_analysis():
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    print("Iris Dataset Head")
    print(df.head())
    
    print("\nSummary Statistics")
    print(df.describe())
    df.fillna(df.mean(), inplace=True)
    filtered_df = df[df['sepal length (cm)'] > 5.0].sort_values(by='sepal length (cm)')
    grouped = df.groupby('species').mean()
    print("\n--- Average Measurements by Species ---")
    print(grouped)
    df['sepal_area'] = df['sepal length (cm)'] * df['sepal width (cm)']

    
    df.to_csv('cleaned_iris_data.csv', index=False)
    print("\nSuccess: 'cleaned_iris_data.csv' has been created.")


    print("\n---Result---")
    print(f"The dataset contains {df.shape[0]} samples across 3 species.")
    print("Insight: Species 2 (Virginica) generally has the largest petal dimensions.")

if __name__ == "__main__":
    run_analysis()