import arcade as ar

#const
sc_w = 1000
sc_h = 650
sc_title = 'test'

#const for scale
charecter_scal = 1
tile_scal = 0.5
ammo_scal = 0.3

#movment speed per frame
player_sp = 5

class MyGame(ar.Window):
    def __init__(self):

        #call the parent class and set up the window
        super().__init__(sc_w, sc_h, sc_title)

        #our scene obj
        self.scene = None

        #our phisics engine
        self.physics_engine = None

        #separete variable that holds the playre sprite
        self.player_sprite = None

        # A Camera that can be used for scrolling the screen
        self.camera = None

        #gui camera
        self.gui_camera = None

        #keep trak score
        self.bullets = 0

        #set bg color
        ar.set_background_color(ar.color.ARSENIC)


    def setup(self):

        #setup the game

        # Set up the Camera
        self.camera = ar.Camera(self.width, self.height)

        #set up gui camera
        self.gui_camera = ar.Camera(self.width, self.height)

        #keep track score
        self.bullets = 10

        #init scene
        self.scene = ar.Scene()

        #create sprite list
        self.scene.add_sprite_list('Player')
        self.scene.add_sprite_list('Walls', use_spatial_hash=True)

        #setup the player
        image_sourse = 'images/test_player.png'
        self.player_sprite = ar.Sprite(image_sourse, charecter_scal)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 64
        self.scene.add_sprite('Player', self.player_sprite)

        #put some box
        cord_list = [[512, 96], [256, 96], [768, 96]]
        for cord in cord_list:
            wall = ar.Sprite('images/boxCrate.png', tile_scal)
            wall.position = cord
            self.scene.add_sprite('Walls', wall)


        # use loop for create some ammo
        for x in range(128, 1250, 256):
            bullet = ar.Sprite('images/coinBronze.png', ammo_scal)
            bullet.center_x = x
            bullet.center_y = 256
            self.scene.add_sprite('Ammo', bullet)

        #create physics engine
        self.physics_engine = ar.PhysicsEngineSimple(
                self.player_sprite, self.scene.get_sprite_list('Walls')
                )


    def on_draw(self):

        #render the sc
        self.clear()

        #draw our scene
        self.scene.draw()

        #activate gui camera
        self.gui_camera.use()

        #draw our ammo on the screen
        ammo_text = f'ammo: {self.bullets}'
        ar.draw_text(
                ammo_text,
                10, 10,
                ar.color.WHITE,
                18)


    def on_key_press(self, key, modifiers):

        if key == ar.key.W:
            self.player_sprite.change_y = player_sp
        if key == ar.key.S:
            self.player_sprite.change_y = -player_sp
        if key == ar.key.A:
            self.player_sprite.change_x = -player_sp
        if key == ar.key.D:
            self.player_sprite.change_x = player_sp



    def on_key_release(self, key, modifiers):


        if key == ar.key.W or key == ar.key.S:
            self.player_sprite.change_y = 0
        elif key == ar.key.A or key == ar.key.D:
            self.player_sprite.change_x = 0

    def center_camera_to_player(self):
        screen_center_x = self.player_sprite.center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.player_sprite.center_y - (self.camera.viewport_height / 2)

        #Don't let camera travel past 0
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x, screen_center_y

        #move camera to player with smoothly
        self.camera.move_to(player_centered, 0.1)


    def on_update(self, delta_time):

        #game logic

        # Activate our Camera
        self.camera.use()

        #move player
        self.physics_engine.update()

        #see if we hit any ammo
        ammo_hit_list = ar.check_for_collision_with_list(
                self.player_sprite, self.scene['Ammo'])

        #loop throught each ammo we hit and remove it
        for bullet in ammo_hit_list:
            #remove ammo
            bullet.remove_from_sprite_lists()
            # add 10 bullet to ammo
            self.bullets += 10

        #Position the camera
        self.center_camera_to_player()

def main():
    window = MyGame()
    window.setup()
    ar.run()


if __name__ == '__main__':
    main()
