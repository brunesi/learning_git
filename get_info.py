import platform
import subprocess
from datetime import datetime, timezone

def obter_infos():
    # 1. Datas e Horários
    utc_now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
    local_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # 2. Informações do Sistema (uname)
    sistema = platform.uname()

    # 3. Informações da Distribuição (lsb_release)
    # Usamos subprocess pois lsb_release é um comando do sistema Linux
    try:
        distro = subprocess.check_output(['lsb_release', '-ds'], universal_newlines=True).strip()
    except Exception:
        distro = "Informação lsb_release não disponível"

    # Exibição dos resultados
    print("-" * 30)
    print(f"Data/Hora: {utc_now} UTC ({local_now} Local)")
    print("-" * 30)
    print(f"Sistema: {sistema.system}")
    print(f"Node Name: {sistema.node}")
    print(f"Release: {sistema.release}")
    print(f"Versão: {sistema.version}")
    print(f"Máquina: {sistema.machine}")
    print(f"Distribuição: {distro}")
    print("-" * 30)

if __name__ == "__main__":
    obter_infos()
