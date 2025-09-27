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
    return (test,)


@app.cell
def _(test):
    test
    return


if __name__ == "__main__":
    app.run()
