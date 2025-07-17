# AT2 Reader

A Python script to read `.AT2` ground motion files and extract acceleration time series, time step, number of points, and peak ground acceleration (PGA).

## Usage

```python

from at2_reader import read_at2_file

acc, dt, npts, pga = read_at2_file("example.at2")

print(f"PGA = {pga} g, Time step = {dt} s, NPTS = {npts}")

