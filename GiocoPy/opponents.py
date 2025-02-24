import pygame
from enemies.enemy import Enemy
from enemies.goblins.goblin_warrior import GoblinWarrior
from enemies.goblins.goblin_boss import GoblinBoss
from enemies.goblins.archer_goblin import ArcherGoblin
from enemies.goblins.goblin_killer import GoblinKiller
from enemies.goblins.coward_goblin import CowardGoblin
import assets.variables as variables



def create_enemy(enemy_number):

    enemy = Enemy()

    if enemy_number == 1:
        enemy.create(
        20,
        "./images/enemies/prisoner/prisoner.png",
        "./images/enemies/prisoner/prisoner_jumping.png",
        "./images/enemies/prisoner/prisoner_shooting.png",
        "./images/enemies/prisoner/prisoner_jumping_shooting.png",
        variables.BULLET_ENEMY_SPEED,
        variables.BULLET_ENEMY_DELAY + 5,
        "./images/enemies/prisoner/bullet.png",
        40,
        40
    )
        
    if enemy_number == 2:
        enemy.create(
        20,
        "./images/enemies/golem/golem.png",
        "./images/enemies/golem/golem.png",
        "./images/enemies/golem/golem_shooting.png",
        "./images/enemies/golem/golem_shooting.png",
        variables.BULLET_ENEMY_SPEED,
        variables.BULLET_ENEMY_DELAY,
        "./images/enemies/golem/bullet.png",
        80,
        80
    )
        
    if enemy_number == 3:
        enemy.create(
        20,
        "./images/enemies/wizard/wizard.png",
        "./images/enemies/wizard/wizard_jumping.png",
        "./images/enemies/wizard/wizard_shooting.png",
        "./images/enemies/wizard/wizard_jumping_shooting.png",
        variables.BULLET_ENEMY_SPEED,
        variables.BULLET_ENEMY_DELAY + 5,
        "./images/enemies/wizard/bullet.png",
        60,
        60
    )
        
    if enemy_number == 4:
        enemy.create(
        15,
        "./images/enemies/boss/boss.png",
        "./images/enemies/boss/boss.png",
        "./images/enemies/boss/boss_shooting.png",
        "./images/enemies/boss/boss_jumping_shooting.png",
        variables.BULLET_ENEMY_SPEED,
        variables.BULLET_ENEMY_DELAY - 15,
        "./images/enemies/boss/bullet.png",
        100,
        100
    )
        
    if enemy_number == 5:
        enemy.create(
        20,
        "./images/enemies/final_boss/final_boss.png",
        "./images/enemies/final_boss/final_boss.png",
        "./images/enemies/final_boss/final_boss_shooting.png",
        "./images/enemies/final_boss/final_boss_shooting.png",
        variables.BULLET_ENEMY_SPEED,
        variables.BULLET_ENEMY_DELAY - 25,
        "./images/enemies/final_boss/bullet.png",
        30,
        30
    )
        
    if enemy_number == 6:
        enemy = CowardGoblin()
        enemy.create(
        10,
        "./images/enemies/coward_goblin/coward_goblin.png",
        "./images/enemies/coward_goblin/coward_goblin_jumping.png",
        "./images/enemies/coward_goblin/coward_goblin_shooting.png",
        "./images/enemies/coward_goblin/coward_goblin_jumping_shooting.png",
        variables.BULLET_ENEMY_SPEED + 4,
        variables.BULLET_ENEMY_DELAY + 10,
        "./images/enemies/coward_goblin/bullet.png",
        60,
        60
    )
        
    if enemy_number == 7:
        enemy = GoblinKiller()
        enemy.create(
            15,
            "./images/enemies/slave_goblin/goblinSchiavo.png",
            "./images/enemies/slave_goblin/goblinSchiavo_jumping.png",
            "./images/enemies/slave_goblin/goblinSchiavo_shooting.png",
            "./images/enemies/slave_goblin/goblinSchiavo_shooting.png",
            variables.BULLET_ENEMY_SPEED + 15,
            variables.BULLET_ENEMY_DELAY + 5,
            "./images/enemies/slave_goblin/bullet.png",
            100,
            70
        )
        
    if enemy_number == 8:
        enemy = ArcherGoblin()
        enemy.create(
            20,
            "./images/enemies/archer_goblin/goblin.png",
            "./images/enemies/archer_goblin/goblin_jumping.png",
            "./images/enemies/archer_goblin/goblin_shooting.png",
            "./images/enemies/archer_goblin/goblin_jumping_shooting.png",
            variables.BULLET_ENEMY_SPEED,
            variables.BULLET_ENEMY_DELAY,
            "./images/enemies/archer_goblin/bullet.png",
            40, 
            40
        )
        
    if enemy_number == 9:
        enemy = GoblinWarrior()
        enemy.create(
        15,
        "./images/enemies/goblin_warrior/goblin_warrior.png",
        "./images/enemies/goblin_warrior/goblin_warrior_jumping.png",
        "./images/enemies/goblin_warrior/goblin_warrior_shooting.png",
        "./images/enemies/goblin_warrior/goblin_warrior_jumping_shooting.png",
        variables.BULLET_ENEMY_SPEED + 2,
        variables.BULLET_ENEMY_DELAY - 5,
        "./images/enemies/goblin_warrior/bullet.png",
        80,
        80
    )
        
    if enemy_number == 10:
        enemy = GoblinBoss()
        enemy.create(
        25,
        "./images/enemies/goblin_boss/goblin_boss.png",
        "./images/enemies/goblin_boss/goblin_boss.png",
        "./images/enemies/goblin_boss/goblin_boss_shooting.png",
        "./images/enemies/goblin_boss/goblin_boss_shooting.png",
        variables.BULLET_ENEMY_SPEED + 4,
        variables.BULLET_ENEMY_DELAY - 10,
        "./images/enemies/goblin_boss/bullet.png",
        60,
        60
    )
        
        
        
        
    return enemy



def get_enemy_background(enemy_number):
    
    if enemy_number == 1:
        return "./images/enemies/prisoner/background.png"
    if enemy_number == 2:
        return "./images/enemies/archer_goblin/background.png"
    if enemy_number == 3:
        return "./images/enemies/golem/background.png"
    if enemy_number == 4:
        return "./images/enemies/boss/background.png"
    if enemy_number == 5:
        return "./images/enemies/final_boss/background.png"
    
    if enemy_number == 6:
        return "./images/enemies/coward_goblin/background.png"
    if enemy_number == 7:
        return "./images/enemies/slave_goblin/background.png"
    if enemy_number == 8:
        return "./images/enemies/archer_goblin/background.png"
    if enemy_number == 9:
        return "./images/enemies/goblin_warrior/background.png"
    if enemy_number == 10:
        return "./images/enemies/goblin_boss/background.png"
