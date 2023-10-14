import arcade as ar

#const
sc_w = 1000
sc_h = 650
sc_title = 'test'

#const for scale
charecter_scal = 1
tile_scal = 0.5

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

        #set bg color
        ar.set_background_color(ar.color.ARSENIC)


    def setup(self):

        #setup the game

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

        #create physics engine
        self.physics_engine = ar.PhysicsEngineSimple(
                self.player_sprite, self.scene.get_sprite_list('Walls')
                )


    def on_draw(self):

        #render the sc
        self.clear()

        #draw our scene
        self.scene.draw()


    def on_key_press(self, key, modifiers):

        if key == ar.key.W:
            self.player_sprite.change_y = player_sp
        elif key == ar.key.S:
            self.player_sprite.change_y = -player_sp
        elif key == ar.key.A:
            self.player_sprite.change_x = -player_sp
        elif key == ar.key.D:
            self.player_sprite.change_x = player_sp



    def on_key_release(self, key, modifiers):

        if key == ar.key.W:
            self.player_sprite.change_y = 0
        elif key == ar.key.S:
            self.player_sprite.change_y = 0
        elif key == ar.key.A:
            self.player_sprite.change_x = 0
        elif key == ar.key.D:
            self.player_sprite.change_x = 0


    def on_update(self, delta_time):

        #game logic

        #move player
        self.physics_engine.update()


def main():
    window = MyGame()
    window.setup()
    ar.run()


if __name__ == '__main__':
    main()
