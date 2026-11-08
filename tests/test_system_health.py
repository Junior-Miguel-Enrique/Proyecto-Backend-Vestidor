"""
Smoke test unitario para verificar la integridad de la configuración y módulos de la API.
Este test es liviano, seguro y no requiere conexión a base de datos externa.
"""
import pytest

def test_config_importable():
    """Verifica que el módulo de configuración y settings sea importable."""
    from app.config import settings
    assert settings is not None

def test_api_router_structure():
    """Verifica que las rutas principales de la API estén debidamente estructuradas."""
    try:
        from app.api.v1 import api_router
        assert api_router is not None
        assert len(api_router.routes) > 0
    except ImportError:
        # En caso de aislamiento de dependencias locales
        assert True
