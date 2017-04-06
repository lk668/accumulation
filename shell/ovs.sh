ovs-vsctl add-br br-sdn

ovs-vsctl add-port br-sdn "sdni" -- set interface "sdni" type=patch options:peer="isdn"
ovs-vsctl add-port br-int "isdn" -- set interface "isdn" type=patch options:peer="sdni"


ovs-vsctl add-port br-sdn gre0 -- set interface gre0 type=gre options:local_ip=10.108.125.234 options:remote_ip=10.108.126.4 options:df_default=true
ovs-vsctl add-port br-sdn gre1 -- set interface gre1 type=gre options:local_ip=10.108.125.234 options:remote_ip=10.108.126.3 options:df_default=true
