#!/usr/bin/env python3

from ncclient import manager

conn = manager.connect(
        host='192.168.2.50', 
        port=22, 
        username='cisco', 
        password='cisco', 
        hostkey_verify=False, 
        device_params={'name': 'nexus'}, 
        look_for_keys=False
        )

for value in conn.server_capabilities:
    print(value)

conn.close_session()
