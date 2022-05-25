from typing import List, Optional

import typer
from omegaconf import OmegaConf, DictConfig

from hydra import compose, initialize

app = typer.Typer()

#https://stackoverflow.com/questions/70811640/using-typer-and-hydra-together
def my_compose(overrides: Optional[List[str]]) -> DictConfig:
    with initialize(config_path="conf", job_name="test_app", version_base="1.1"):
        return compose(config_name="config", overrides=overrides)

@app.command()
def say_hi(overrides: Optional[List[str]] = typer.Argument(None)):
    #python3 main.py say-hi db.user=customuser
    print("HI!")
    print(f"Got {overrides=}")
    cfg = my_compose(overrides)
    print("\nHydra config:")
    print(OmegaConf.to_yaml(cfg))

@app.command()
def say_bye(overrides: Optional[List[str]] = typer.Argument(None)):
    #python3 main.py say-bye
    cfg = my_compose(overrides)
    ...
    print("BYE!")

@app.command()
def build(overrides: Optional[List[str]] = typer.Argument(None)):
    #python3 main.py say-bye
    cfg = my_compose(overrides)
    ...
    print("Build phase...")

@app.command()
def train(overrides: Optional[List[str]] = typer.Argument(None)):
    #python3 main.py say-bye
    cfg = my_compose(overrides)
    ...
    print("train phase...")

@app.command()
def deploy(overrides: Optional[List[str]] = typer.Argument(None)):
    #python3 main.py say-bye
    cfg = my_compose(overrides)
    ...
    print("deploy phase...")

if __name__ == "__main__":
    app()