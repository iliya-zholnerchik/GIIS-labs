import pyvista as pv

class Figures:

    default_colors = ( "ff0000", "28e5da", "0000ff", "ffff00", "c8bebe", "f79292" )
    default_meshes = ( pv.Cube, pv.Octahedron , pv.Cone, pv.Cylinder, pv.Icosahedron, pv.Dodecahedron )
    
    def __init__(self, meshes=default_meshes, colors=default_colors) -> None:
        self.plotter = pv.Plotter()
        for i, mesh in enumerate(meshes):
            added = self.plotter.add_mesh(mesh(), name=str(mesh), color=colors[i])
            added.SetVisibility(False)
            self.plotter.add_checkbox_button_widget( added.SetVisibility, value=False, position=(5, 70 * i), color_on=colors[i] )
    
    def show(self):
        self.plotter.show()

Figures().show()