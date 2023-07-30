import sys
import pandas as pd
import plotly.graph_objects as go

# Check if filename is given
if len(sys.argv) < 2:
    print("Please provide a file name.")
    sys.exit()

filename = sys.argv[1]

# read and preprocess data
with open(filename, 'r') as file:
    content = file.readlines()

new_content = []

for line in content:
    if "RAW_Data: " in line:
        line = line.replace("RAW_Data: ", "")
        line = line.replace(",", "\n")
        new_content.extend(line.split())

# Remove all non-numeric values
new_content = [value for value in new_content if value.replace('-', '').isnumeric()]

# absolute time and pulse states
data = list(map(int, new_content))
time = [abs(value) for value in data]
pulse = [1 if value >= 0 else 0 for value in data]

# cumulative time and corresponding pulse states
cumulative_time = []
cumulative_pulse = []
cumulative = 0
for i in range(len(time)):
    cumulative_pulse.append(pulse[i])
    cumulative_time.append(cumulative)
    cumulative += time[i]

# Create DataFrame
df = pd.DataFrame({
    'time': time,
    'pulse': cumulative_pulse,
    'cumulative_time': cumulative_time,
})

# visualize
fig = go.Figure(data=go.Scatter(x=df['cumulative_time'], y=df['pulse'], mode='lines', line_shape='hv'))
fig.show()
