import subprocess
import sys

def test_ejecucion_sistema_completo():
    """Ejecuta main.py como proceso independiente para validar el sistema."""
    proceso = subprocess.run(
        [sys.executable, "main.py"],
        capture_output=True,
        text=True
    )
    assert proceso.returncode == 0
    assert "Resultado de compra:" in proceso.stdout
    assert "'estado': 'exito'" in proceso.stdout