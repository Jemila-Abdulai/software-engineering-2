# Ccript that tells you what version we are at, cor CI
import configparser
import os

config = configparser.ConfigParser()
repoRoot = os.path.join(os.path.realpath(__file__), "../")
print(repoRoot)

versionConfig = config.read(os.path.join(repoRoot, "VERSION.cfg"))

print(config["bumpversion"]["current_version"], end="")
