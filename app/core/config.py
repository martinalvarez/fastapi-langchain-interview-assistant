# app/core/config.py

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from typing import Optional

# 1. Heredamos de BaseSettings para la carga automática
class Settings(BaseSettings):
    """
    Clase de configuración principal que carga variables de entorno.
    """
    # LangChain/LLM Settings
    # Usaremos Field para definir un valor por defecto si no se encuentra
    # y para tipar correctamente la variable.
    openai_api_key: str = Field(
        ..., validation_alias="OPENAI_API_KEY", description="La clave de API de OpenAI."
    )
    
    # FastAPI Settings
    project_name: str = "FastLLMPrep: Interview Assistant"
    
    # 2. Configuración para Pydantic Settings
    model_config = SettingsConfigDict(
        env_file=".env",              # Carga variables desde el archivo .env
        extra='ignore'                # Ignora variables de entorno que no están definidas aquí
    )

# 3. Creamos una instancia que se usará en todo el proyecto.
settings = Settings()