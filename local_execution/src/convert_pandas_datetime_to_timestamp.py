from pandas import DataFrame, Timestamp

def convert_pandas_datetime_to_timestamp(df:DataFrame) -> DataFrame:
    df_converted = df
    for column in df_converted.select_dtypes(include='datetime64'):
        df_converted[column] = df_converted[column].apply(lambda x: Timestamp(x)).astype(int)
    return df_converted