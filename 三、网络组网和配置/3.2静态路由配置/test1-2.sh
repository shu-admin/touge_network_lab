echo 'set pcname PC1
ip 10.0.0.1 10.0.0.2 24
set pcname PC2
ip 20.0.0.1 20.0.0.2 24
hostname R1
--
interface FastEthernet0/0
 ip address 10.0.0.2 255.255.255.0
--
interface FastEthernet0/1
 ip address 12.12.12.1 255.255.255.0
hostname R2
--
interface FastEthernet0/0
 ip address 12.12.12.2 255.255.255.0
--
interface FastEthernet0/1
 ip address 23.23.23.1 255.255.255.0
hostname R3
--
interface FastEthernet0/0
 ip address 20.0.0.2 255.255.255.0
--
interface FastEthernet0/1
 ip address 23.23.23.2 255.255.255.0
'