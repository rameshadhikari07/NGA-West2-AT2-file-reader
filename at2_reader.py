import numpy as np
def read_at2_file(filepath):
    """
    Reads a .AT2 ground motion file and extracts acceleration time series data.

    The function parses the .AT2 file format used in earthquake engineering, 
    extracting the number of points (NPTS), time step (DT), acceleration values, 
    and computes the Peak Ground Acceleration (PGA).

    Parameters
    ----------
    filepath : str
        Path to the .AT2 file.

    Returns
    -------
    acc_values : np.ndarray
        Array of acceleration values (in g).
    dt : float
        Time step (in seconds).
    npts : int
        Number of data points.
    pga : float
        Peak Ground Acceleration (absolute maximum of the acceleration array, in g).


    Notes
    -----.
    - Issues a warning if the number of data points doesn't match the header value (NPTS).
    """
    
    with open(filepath, 'r') as file:
        lines = file.readlines()
    
    # Extract NPTS and DT from the 3rd line
    for line in lines:
        if 'NPTS=' in line and 'DT=' in line:
            parts = line.split(',')
            npts = int(parts[0].split('=')[1].strip())
            dt = float(parts[1].split('=')[1].strip().split()[0])
            break

    # Read acceleration values from line 5 onwards
    acc_values = []
    for line in lines[4:]:
        acc_values.extend([float(val) for val in line.strip().split()])
    
    pga = np.abs(acc_values).max()
    
    # Verify expected number of points
    if len(acc_values) != npts:
        print(f"Warning: Expected {npts} values, but found {len(acc_values)}.")

    return np.array(acc_values), dt, npts, pga