import marimo

__generated_with = "0.16.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import polars as pl

    base_dir = 'hull-tactical-market-prediction'
    tr = base_dir + '/train.csv'
    te = base_dir + '/test.csv'
    return pl, te, tr


@app.cell
def _(pl, te, tr):
    train = pl.read_csv(tr)
    test = pl.read_csv(te)
    return test, train


@app.cell
def _(train):
    train
    return


@app.cell
def _(test):
    test
    return


@app.cell
def _(train):
    for column in train.columns:
        print(column)
    return


@app.cell
def _(train):
    sub = train[['forward_returns', 'risk_free_rate', 'market_forward_excess_returns']][0]
    sub
    return (sub,)


@app.cell
def _(sub):
    sub['forward_returns'] - sub['risk_free_rate'] 
    #== sub['market_forward_excess_returns']
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    date_id - An identifier for a single trading day.

    M* - Market Dynamics/Technical features.

    E* - Macro Economic features.

    I* - Interest Rate features.

    P* - Price/Valuation features.

    V* - Volatility features.

    S* - Sentiment features.

    MOM* - Momentum features.

    D* - Dummy/Binary features.

    forward_returns - The returns from buying the S&P 500 and selling it a day later. Train set only.

    risk_free_rate - The federal funds rate. Train set only.
    market_forward_excess_returns - Forward returns relative to expectations. Computed by subtracting the rolling five-year mean forward returns and winsorizing the result using a median absolute deviation (MAD) with a criterion of 4. Train set only.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    feature 1:

    Feature Idea: Calculate a 5-day moving average and a 20-day moving average for one of the M* (Market) features.
    """
    )
    return


@app.cell
def _(pl):
    cols = [f'M{i}' for i in range(1, 19)]

    for col in cols:
        for window in [5, 10, 20]:
            train = train.with_columns(
                pl.col(col).rolling_mean(window_size=window).alias(f'{col}_rolling_mean_{window}')
            )
    return (train,)


@app.cell
def _(train):
    for c in train.columns:
        print(c)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
