from rcon.source import Client

def send_rcon_command(command: str, ip: str, port: int, passwd: str) -> str:
    # FIXME: SRCDS sends multiple packets for large responses, unfortunately it seems that the rcon library doesn't handle this.
    #        This means that large responses will be truncated. Will need to fix at some point following workaround listed
    #        here: https://developer.valvesoftware.com/wiki/Source_RCON_Protocol#Multiple-packet_Responses
    with Client(ip, port, passwd=passwd) as client:
        response = client.run(command)
        return response
