from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    app_env: str = "development"
    llm_model: str = "llama3.1:latest"
    litellm_base: str = "http://litellm:4000"
    litellm_key: str = "sk-change-me"


settings = Settings()
