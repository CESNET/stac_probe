# STAC Probe
Really just a simple STAC probe for Nagios monitoring.

## Usage
Default config is specified in `main.py`, variables:

```python
thresholds = {
    'ok': 24,
    'warn': 168
}
default_stac_server = "https://stac.cesnet.cz"
```

Those can be overriden by CLI args:

- `-s, --server` 
  - STAC server to probe.
  - Overrides the `default_stac_server` variable
- `-o, --ok`
  - How old file (in hours) is considered OK? Anything older will be considered WARN or CRIT.
  - Overrides the `thresholds['ok']` variable
- `-w, --warn`
  - How old file (in hours) is considered WARN? Anything older will be considered CRIT.
  - Overrides the `thresholds['warn']` variable

User have to specify STAC collection name to check using the required CLI argument `--collection, -c`

For example final command probing collection `https://stac.cesnet.cz/collecitons/landsat_ot_c2_l1` 
with OK threshold of 84 hours will look like this:

```bash
python main.py -c landsat_ot_c2_l1 -o 84
```

## Output

Scripts prints an informational message to `stdout`. For example (and for OK):

```text
The last entry in collection landsat_ot_c2_l1 is from 2025-03-24.
```

Return values for script are as follows:

```text
0: OK
1: WARN
2: CRIT
```
