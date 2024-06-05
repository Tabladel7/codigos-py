import requests
import json

url = "http://<IP_DEL_ROUTER>:<PUERTO>/restconf/data/ietf-interfaces:interfaces/interface=Loopback55"
username = "TU_USUARIO"
password = "TU_CONTRASEÑA"

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

body = {
    "ietf-interfaces:interface": {
        "name": "Loopback55",
        "description": "Nombre Apellido",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "172.16.55.1",
                    "netmask": "255.255.255.0"
                }
            ]
        }
    }
}

auth = (username, password)
response = requests.put(url, headers=headers, auth=auth, data=json.dumps(body))
