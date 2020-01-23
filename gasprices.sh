#!/bin/bash

#
##
## Title: Challenge 1
## By: Marco A Rojas
##

DIRNAME=$(dirname $0)
APPMAIL="marquicus@gmail.com"

## Built in functions ##

usage() {
  cat <<EOF
Utility for generating gas prices by day and month

Usage:
  source ${0##*/} [file]
  Parameters:
               Muestra el entorno activado y este menu de ayuda
    [file]     CSV or EXCEL File taken from https://www.eia.gov/dnav/ng/hist/rngwhhdD.htm

Please report errors to $APPMAIL
EOF
}

getdata() {
	python ${DIRNAME}/gas_prices_dates.py -i $1
}

packagedata() {
	python ${DIRNAME}/packaging.py
}

[ "$#" -eq "0" ] && usage && exit 0

if [[ $1 == *.csv || $1 == *.xls || $1 == *.xlsx ]]; then
	getdata $1
	packagedata
else
	usage
fi

# End of file
# vim: set ts=2 sw=2 noet:

