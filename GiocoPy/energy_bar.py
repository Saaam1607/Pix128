import pygame
from energy_tick import EnergyTick



class EnergyBar(pygame.sprite.Sprite):


    def __init__(self, max_energy_number, energy_recovery_delay):
        super().__init__()
        self.max_energy_number = max_energy_number
        self.energy_recovery_delay = energy_recovery_delay
        self.rect = pygame.Rect(10, 90, max_energy_number * 10 + 20, 40)
        self.image = pygame.image.load("./images/energy_container.png")
        self.image = pygame.transform.scale(self.image, (max_energy_number * 10 + 20, 40))
        self.energies_group = pygame.sprite.Group()
        for i in range(max_energy_number):
            if i % 10 < 5:
                self.energies_group.add(EnergyTick(20 + i * 10, 100, 10, 20, "images/energy_tick1.png"))
            else:
                self.energies_group.add(EnergyTick(20 + i * 10, 100, 10, 20, "images/energy_tick2.png"))
        self.recover_countdown = self.energy_recovery_delay


    def get_available_energy(self):
        return len(self.energies_group)


    def consume_energy(self):
        if (self.get_available_energy() >= 5):
            for i in range(5):
                last_energy = self.energies_group.sprites()[-1]
                last_energy.kill()
            

    def check_number_range(self, number):
        tens = (number // 10) % 10
        number_without_tens = number - tens * 10
        if number_without_tens < 5:
            return True
        else:
            return False


    def recover_energy(self):        
        if (self.recover_countdown == 0):
            if (self.get_available_energy() <= self.max_energy_number):
                if self.check_number_range(self.get_available_energy()):
                    self.energies_group.add(EnergyTick(20 + len(self.energies_group) * 10, 100, 10, 20, "images/energy_tick1.png"))
                else:
                    self.energies_group.add(EnergyTick(20 + len(self.energies_group) * 10, 100, 10, 20, "images/energy_tick2.png"))
            self.recover_countdown = self.energy_recovery_delay
        else:
            self.recover_countdown -= 1
            

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.energies_group.draw(screen)
        