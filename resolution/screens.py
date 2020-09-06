class Screen:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def size(self):
        return self.width, self.height

    def rotate(self):
        tmp = self.width
        self.width = self.height
        self.height = tmp
        return self


class Standard:
    S_240P = Screen(320, 240)
    VGA = Screen(640, 480)
    SVGA = Screen(800, 600)
    XGA = Screen(1024, 768)
    SXGA = Screen(1280, 1024)


class Wide:
    W_240P = Screen(426, 240)
    W_480P = Screen(720, 480)
    W_720P = Screen(1280, 720)
    HD_1080P = Screen(1920, 1080)
    HD_4K = Screen(3840, 2160)


class Console:
    ATARI_2600 = Screen(160, 192)
    NES = Screen(256, 224)
    SNES = Screen(512, 448)
    NINTENDO_DS = Screen(256, 192)
    NINTENDO_2DS_TOP = Screen(400, 240)
    NINTENDO_3DS = Screen(320, 240)
    NINTENDO_3DS_TOP = Screen(800, 240)
    NINTENDO_SWITCH = Wide.W_720P
    GAMEBOY = Screen(160, 144)
    SEGA_GENESIS = Screen(320, 224)
    PSP = Screen(480, 272)
    PLAYSTATION = Screen(640, 480)
