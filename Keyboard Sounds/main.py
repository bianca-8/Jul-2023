import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((200, 200))
    pygame.display.set_caption("Keyboard Sound Player")
    
    # Define a dictionary to map keys to sounds
    key_sounds = {
        pygame.K_a: "sound_a.wav",
        pygame.K_b: "sound_b.wav",
        pygame.K_c: "sound_c.wav",
        # Add more keys and sound filenames as needed
    }
    
    # Load sounds
    sounds = {key: pygame.mixer.Sound(filename) for key, filename in key_sounds.items()}
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in sounds:
                    # Play the corresponding sound when a valid key is pressed
                    sounds[event.key].play()
        
        # Fill the screen to avoid visual artifacts
        screen.fill((0, 0, 0))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
