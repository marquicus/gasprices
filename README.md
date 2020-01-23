gasprices
========================

Challenge 1

Getting Started
---------------

Generate new virtualenv with python 3.6+ and activate

```
python -m venv venv
source venv/bin/activate
```

Install all dependencies:

```
pip install -r requirements.txt
```
Download csv or xls file from https://www.eia.gov/dnav/ng/hist/rngwhhdD.htm with view history "daily"

Execute shell `gasprices.sh` passing as parameter the downloaded file (you can use the absolute|relative path if not in same directory)
```
./gasprices.sh Henry_Hub_Natural_Gas_Spot_Price.csv
```

