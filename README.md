# Global Temperature Time Series

Simple Dashboard for personal didactic use.

## Data Description

Global Temperature Time Series. Data are included from the GISS Surface Temperature (GISTEMP) analysis and the global component of Climate at a Glance (GCAG). Two datasets are provided: 1) global monthly mean and 2) annual mean temperature anomalies in degrees Celsius from 1880 to the present.

[Data source (DataHub)](https://datahub.io/core/global-temp#readme)

# Run Server

Create virtual env

```
python -m venv .venv
```

Activate the new virtual env

```
source .venv/bin/activate
```

Install the dependencies

```
pip install -r requirements.txt
```
Run the app
```
python App.py
```

go on [http://127.0.0.1:8050/](http://127.0.0.1:8050/)