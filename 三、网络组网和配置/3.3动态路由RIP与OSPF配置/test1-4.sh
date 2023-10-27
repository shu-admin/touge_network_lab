echo 'hostname R1
--
router ospf 1
--
 network 10.0.0.0 0.0.0.255 area 1
 network 12.12.12.0 0.0.0.255 area 1
hostname R2
--
router ospf 1
--
 network 12.12.12.0 0.0.0.255 area 1
 network 23.23.23.0 0.0.0.255 area 0
hostname R3
--
router ospf 1
--
 network 23.23.23.0 0.0.0.255 area 0
 network 34.34.34.0 0.0.0.255 area 2
hostname R4
--
router ospf 1
--
 network 20.0.0.0 0.0.0.255 area 2
 network 34.34.34.0 0.0.0.255 area 2
'