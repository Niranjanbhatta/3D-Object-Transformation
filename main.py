import tkinter as tk
from tkinter import messagebox
import vtk

# Import your shape functions
from cone import create_vtk_cone_example
from cube import create_vtk_cube_example
from cuboid import create_vtk_cuboid_example
from cylinder import create_vtk_cylinder_example
from pyramid import create_vtk_pyramid_example
from sphere import create_vtk_sphere_example

def show_shape(shape_function):
    # Call the selected shape function
    shape_function()

def select_shape():
    # Create a tkinter window
    root = tk.Tk()
    root.title("Select Shape")
    root.geometry("300x370")
    
    # Define shape options
    shapes = [
        ("Cone", create_vtk_cone_example),
        ("Cube", create_vtk_cube_example),
        ("Cuboid", create_vtk_cuboid_example),
        ("Cylinder", create_vtk_cylinder_example),
        ("Pyramid", create_vtk_pyramid_example),
        ("Sphere", create_vtk_sphere_example)
    ]

    # Configure padding between buttons
    root.grid_columnconfigure(0, weight=1)  # Make column resizable
    root.grid_rowconfigure(len(shapes), weight=1)  # Make last row resizable
    padding_y = 10  # Vertical padding between buttons

    # Create buttons for each shape
    for index, (shape_name, shape_function) in enumerate(shapes):
        # Create button with grid layout, each button on a new row
        btn = tk.Button(root, text=shape_name, width=20, height=2, command=lambda f=shape_function: show_shape(f))
        btn.grid(row=index, column=0,padx=padding_y ,pady=padding_y, sticky="nsew")


    root.mainloop()

# Main entry point
if __name__ == "__main__":
    select_shape()
