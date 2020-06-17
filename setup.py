from cx_Freeze import setup, Executable

includefiles = ['spaceship.png', 'rocket.png', 'laser.wav',  'explosion.wav',
                'enemy.png', 'bullet_1.png', 'back.png'
                ]
includes = []
excludes = ['Tkinter']
packages = ['pygame']

setup(
    name = 'Space Invader',
    version = '0.1',
    description = 'A space shooting game',
    author = 'Tanjeel',
    options = {'build_exe': {'includes':includes,'excludes':excludes,'packages':packages,'include_files':includefiles}}, 
    executables = [Executable('space_invader.py')]
)