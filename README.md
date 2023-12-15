# histeventexplorer_pkg

A Python package for retrieving and visualizing historical events with associated imagery.

## Installation

```bash
$ pip install histeventexplorer_pkg
```
## Features
**Comprehensive Event Retrieval**: Access a vast database of historical events by year, with the ability to filter by significance, region, and more.

**Trend Analysis Tools**: Investigate patterns and frequencies of historical occurrences using our trend analysis functions.

**Imagery Association**: Bring history to life by fetching related imagery for any listed historical event, enhancing the storytelling and educational value.

**Data Visualization**: Utilize built-in methods to graphically represent historical trends over time, aiding in data-driven storytelling and presentations.

## Usage

**Fetching Events**:
Retrieve historical events by simply specifying the year


you can simply use:

```python 
from histeventexplorer_pkg import fetch_events

events = fetch_events(api_key, year=1914)
```
**Analyzing Trends:**
Analyze the frequency of event types over a century:

```python 
from histeventexplorer_pkg import analyze_event_trends

event_trends = analyze_event_trends(api_key, 1800, 1900, ['war', 'revolution'])
```
**Visualizing Data:**
Generate visual representations of event trends:
```python 
from histeventexplorer_pkg import visualize_event_trends

visualize_event_trends(event_trends)
```


**Obtaining Imagery:**
Fetch related images for an immersive experience:
```python 

from histeventexplorer_pkg import fetch_event_images

images = fetch_event_images(api_key, 'moon landing')
```
For more examples and usage, please refer to the Documentation.

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`histeventexplorer_pkg` was created by Ruining Feng. It is licensed under the terms of the MIT license.

## Credits

`histeventexplorer_pkg` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
