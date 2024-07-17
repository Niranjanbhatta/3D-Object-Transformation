# Import the vtk module
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
        # Move the actor left by 0.1 units on the x-axis if the "Left" key is pressed
        if key == "Left":
            self.actor.AddPosition(-0.1, 0, 0)
        # Move the actor right by 0.1 units on the x-axis if the "Right" key is pressed
        elif key == "Right":
            self.actor.AddPosition(0.1, 0, 0)
        # Move the actor up by 0.1 units on the y-axis if the "Up" key is pressed
        elif key == "Up":
            self.actor.AddPosition(0, 0.1, 0)
        # Move the actor down by 0.1 units on the y-axis if the "Down" key is pressed
        elif key == "Down":
            self.actor.AddPosition(0, -0.1, 0)
        
        # Access the renderer associated with the actor and render it
        self.actor.GetMapper().Update()
        self.actor.GetMapper().Modified()
        self.GetInteractor().Render()

    # Define a method to set the actor to be manipulated
    def set_actor(self, actor):
        self.actor = actor


# Function to create a VTK example with a cuboid
def create_vtk_cuboid_example():
    # Create a cuboid source with specified dimensions
    cuboidSource = vtk.vtkCubeSource()
    cuboidSource.SetXLength(2.0)  # Set length along x-axis
    cuboidSource.SetYLength(3.0)  # Set length along y-axis
    cuboidSource.SetZLength(4.0)  # Set length along z-axis

    # Create a mapper object to map the cuboid data to graphics primitives
    mapper = vtk.vtkPolyDataMapper()
    # Connect the mapper to the output of the cuboid source
    mapper.SetInputConnection(cuboidSource.GetOutputPort())

    # Create an actor object to represent the cuboid in the scene
    actor = vtk.vtkActor()
    # Set the mapper for the actor
    actor.SetMapper(mapper)

    # Create a renderer object to manage the rendering process
    renderer = vtk.vtkRenderer()
    # Add the actor to the renderer
    renderer.AddActor(actor)
    # Set the background color of the renderer (optional)
    renderer.SetBackground(0.1, 0.2, 0.4)

    # Create a render window object to provide a window for rendering
    renderWindow = vtk.vtkRenderWindow()
    # Add the renderer to the render window
    renderWindow.AddRenderer(renderer)
    # Set the title of the render window
    renderWindow.SetWindowName("VTK Cuboid Example")

    # Create a render window interactor to handle user interactions with the render window
    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    # Link the interactor to the render window
    renderWindowInteractor.SetRenderWindow(renderWindow)

    # Use the trackball camera interactor style to enable zooming
    interactorStyle = vtk.vtkInteractorStyleTrackballCamera()
    # Set the interactor style for the render window interactor
    renderWindowInteractor.SetInteractorStyle(interactorStyle)

    # Create an instance of the custom interactor style
    style = CustomInteractorStyle()
    # Set the actor for the custom interactor style
    style.set_actor(actor)
    # Set the custom interactor style for the render window interactor
    renderWindowInteractor.SetInteractorStyle(style)

    # Initialize and start the rendering event loop
    renderWindow.Render()
    renderWindowInteractor.Start()

# Call the function if this script is run directly
if __name__ == "__main__":
    create_vtk_cuboid_example()
