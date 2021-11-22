from git import Repo


class Clonador:
    def __init__(self, url, nome):
        Repo.clone_from(url, nome)


if __name__ == '__main__':
    Repo.clone_from('https://github.com/TechDriversFatec/TechDrivers', 'teste', progress=Progress())



