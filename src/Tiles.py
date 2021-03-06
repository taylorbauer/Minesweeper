"""
The tiles class handles the states of each tile object, letting the program know if a certain tile is a flag, a mine, or already revealed.
"""
import pygame
from random import randint
flag_image = pygame.image.load("src/pixel_flag.png")

class Tiles:
    
    num_adjacent_mines = 0
    pygame.font.init()
    mine_font = pygame.font.SysFont('Helvetica', 26)

    # Constructor initializing a Tile object
    # Tile object will be set to self, booleans(is_revealed, is_flag, is_mine)
    # Display will be called to draw a tile on the board
    def __init__(self, is_revealed, is_flag, is_mine, display):
        """
        @pre Initialization of a tile object
        @param
            is_revealed: takes a bool if tile object is already revealed
            is_flag: takes a bool if tile object is flagged
            is_mine: takes a bool if tile object is a mine
        @post Initializes display to display, surf to a surface size of 30x30 pixels, then fills each surface with a gray color"
        @return None
        """ 
        self.is_revealed = is_revealed
        self.is_flag = is_flag
        self.is_mine = is_mine
        self.display = display
        self.surf = pygame.Surface((30,30))
        self.surf.fill((100,100,100))
  
    # Draws number of adjacent mines to screen
    def tile_reveal(self):
        """
        Displays the number of mines surrounding a revealed tile (if any exist)

        @pre Expects a call from a user right-click
        @param None
        @post Revealed tiles will now display number of adjacent mines
        @return None
        """
        self.is_revealed = True
        self.surf.fill((50,50,50))
        if(not self.is_flag and not self.is_mine):
            if self.num_adjacent_mines > 0:
                adj_text = str(self.num_adjacent_mines)
                font_surf = self.mine_font.render(adj_text, True, (250, 250, 250))
                self.surf.blit(font_surf, (5, 5))
        

    def tile_flag(self):
        """
        Adds or removes flag image on tile

        @pre Expects a call from a user left-click
        @param None
        @post Flag is displayed or removed from tile
        @return Returns an integer that will add or subtract from the flag count that is being compared to the mine count
        """
        if self.is_revealed == False:
            if self.is_flag == False:
                self.is_flag = True
                self.surf.blit(flag_image, (5, 5))
                if self.is_mine == True:
                    self.surf.blit(flag_image, (5, 5))
                    return(1)
                else: 
                    return 0
            elif self.is_flag == True:
                self.is_flag = False
                self.surf.fill((100, 100, 100))
                if self.is_mine == True:
                    self.surf.fill((100, 100, 100))
                    return(-1)
                else:
                    return 0
        else:
            return 0