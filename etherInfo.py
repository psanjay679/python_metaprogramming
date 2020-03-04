import re
new_hardware = ['FireEyeNX4500', 'FireEyeNX3500', 'FireEyeNX2550', 'FireEyeNX5500']
result = {}
data = """Appliance: FireEye1400
================================================================================================================================================
Interface  PCI-ID        MAC Address       Link  Speed    Transceiver   Driver   Version    Device info
================================================================================================================================================
 pether3  0000:01:00.0  00:0c:bd:06:d8:9b  yes   1000Mb/s   --------      igb   5.3.4.4-pq  82576 Gigabit Network Connection     IntelCorporation                       
 pether4  0000:01:00.1  00:0c:bd:06:d8:9a  yes   1000Mb/s   --------      igb   5.3.4.4-pq  82576 Gigabit Network Connection     IntelCorporation                       
  ether1  0000:02:00.0  0c:c4:7a:05:d9:cc  yes   1000Mb/s   --------    e1000e1.9.5-NAPI-PQ  82574L Gigabit Network Connection     SuperMicro                       
 pether2  0000:03:00.0  0c:c4:7a:05:d9:cd  yes    100Mb/s   --------    e1000e1.9.5-NAPI-PQ  82574L Gigabit Network Connection     SuperMicro                       
================================================================================================================================================
Interface A Ports : pether3 pether4
================================================================================================================================================
"""

data = data.replace('(B', '').split('\n')
print(data)
# data = data.splitlines()
model = data[0].split(':')[1].strip()
i = 4  # Skip starting 4 lines
n = len(data)
temp = {}
while i < n:
    t = data[i].strip().split(' ', 1)
    if len(t) == 2:
        temp[t[0].strip()] = t[1].strip()
    i += 1

interface_re = re.compile('([A-Z])\s+Ports\s+:\s+(\w+)\s+(\w+)')
for intf in interface_re.findall(temp['Interface']):
    result[intf[0]] = {'ports': [intf[1], intf[2]], 'type': 'fiber'}
    if 'Gigabit Network Connection' in temp[intf[1]]:
        result[intf[0]]['type'] = 'ethernet'
    elif 'VMXNET3 Ethernet Controller' in temp[intf[1]]:
        result[intf[0]]['type'] = 'VM'
    elif model in new_hardware:
        result[intf[0]]['type'] = 'fiber-new'

print(result)
