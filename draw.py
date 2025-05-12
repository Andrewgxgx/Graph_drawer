"""
Star this project on Github - https://github.com/Andrewgxgx/Graph_drawer
This script generates a PDF file with a grid of squares, allowing the user to specify the size of the squares and the color of the lines.
It uses the ReportLab library to create the PDF and draw the grid.
Written by Andrew Gx (https://andrewgx.site)
Licensed under : GNU GENERAL PUBLIC LICENSE
"""
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
import os

color_map = {
    "black": colors.black,
    "red": colors.red,
    "green": colors.green,
    "blue": colors.blue,
    "light-blue": colors.HexColor("#ADD8E6"),
    "gray": colors.gray,
    "light-gray": colors.lightgrey,
    "dark-gray": colors.darkgrey,
    "purple": colors.purple,
    "orange": colors.orange,
    "grd": colors.lightgoldenrodyellow
}

def get_user_input():

    try:
        print("Enter 'q' to quit")
        square_width = input("Enter the width of each square (in mm): ")
        if square_width.lower() == 'q':
            return None, None, None  # Signal the main func to stop because inf loop = nono good
        try:
            square_width = float(square_width)
        except ValueError:
            print("Invalid input for width.  Please enter a number or 'q'.")
            return None, None, None

        square_height = input("Enter the height of each square (in mm): ")
        if square_height.lower() == 'q':
            return None, None, None
        try:
            square_height = float(square_height)
        except ValueError:
            print("Invalid input for height.  Please enter a number or 'q'.")
            return None, None, None

        print("\nAvailable colors:", ", ".join(color_map.keys()))
        color_input = input("Enter a color for the lines (e.g., black, blue, light-blue): ").strip().lower()
        if color_input.lower() == 'q':
            return None, None, None
        if color_input not in color_map:
            print("Invalid color. Defaulting to black.")
            color_input = "black"

        return square_width, square_height, color_map[color_input]
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None, None, None

def draw_graph_paper(filename, square_w_mm, square_h_mm, line_color):
    """
    Draws the graph paper on a PDF file.
    Args:
        filename (str): The name of the output PDF file.
        square_w_mm (float): Width of each square in millimeters.
        square_h_mm (float): Height of each square in millimeters.
        line_color (reportlab.color.Color): Color of the lines.
    """
    try:
        c = canvas.Canvas(filename, pagesize=A4)
        width, height = A4  # you can set this to letter or A3 etc, any size

        c.setStrokeColor(line_color)
        c.setLineWidth(0.3)  # Line stroke

        # Convert mm to points
        square_w = square_w_mm * mm
        square_h = square_h_mm * mm

        # Draw vertical lines (y-axis)
        x = 0
        while x <= width:
            c.line(x, 0, x, height)
            x += square_w

        # Draw horizontal lines (x-axis)
        y = 0
        while y <= height:
            c.line(0, y, width, y)
            y += square_h

        c.save()
        print(f"Graph paper saved as '{filename}'.")
    except Exception as e:
        print(f"Error drawing graph paper: {e}")

def main():
    #Loop thingy ahhh
    while True:
        square_w, square_h, line_color = get_user_input()
        if square_w is None: 
            break
        output_file = os.path.join(os.getcwd(), "graph_paper.pdf")
        draw_graph_paper(output_file, square_w, square_h, line_color)

if __name__ == "__main__":
    main()
