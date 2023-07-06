# Sales Data Visualization

This code repository contains a Python project that uses the flet library for data visualization and pandas for data handling. This project creates a visualization from the sales data stored in a CSV file. The main components of this project include the DataVisualization class, the main function, and several helper functions. The code creates a pie chart for sales data comparison, and lists with the numerical values on the side.

## Project Structure

The project structure is as follows:

- main.py - The main file where the sales data is loaded, processed, and visualized.
- sales.csv - The file containing the sales data. This file should be located in the same directory as the main file. The data should start from the 6th column with the first 5 columns used for metadata or other purposes.
Main Components

## The project has two main components:

1. DataVisualization - This is a class that creates a pie chart using the flet library. It takes in the sum of the sales for the month, the maximum sum, the spacing, and color as inputs. It initializes the chart with these parameters and returns the pie chart when the build() function is called.

2. main() - This is the main function of the project. It does several things:

- It loads and cleans the sales data from the CSV file.
- It processes the data, replacing any missing values or placeholders with zeros.
- It calculates the sum and maximum sum for each month.
- It creates a stack of pie charts for each month, with the size and color of each chart varying.
- It creates a list of sales sums for each month and displays them next to the corresponding chart.

## File Format
The input data file should be a CSV file in the format described below:

- The first 5 columns can be any data or metadata.
- The remaining columns should be monthly sales data, with each column representing a different month.

## Usage

- The DataVisualization class is a self-contained class that you can import and use in other projects.

- To run the main program, run the command python main.py in the project directory. Ensure that the "sales.csv" file is located in the same directory.

## Dependencies
This project uses the following Python packages:

- flet
- pandas
- math

These dependencies can be installed via pip:
```
pip install flet pandas
```

## Future Enhancements
In the future, I plan to make the following enhancements:

- Provide the ability to handle different data input formats.
- Improve data preprocessing capabilities.
- Improve the color scheme of the visualizations for better visibility and understanding.
- Add interactivity to the visualizations.

## Contributions
Feel free to fork the project and submit your pull requests. Please make sure your code is well-formatted and documented.

## License
This project is released under the MIT license. For more details, see the LICENSE file.


![Demo GIF](vd.gif)
