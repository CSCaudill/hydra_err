from dataclasses import dataclass
from hydra.core.config_store import ConfigStore


@dataclass
class Account:
    user: str
    password: str


@dataclass
class Config:
    account: Account


def register_configs() -> None:
    cs = ConfigStore.instance()
    cs.store(name="base_config", node=Config)
    cs.store(group="account", name="base_account", node=Account)
