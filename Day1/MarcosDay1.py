import polars as pl
import pandas as pd


dfpandas = pd.read_csv('marcosh_2024_input_day1.txt', sep='   ', header=None)
dfpandas.columns = ['A', 'B']

df = pl.from_dataframe(dfpandas)


def part1(df: pl.DataFrame):
    out = (
        df.with_columns(A=pl.col('A').sort(), B=pl.col('B').sort())
        .with_columns(diff=(pl.col('A') - pl.col('B')).abs())
        .select(pl.col('diff').sum())
    )
    return out


def part2(df):
    counts = df.select(counts=pl.col('B').value_counts()).unnest('counts')
    df = df.join(counts, left_on=['A'], right_on=['B'])
    return df.with_columns(score=pl.col('count') * pl.col('A')).select(pl.col('score').sum())


part1(df)
part2(df)
