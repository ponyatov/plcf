import os
"generic VSCode project generator"

import datetime as dt

APP = 'plcf'
TITLE = 'Programming Language Construction Framework'
ABOUT = ''

VERSION = '0.0.1'
AUTHOR = 'Dmitry Ponyatov'
EMAIL = 'dponyatov@gmail.com'
YEAR = dt.date.today().year
LICENSE = 'MIT'


class JSON():
    def __init__(self, name):
        with open(name, 'w') as json:
            print('{\n}', file=json)


class Project():

    def README(self):
        with open('README.md', 'w') as readme:
            print(
                f'''\
# `{APP}` {VERSION}
## {TITLE}

(c) {AUTHOR} <<{EMAIL}>> {YEAR} {LICENSE}''', file=readme)
            if ABOUT:
                print(ABOUT, file=readme)

    def gitignore(self):
        with open('.gitignore', 'w') as giti:
            print('''*~
*.swp
*.log''', file=giti)
            for i in self.GITI:
                print(i, file=giti)
            print('!.gitignore''', file=giti)

    def mkdir(self, name, extra=None):
        if not os.path.exists(name):
            os.mkdir(name)
        with open(f'{name}/.gitignore', 'w') as giti:
            if extra is not None:
                print(extra, file=giti)
            print('!.gitignore\n', file=giti)

    def bin(self): self.mkdir('bin', '*')
    def doc(self): self.mkdir('doc', 'html/')
    def lib(self): self.mkdir('lib')
    def inc(self): self.mkdir('inc')
    def src(self): self.mkdir('src')
    def tmp(self): self.mkdir('tmp', '*')
    def ref(self): self.mkdir('ref', '*')

    JSONS = ['extensions', 'settings', 'tasks', 'launch']
    GITI = []

    def extensions(self):
        with open('.vscode/extensions.json', 'w') as json:
            print('{}', file=json)

    def settins(self):
        with open('.vscode/settins.json', 'w') as json:
            print('{}', file=json)

    def tasks(self):
        with open('.vscode/tasks.json', 'w') as json:
            print('{}', file=json)

    def launch(self):
        with open('.vscode/launch.json', 'w') as json:
            print('{}', file=json)

    def vscode(self):
        self.mkdir('.vscode')
        for json in self.JSONS:
            JSON(f'.vscode/{json}.json')
        self.extensions()
        self.settins()
        self.tasks()
        self.launch()

    def vsext(self):
        self.mkdir('vscode')
        JSON('vscode/project.json')

    def dirs(self):
        self.bin()
        self.doc()
        self.lib()
        self.inc()
        self.src()
        self.tmp()
        self.ref()

    def __init__(self):
        self.gen()

    def cpp(self):
        open(f'inc/{APP}.hpp', 'w').close()
        open(f'src/{APP}.cpp', 'w').close()
        open(f'src/{APP}.lex', 'w').close()
        open(f'src/{APP}.yacc', 'w').close()

    def gen(self):
        self.README()
        self.dirs()
        self.gitignore()
        self.vscode()
        self.vsext()
        self.cpp()


class PyProject(Project):
    GITI = Project.GITI + ['__pycache__/', '*.pyc']


class CppProject(Project):
    GITI = Project.GITI + ['*.o', '*.obj']


class ThisProject(PyProject, CppProject):
    GITI = sorted(list(set(PyProject.GITI + CppProject.GITI)))


if __name__ == '__main__':
    ThisProject()
    os.system('git add -A')
    print(f'git remote add gh git@github.com:ponyatov/{APP}.git')
    print(f'git remote add flic git@gitflic.ru:dponyatov/{APP}.git')
