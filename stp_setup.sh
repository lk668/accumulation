echo "Please input the stp options of the OVS:"
echo "true or false:"
read val

sudo ovs-vsctl set bridge br-int stp_enable=$val
sudo ovs-vsctl set bridge br-sdn stp_enable=$val
sudo ovs-vsctl set bridge br-extra stp_enable=$val

