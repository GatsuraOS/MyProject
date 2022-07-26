from json import load

from Schemas import ConfigSchema


def load_config() -> ConfigSchema:
    with open("config.json", "r", encoding="UTF-8") as file:
        return ConfigSchema(**load(file))


CONFIG: ConfigSchema = load_config()
