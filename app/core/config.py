from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Config(BaseSettings):
    app_name: str = "My app name"
    debug: bool = False

    db_user: str = ""
    db_pass: str = ""
    db_name: str = ""

    origins: str = ""
    port: int = 8000

    @property
    def property_example(self):
        return "some constructed property"

    @property
    def allowed_origins(self):
        return self.origins.split(",") if self.origins else "*"


config = Config()
