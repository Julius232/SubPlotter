# SubPlotter

SubPlotter is a Python script to visualize data from given files. It supports two types of files, which can represent different types of signals:

1. `.sub` files, which represent Sub-GHz signals. In these files, the data consists of alternating positive and negative numbers, representing time intervals (in some unit) of 'on' and 'off' states, respectively.

2. `.ir` files, which represent IR signals. In these files, the data is a series of positive numbers, and 'on' and 'off' states alternate with every number.

The script organizes the data and then uses Plotly to create a graph. It produces a step graph where 'on' states are represented by 1 and 'off' states by 0. The x-axis represents the cumulative time.

## Installation

1. Clone the repository
2. Navigate to the project directory in your terminal
3. Install the necessary packages by running `pip install -r requirements.txt`

## Usage

Run the script with the filename as an argument.


```shell
python PlotSub.py filename.sub

python PlotIr.py filename.ir