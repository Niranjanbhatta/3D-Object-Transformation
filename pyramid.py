# Import the vtk module for visualization
import vtk

# Define a custom interactor style class inheriting from vtkInteractorStyleTrackballCamera
class CustomInteractorStyle(vtk.vtkInteractorStyleTrackballCamera):
    # Initialize the custom interactor style
    def __init__(self):
        # Add an observer for the "KeyPressEvent" which calls the on_key_press method
        self.AddObserver("KeyPressEvent", self.on_key_press)

    # Define the method to handle key press events
    def on_key_press(self, obj, event):
        # Get the key symbol (e.g., "Left", "Right") of the key that was pressed
        key = self.GetInteractor().GetKeySym()
        # Move the actor in response to arrow key presses
        if key == "Left":
            self.actor.AddPosition(-0.1, 0, 0)
        elif key == "Right":
            self.actor.AddPosition(0.1, 0, 0)
        elif key == "Up":
            self.actor.AddPosition(0, 0.1, 0)
        elif key == "Down":
            self.actor.AddPosition(0, -0.1, 0)
        
        # Access the renderer associated with the actor and render it
        self.actor.GetMapper().Update()
        self.actor.GetMapper().Modified()
        self.GetInteractor().Render()

    # Define a method to set the actor to be manipulated
    def set_actor(self, actor):
        self.actor = actor


# Function to create a VTK example with a pyramid
def create_vtk_pyramid_example():
    # Define the vertices of the pyramid
    points = vtk.vtkPoints()
    points.InsertNextPoint(-1.0, -1.0, 0.0)  # Base vertex 0
    points.InsertNextPoint( 1.0, -1.0, 0.0)  # Base vertex 1
    points.InsertNextPoint( 1.0,  1.0, 0.0)  # Base vertex 2
    points.InsertNextPoint(-1.0,  1.0, 0.0)  # Base vertex 3
    points.InsertNextPoint( 0.0,  0.0, 2.0)  # Apex (taller top)

    # Create the base of the pyramid (a square)
    base = vtk.vtkCellArray()
    base.InsertNextCell(4)
    base.InsertCellPoint(0)
    base.InsertCellPoint(1)
    base.InsertCellPoint(2)
    base.InsertCellPoint(3)

    # Create the sides of the pyramid (triangles connecting apex to each base vertex)
    side1 = vtk.vtkTriangle()
    side1.GetPointIds().SetId(0, 0)  # Base vertex 0
    side1.GetPointIds().SetId(1, 4)  # Apex
    side1.GetPointIds().SetId(2, 1)  # Base vertex 1

    side2 = vtk.vtkTriangle()
    side2.GetPointIds().SetId(0, 1)  # Base vertex 1
    side2.GetPointIds().SetId(1, 4)  # Apex
    side2.GetPointIds().SetId(2, 2)  # Base vertex 2

    side3 = vtk.vtkTriangle()
    side3.GetPointIds().SetId(0, 2)  # Base vertex 2
    side3.GetPointIds().SetId(1, 4)  # Apex
    side3.GetPointIds().SetId(2, 3)  # Base vertex 3

    side4 = vtk.vtkTriangle()
    side4.GetPointIds().SetId(0, 3)  # Base vertex 3
    side4.GetPointIds().SetId(1, 4)  # Apex
    side4.GetPointIds().SetId(2, 0)  # Base vertex 0

    # Create a polydata to represent the pyramid
    pyramid = vtk.vtkPolyData()
    pyramid.SetPoints(points)
    pyramid.SetPolys(base)
    pyramid.GetPolys().InsertNextCell(side1)
    pyramid.GetPolys().InsertNextCell(side2)
    pyramid.GetPolys().InsertNextCell(side3)
    pyramid.GetPolys().InsertNextCell(side4)

    # Create a mapper object to map the pyramid data to graphics primitives
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputData(pyramid)

    # Create an actor object to represent the pyramid in the scene
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    # Create a renderer object to manage the rendering process
    renderer = vtk.vtkRenderer()
    renderer.AddActor(actor)
    renderer.SetBackground(0.1, 0.2, 0.4)  # Set background color (optional)

    # Create a render window object to provide a window for rendering
    renderWindow = vtk.vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindow.SetWindowName("VTK Pyramid Example")

    # Create a render window interactor to handle user interactions with the render window
    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    # Use the trackball camera interactor style to enable zooming
    interactorStyle = vtk.vtkInteractorStyleTrackballCamera()
    renderWindowInteractor.SetInteractorStyle(interactorStyle)

    # Use the custom interactor style to handle key presses
    style = CustomInteractorStyle()
    style.set_actor(actor)
    renderWindowInteractor.SetInteractorStyle(style)

    # Initialize and start the event loop
    renderWindow.Render()
    renderWindowInteractor.Start()

# Call the function if this script is run directly
if __name__ == "__main__":
    create_vtk_pyramid_example()
