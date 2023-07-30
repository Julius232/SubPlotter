# SubPlotter

SubPlotter is a Python script to visualize data from a given file. It parses the file, organizes the data, and then uses Plotly to create a graph.

The data is structured in a specific way: it consists of alternating positive and negative numbers, representing time intervals (in some unit) of 'on' and 'off' states, respectively.

The script produces a step graph where 'on' states are represented by 1 and 'off' states by 0. The x-axis represents the cumulative time.

## Installation

1. Clone the repository
2. Navigate to the project directory in your terminal
3. Install the necessary packages by running `pip install -r requirements.txt`

## Usage

Run the script with the filename as an argument. For example, if your file is named 'filename.sub', you would run:

```shell
python PlotSub.py filename.sub