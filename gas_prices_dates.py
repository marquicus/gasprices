import argparse
import pandas as pd


def gas_prices(input):
    """Getting gas prices by day and month

    1. Read csv or excel (assuming extension csv is a true csv file format, it might be another validations in real scenario, in my experience I prefer to perform it at bash script level)
    1.1 Datetime Index is for month
    2. Write to csv
    3. Group and sum by colum Henry...
    4. Format index starting with day it's the cause I use another df
    5. Write to csv
    """

    print("Getting daily prices")
    if input[0].name.lower().endswith('.csv'):
        dfg = pd.read_csv(input[0], skiprows=4)
    else:
        dfg = pd.read_excel(input[0], skiprows=3, sheet_name='Data 1')
    dfg.index = pd.to_datetime(dfg["Day"], format='%m/%d/%Y')
    dfg.to_csv('gas_byday.csv', header=["date", "value"], index=False)

    print("Getting monthly prices")
    dfg_month = dfg['Henry Hub Natural Gas Spot Price Dollars per Million Btu'].resample('M').sum()
    df = pd.DataFrame(dfg_month, index=dfg_month.index.strftime("%d/%m/%Y"))
    df.to_csv('gas_bymonth.csv', header=["value"], index_label="date", index=True)

    print("Done")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gas Prices Exporter",
                                     epilog="Report errors a marquicus@mail.com")
    parser.add_argument('-i', '--input', nargs='+', required=True,
                        type=argparse.FileType('r'),
                        help='Input file, only .csv, xls or xslx extensions allowed')
    kwargs = vars(parser.parse_args())
    gas_prices(**kwargs)


# End of file
# vim: set ts=2 sw=2 noet:
