"""Importing ursina all"""
from ursina import *
"""importing first person player class"""
from ursina.prefabs.first_person_controller import FirstPersonController

# Variable for Ursina()
app = Ursina()

# loading blocks, audio
grass_block = load_texture('Grass_Block_TEX.png')
diamond_block = load_texture('diamond-minecraft-2.png')
dust_block = load_texture('dust.png')
block_audio = Audio('sound.mp3', loop=False, autoplay=False)

# fps counter(default this True)
window.fps_counter.enabled = False

# exit button
window.exit_button.visible = False

# update function, changing block and sword movement
block = 1
def update():
    global block
    if held_keys['1']:
        block = 1
    if held_keys['2']:
        block = 2
    if held_keys['3']:
        block = 3

    """For sword movement"""
    if held_keys['left mouse'] or held_keys['right mouse']:

        my_hand.movement()
    else:
        my_hand.default()

# voxel every block
class Voxel(Button):
    def __init__(self, position, texture=grass_block, model='Grass_Block.obj', scale = 0.5, origin_y = 0.5):
        super().__init__(
            parent = scene,
            position = position,
            model = model,
            origin_y = origin_y,
            texture = texture,
            color = color.color(0,0, random.uniform(0.9,1)),
            scale = scale
        )

    # For blocks changing
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                block_audio.play()
                if block == 1:
                    Voxel(position = self.position + mouse.normal, texture=grass_block, model='Grass_Block.obj')
                if block == 2:
                    Voxel(position = self.position + mouse.normal, texture=diamond_block, model = 'cube', scale=1, origin_y=-0.23)
                if block == 3:
                    Voxel(position = self.position + mouse.normal, texture=dust_block, model = 'cube', scale=1, origin_y=-0.23)

            if key == 'right mouse down':
                block_audio.play()
                destroy(self)

# sky texture
class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = 'skybox.png',
            scale = 150,
            double_sided = True
        )

# Sword
class Sword(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'minecraft_photos/DiamondSword2.obj',
            texture = 'minecraft_photos/Diffuse.png',
            scale = 0.01,
            rotation = Vec3(135,115,135),
            position = Vec2(0.15,-0.3)
        )

    def movement(self):
        self.position = Vec2(0.1, -0.1)

    def default(self):
        self.position = Vec2(0.15,-0.3)

# Sword object
my_hand = Sword()

# Creating multiple voxel for land
for z in range(20):
    for x in range(20):
        voxel = Voxel(position=(x,0,z))

# First Person View object
cam = FirstPersonController()

# Sky class object
sky = Sky()

# Running the app
app.run()

# Note: CLass method and function call automatically in every frame.
