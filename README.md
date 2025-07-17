# AT2 Reader

This Python script is designed to read acceleration time histories in the `.AT2` format, commonly used in earthquake engineering and compatible with the **NGA-West2 database**, developed by the **Pacific Earthquake Engineering Research Center (PEER)**.

The **NGA-West2 database** is a comprehensive and curated collection of strong ground motion recordings from shallow crustal earthquakes in active tectonic regions. These records are widely used for:

- Ground motion selection  
- Structural response analysis  
- Nonlinear time history analysis  

The `.AT2` format is one of the standard output formats provided by the [PEER Ground Motion Database](https://ngawest2.berkeley.edu), and includes metadata such as the number of points (`NPTS`), time step (`DT`), and acceleration values.

---

## Features

- Reads `.AT2` ground motion files
- Extracts:
  - Acceleration time series (in g)
  - Time step (`DT`)
  - Number of points (`NPTS`)
  - Peak Ground Acceleration (`PGA`)

---

## Usage

```python
from at2_reader import read_at2_file

acc, dt, npts, pga = read_at2_file("example.at2")

print(f"PGA = {pga} g, Time step = {dt} s, NPTS = {npts}")
