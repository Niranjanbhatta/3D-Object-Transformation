import vtk

class CustomInteractorStyle(vtk.vtkInteractorStyleTrackballCamera):
    def __init__(self):
        # Initialize the superclass and add an observer for key press events
        self.AddObserver("KeyPressEvent", self.on_key_press)

    def on_key_press(self, obj, event):
        # Get the key that was pressed
        key = self.GetInteractor().GetKeySym()
        # Adjust actor position based on arrow key presses
        if key == "Left":
            self.actor.AddPosition(-0.1, 0, 0)
        elif key == "Right":
            self.actor.AddPosition(0.1, 0, 0)
        elif key == "Up":
            self.actor.AddPosition(0, 0.1, 0)
        elif key == "Down":
            self.actor.AddPosition(0, -0.1, 0)
        
        # Update and render the actor
        self.actor.GetMapper().Update()
        self.actor.GetMapper().Modified()
        self.GetInteractor().Render()

    def set_actor(self, actor):
        # Method to set the actor that will be manipulated
        self.actor = actor

def create_vtk_sphere_example():
    # Create a sphere source with specified properties
    sphereSource = vtk.vtkSphereSource()
    sphereSource.SetRadius(1.0)  # Set radius of the sphere
    sphereSource.SetThetaResolution(30)  # Set theta (longitude) resolution
    sphereSource.SetPhiResolution(15)  # Set phi (latitude) resolution

    # Create a mapper to map the sphere source data to graphics primitives
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(sphereSource.GetOutputPort())

    # Create an actor to represent the sphere in the scene
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    # Create a renderer to manage the rendering process
    renderer = vtk.vtkRenderer()
    renderer.AddActor(actor)
    renderer.SetBackground(0.1, 0.2, 0.4)  # Set background color (optional)

    # Create a render window to provide a window for rendering
    renderWindow = vtk.vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindow.SetWindowName("VTK Sphere Example")

    # Create a render window interactor to handle user interactions
    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    # Use the trackball camera interactor style for default interactions
    interactorStyle = vtk.vtkInteractorStyleTrackballCamera()
    renderWindowInteractor.SetInteractorStyle(interactorStyle)

    # Use the custom interactor style to handle key presses
    style = CustomInteractorStyle()
    style.set_actor(actor)
    renderWindowInteractor.SetInteractorStyle(style)

    # Initialize and start the event loop for rendering
    renderWindow.Render()
    renderWindowInteractor.Start()

# Call the function if this script is run directly
if __name__ == "__main__":
    create_vtk_sphere_example()
