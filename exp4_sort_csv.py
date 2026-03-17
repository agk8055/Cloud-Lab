import pandas as pd
try:
    df = pd.read_csv("sort.csv")
    print("--- Data Before Sorting ---")
    print(df)

    # data_list = df.values.tolist()
    # n = len(data_list)
    # for i in range(n):
    #     for j in range(0, n - i - 1):
    #         if data_list[j][2] > data_list[j+1][2]:
    #             data_list[j], data_list[j+1] = data_list[j+1], data_list[j]
    # sorted_df = pd.DataFrame(data_list, columns=df.columns)
    
    sorted_df = df.sort_values(by="Score")
    print("\n--- Data After Sorting (by Score) ---")
    print(sorted_df)
except FileNotFoundError:
    print("Error: 'sort.csv' not found. Make sure both files are in the same folder.")