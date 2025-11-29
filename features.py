import pandas as pd

def build_features(df):
    df_fe = df[[
        "Avg. Area Income",
        "Avg. Area House Age",
        "Avg. Area Number of Rooms",
        "Avg. Area Number of Bedrooms",
        "Area Population"
    ]].copy()

    df_fe["Income2"] = df_fe["Avg. Area Income"]**2
    df_fe["Rooms2"]  = df_fe["Avg. Area Number of Rooms"]**2
    df_fe["Pop2"]    = df_fe["Area Population"]**2

    df_fe["BedRoom_Ratio"] = (
        df_fe["Avg. Area Number of Bedrooms"] /
        df_fe["Avg. Area Number of Rooms"]
    )

    df_fe["Income_Rooms"] = df_fe["Avg. Area Income"] * df_fe["Avg. Area Number of Rooms"]
    df_fe["Income_Pop"]   = df_fe["Avg. Area Income"] * df_fe["Area Population"]
    df_fe["Rooms_Age"]    = df_fe["Avg. Area Number of Rooms"] * df_fe["Avg. Area House Age"]
    df_fe["Age_Income"]   = df_fe["Avg. Area House Age"] * df_fe["Avg. Area Income"]

    return df_fe
