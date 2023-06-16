from vedo import *
import trimesh
import pyrender

class Renderer:

    def __init__(self, download_path, entries):
        self.download_path = download_path
        self.entries = entries

    def obj_render(self, entry):
        path = '/'.join([self.download_path, entry])
        hologram = self.entries["db"][entry]["hologram"]

        mesh = Mesh(path + '/' + hologram['filename'])
        mesh.texture(path + '/' + hologram['textureFilenames'][0])
        mesh.show()

    def glb_render(self, entry):
        path = '/'.join([self.download_path, entry])
        hologram = self.entries["db"][entry]["hologram"]

        model = trimesh.load(path + '/' + hologram['filename'])
        scene = pyrender.Scene.from_trimesh_scene(model)
        pyrender.Viewer(scene, use_raymond_lighting=True, use_direct_lighting=True)


