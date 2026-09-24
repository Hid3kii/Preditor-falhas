import subprocess
import sys

def ping_host(host: str, count: int = 4) -> str:
    """
    Executa pings ICMP contra um host alvo utilizando o utilitário do SO.
    
    Args:
        host (str): Endereço IP ou domínio do destino.
        count (int): Quantidade de pacotes a enviar (padrão: 4).
        
    Returns:
        str: Saída de texto bruta retornada pelo comando ping.
    """
    # Trata incompatibilidade de flags entre Windows (-n) e Unix (-c)
    param = "-n" if sys.platform.startswith("win") else "-c"
    
    # Execução em lista previne vulnerabilidades de Command Injection
    resultado = subprocess.run(
        ["ping", param, str(count), host],
        capture_output=True,
        text=True
    )
    
    return resultado.stdout


if __name__ == "__main__":
    host_alvo = "8.8.8.8"
    print(f"Executando ping de teste para {host_alvo}...")
    saida = ping_host(host_alvo)
    print(saida)