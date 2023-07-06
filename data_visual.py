import flet as ft
import pandas as pd
from math import pi



# Class for data visualization
class DataVisualization(ft.UserControl):
    def __init__(self, month_sum: float, max_sum: float, spacing: int, color: str):
        # Initialization of the main parameters of the class: sum for the month, difference with the maximum sum, color, and spacing
        self.month_sum: float = month_sum
        self.delta_sum: float = max_sum - self.month_sum
        self.color = color

        # Creating a LineChart with two sections: one represents the sum of sales for the month, the other - the difference between the maximum sum and the sum of sales for the month
        self.chart: ft.Control = ft.PieChart(
            sections=[
                ft.PieChartSection(value=self.month_sum, color=self.color, radius=15),
                ft.PieChartSection(
                    value=self.delta_sum,
                    color=ft.colors.with_opacity(0.025, "white"),
                    radius=15,
                ),
            ],
            sections_space=0,
            center_space_radius=spacing,
            rotate=ft.Rotate((pi) / 2),
        )

        # Initialization of the parent class
        super().__init__()


    def build(self):
        return self.chart

# Main function of the program
def main(page: ft.Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    # Initialization of the list of colors for the chart
    colors: list = []
    for num in range(1, 13):
        colors.append(f"blue{num}00")

    # Loading and cleaning the data from the "sales.csv" file
    sales_data = pd.read_csv("sales.csv")

    # Data processing: removing commas, replacing missing values with 0
    sales_data = sales_data.replace("n.a.", pd.NA)
    sales_data = sales_data.dropna()

    # Initialization of lists for storing data by months, sums, and maximum sums
    for MONTH in sales_data.columns[5:]:
        sales_data[MONTH] = sales_data[MONTH].str.replace(",", "")
        sales_data[MONTH] = sales_data[MONTH].str.replace("not available", "0")
        sales_data[MONTH] = sales_data[MONTH].str.replace("not avilable", "0")
        sales_data[MONTH] = pd.DataFrame(sales_data, columns=[MONTH], dtype=float)

    month_list = []
    max_num = []
    sum_list = []

    # Filling the lists with data from the processed data
    for MONTH in sales_data.columns[5:]:
        month_list.append(MONTH)
        max_num.append(sales_data[MONTH].sum())
    sum_list = max_num
    max_num = max(max_num)

    # Creating a stack of visualizations taking into account the scale, size, and color
    stack = ft.Stack(scale=ft.Scale(0.65))
    size = 100
    for index, MONTH in enumerate(sales_data.columns[5:]):
        stack.controls.append(
            DataVisualization(
                month_sum=sales_data[MONTH].sum(),
                max_sum=max_num,
                spacing=size,
                color=colors[index],
            )
        )

        size += 30

    # Function that changes the highlighting of visualizations according to user interaction
    def highlight_data(e):
        if e.data == "true":
            for index, chart in enumerate(stack.controls[:]):
                if index != e.control.data:
                    chart.chart.sections[0].color = ft.colors.with_opacity(
                        0.05, "white10"
                    )
                    chart.update()
        else:
            for index, chart in enumerate(stack.controls[:]):
                if index != e.control.data:
                    chart.chart.sections[0].color = colors[index]
                    chart.update()

    # Create the sum of columns
    col = ft.Column(alignment="center")
    for index in range(len(month_list)):
        col.controls.append(
            #
            ft.Container(
                on_hover=lambda e: highlight_data(e),
                data=index,
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Row(
                            alignment="start",
                            controls=[
                                ft.Container(
                                    width=9,
                                    height=9,
                                    shape=ft.BoxShape("circle"),
                                    bgcolor=colors[index],
                                ),
                                ft.Text(month_list[index], size=14, weight="bold"),
                            ],
                        ),
                        ft.Row(
                            alignment="end",
                            controls=[
                                ft.Text(
                                    sum_list[index],
                                    size=14,
                                    weight="bold",
                                ),
                            ],
                        ),
                    ],
                ),
            )
        )

    # Creating a page structure with controls and padding
    page.add(

        # Page layout in the application widnow
        ft.Row(
            alignment="center",
            controls=[

                # The left window with PiChart visualization
                ft.Container(
                    width=500,
                    height=500,
                    bgcolor=ft.colors.with_opacity(0.009, "white"),
                    content=stack,

                ),

                # The right window with data
                ft.Container(
                    height=500,
                    width=400,
                    padding=50,
                    bgcolor=ft.colors.with_opacity(0.009, "white"),
                    content=col,

                ),
            ],
        )
    )

    page.update()


if __name__ == "__main__":
    ft.flet.app(target=main)