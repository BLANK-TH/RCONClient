from rcon.source import Client

def send_rcon_command(command: str, ip: str, port: int, passwd: str) -> str:
    with Client(ip, port, passwd=passwd) as client:
        response = client.run(command)
        return response
