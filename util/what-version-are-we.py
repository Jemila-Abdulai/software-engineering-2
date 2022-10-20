# Ccript that tells you what version we are at, cor CI
import configparser
import os

config = configparser.ConfigParser()
repoRoot = os.path.join(os.path.realpath(__file__), "../")

versionConfig = config.read(os.path.join("VERSION.cfg"))

print(config["bumpversion"]["current_version"], end="")
