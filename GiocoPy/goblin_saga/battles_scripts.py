battles = [
    [
        {
            "type": "dialogue",
            "directory_path": "./images/goblin_saga/chief",
            "number_of_frames": 10,
            "character_position": "left",
            "background_path": "./images/goblin_saga/backgrounds/city.png",
            "speech":
                [
                    "Hello, I am the chief of this village. I am glad you are here to help us. Our village has been taken under siege by a goblin group. Our defenses have tried to stand to enemy attacks but there was nothing to be done.",
                    "Goblins succeded in going beyond the walls and entered the village. They have been stealing our food and loot our people. At this rate, we should abandon the village...",
                    "Please, help us. You are our only hope...",
                    "Wonderful! I will try to help you giving some information about the goblin that you are going to face and recovering your health after each battle.",
                    "Your first enemy is the coward goblin. He is the weakest of the goblins, but he is still a threat. It will try to hit you throwing wooden sticks. It's not so resistant, so you should be able to defeat it easily.",
                    "Go and defeat him!"
                ],
            "voice_path": "voices/goblin_saga/chief1"
        },
        {
            "type": "enemy_dialogue",
            "character_path": "./images/enemies/coward_goblin/coward_goblin.png",
            "number_of_frames": 1,
            "character_position": "rigth",
            "background_path": "./images/goblin_saga/backgrounds/city.png",
            "speech":
                [
                    "Ahahah! You are so weak! I will defeat you easily!",
                ],
            "voice_path": "voices/goblin_saga/coward_goblin"
        },
        {
            "type": "preparing_battle",
            "enemy_number": 6,
            "xp_reward": 50,
        },
        {
            "type": "battle",
        }
    ],
    [
        {
            "type": "dialogue",
            "directory_path": "./images/goblin_saga/chief",
            "number_of_frames": 10,
            "character_position": "left",
            "background_path": "./images/goblin_saga/backgrounds/city.png",
            "speech":
                [
                    "You did it! You defeated the coward goblin! You are a great warrior!",
                    "However, you should be careful. The others are stronger and your travel will be harder.",
                    "The next enemy is the goblin stabber. He is not so resistant too, but he is faster than the coward goblin.",
                ]
        },
        {
            "type": "enemy_dialogue",
            "character_path": "./images/enemies/slave_goblin/goblinSchiavo.png",
            "number_of_frames": 1,
            "character_position": "rigth",
            "background_path": "./images/goblin_saga/backgrounds/city.png",
            "speech":
                [
                    "The coward goblin is just the weakest of us. You will never defeat me!",
                ],
            "voice_path": "voices/goblin_saga/slave_goblin"
        },
        {
            "type": "preparing_battle",
            "enemy_number": 7,
            "xp_reward": 100,
        },
        {
            "type": "battle",
        }
    ],
    [
        {
            "type": "dialogue",
            "directory_path": "./images/goblin_saga/chief",
            "number_of_frames": 10,
            "character_position": "left",
            "background_path": "./images/goblin_saga/backgrounds/city.png",
            "speech":
                [
                    "prossimo: archer goblin",
                ]
        },
        {
            "type": "enemy_dialogue",
            "character_path": "./images/enemies/archer_goblin/goblin.png",
            "number_of_frames": 1,
            "character_position": "rigth",
            "background_path": "./images/goblin_saga/backgrounds/city.png",
            "speech":
                [
                    "ciao bello",
                ],
            "voice_path": "voices/goblin_saga/archer_goblin"
        },
        {
            "type": "preparing_battle",
            "enemy_number": 8,
            "xp_reward": 150,
        },
        {
            "type": "battle",
        }
    ],
    [
        {
            "type": "dialogue",
            "directory_path": "./images/goblin_saga/chief",
            "number_of_frames": 10,
            "character_position": "left",
            "background_path": "./images/goblin_saga/backgrounds/city.png",
            "speech":
                [
                    "prossimo: goblin warrior",
                ]
        },
        {
            "type": "enemy_dialogue",
            "character_path": "./images/enemies/goblin_warrior/goblin_warrior.png",
            "number_of_frames": 1,
            "character_position": "rigth",
            "background_path": "./images/goblin_saga/backgrounds/city.png",
            "speech":
                [
                    "ciao bello",
                ],
            "voice_path": "voices/goblin_saga/goblin_warrior"
        },
        {
            "type": "preparing_battle",
            "enemy_number": 9,
            "xp_reward": 200,
        },
        {
            "type": "battle",
        }

    ],
    [
        {
            "type": "dialogue",
            "directory_path": "./images/goblin_saga/chief",
            "number_of_frames": 10,
            "character_position": "left",
            "background_path": "./images/goblin_saga/backgrounds/city.png",
            "speech":
                [
                    "prossimo: goblin boss",
                ]
        },
        {
            "type": "enemy_dialogue",
            "character_path": "./images/enemies/goblin_boss/goblin_boss.png",
            "number_of_frames": 1,
            "character_position": "rigth",
            "background_path": "./images/goblin_saga/backgrounds/city.png",
            "speech":
                [
                    "ciao bello",
                ],
            "voice_path": "voices/goblin_saga/goblin_boss"
        },
        {
            "type": "preparing_battle",
            "enemy_number": 10,
            "xp_reward": 250,
        },
        {
            "type": "battle",
        }
    ],
]