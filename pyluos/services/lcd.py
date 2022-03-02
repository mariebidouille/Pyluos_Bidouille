from .service import Service, interact 

import time

class Lcd(Service):
    
    _MODE_RIGHT_TO_LEFT = 0
    _MODE_SCROLL_DISPLAY = 1
    _MODE_AUTOSCROLL = 2
    _MODE_BLINK = 3
    _MODE_CURSOR = 4
    _MODE_DISPLAY = 5

    def __init__(self, id, alias, device):
        Service.__init__(self, 'Lcd', id, alias, device)
        self._config = [False] * (Lcd._MODE_DISPLAY+1)
        self._config[Lcd._MODE_DISPLAY] = True

    def _convert_config(self):
        return int(''.join(['1' if c else '0' for c in self._config]), 2) # Table read reversly

    def bit(self, i, enable):
        self._config = self._config[:i] + () + self._config[i + 1:]

    def display(self, new_val):
        if (self._config[Lcd._MODE_DISPLAY] != True):
            print("text mode could be disabled in the service please use 'device.service.display_mode = True' to enable it")
        self._push_value('text', new_val) 
        time.sleep(0.01)

    #Modes 
    @property 
    def display_mode(self):
        return self._config[Lcd._MODE_DISPLAY]

    @display_mode.setter
    def display_mode(self, enable):
        self._config[Lcd._MODE_DISPLAY] = True if enable != 0 else False
        self._push_value('parameters', self._convert_config())
        time.sleep(0.01)
    
    @property
    def cursor_mode(self):
        return self._config[Lcd._MODE_CURSOR]
    
    @cursor_mode.setter
    def cursor_mode(self, enable):
        self._config[Lcd._MODE_CURSOR] = True if enable != 0 else False
        self._push_value('parameters', self._convert_config())
        time.sleep(0.01)

    @property
    def blink_mode(self):
        return self._config[Lcd._MODE_BLINK]
    
    @blink_mode.setter
    def blink_mode(self, enable):
        self._config[Lcd._MODE_BLINK] = True if enable != 0 else False
        self._push_value('parameters', self._convert_config())
        time.sleep(0.01)

    @property
    def autoscroll_mode(self):
        return self._config[Lcd._MODE_AUTOSCROLL]
    
    @autoscroll_mode.setter
    def autoscroll_mode(self, enable):
        self._config[Lcd._MODE_AUTOSCROLL] = True if enable != 0 else False
        self._push_value('parameters', self._convert_config())
        time.sleep(0.01)
    
    @property
    def right_to_left_mode(self):
        return self._config[Lcd._MODE_RIGHT_TO_LEFT]
    
    @right_to_left_mode.setter
    def right_to_left_mode(self, enable):
        self._config[Lcd._MODE_RIGHT_TO_LEFT] = True if enable != 0 else False
        self._push_value('parameters', self._convert_config())
        time.sleep(0.01)
    
    @property
    def scroll_display_mode(self):
        return self._config[Lcd._MODE_SCROLL_DISPLAY]
    
    @scroll_display_mode.setter
    def scroll_display_mode(self, enable):
        self._config[Lcd._MODE_SCROLL_DISPLAY] = True if enable != 0 else False
        self._push_value('parameters', self._convert_config())
        time.sleep(0.01)

    def reinit(self):
        self._push_value('reinit', None)
        time.sleep(0.01)

