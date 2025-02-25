import pygame
from energy_tick import EnergyTick

class SubEnergyBar(pygame.sprite.Sprite):

    def __init__(self, max_energy_number, energy_recovery_delay):
        super().__init__()
        self.max_energy_number = max_energy_number
        self.energy_recovery_delay = energy_recovery_delay
        self.rect = pygame.Rect(10, 140, max_energy_number * 10 + 20, 40)
        self.image = pygame.image.load("./images/sub_energy_container.png")
        self.image = pygame.transform.scale(self.image, (max_energy_number * 10 + 20, 40))
        self.energies_group = pygame.sprite.Group()
        # for i in range(max_energy_number):
            # self.energies_group.add(EnergyTick(20 + i * 10, 150, 10, 20, "images/sub_energy_tick.png"))
        self.recover_countdown = self.energy_recovery_delay

    def get_available_energy(self):
        return len(self.energies_group)

    def consume_energy(self):
        self.energies_group.empty()

    def recover_energy(self):        
        if (self.recover_countdown == 0):
            if (self.get_available_energy() <= self.max_energy_number):
                self.energies_group.add(EnergyTick(20 + len(self.energies_group) * 10, 150, 10, 20, "images/sub_energy_tick.png"))
            self.recover_countdown = self.energy_recovery_delay
        else:
            self.recover_countdown -= 1
            
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.energies_group.draw(screen)