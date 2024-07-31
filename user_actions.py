from kivy.uix.relativelayout import RelativeLayout


def keyboard_closed(self):
    self._keyboard.unbind(on_key_down=self.on_keyboard_down)
    self._keyboard.bind(on_key_up=self.on_keyboard_up)
    self._keyboard = None


def on_touch_down(self, touch):
    # state_game_over = False
    # state_game_has_started = False

    if not self.state_game_over and self.state_game_has_started:
        if touch.x < self.width / 2:
            self.current_speed_x = self.SPEED_X
            print('<-')
        else:
            self.current_speed_x = -self.SPEED_X
            print('->')
    return super(RelativeLayout, self).on_touch_down(touch)


def on_touch_up(self, touch):
    self.current_speed_x = 0
    print('UP')


def on_keyboard_down(self, keyboard, keycode, text, modifiers):
    if keycode[1] == 'left':
        self.current_speed_x = self.SPEED_X
        print('<-')
    elif keycode[1] == 'right':
        self.current_speed_x = -self.SPEED_X
        print('->')
    return True


def on_keyboard_up(self, keyboard, keycode):
    self.current_speed_x = 0