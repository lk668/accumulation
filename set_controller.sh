echo "Please input the options of the controller status:"
echo "set or del"
read val
case $val in 
    set)
        sudo ovs-vsctl set-controller br-int tcp:10.108.125.20:8700
        sudo ovs-vsctl set-controller br-sdn tcp:10.108.125.20:8700
        sudo ovs-vsctl set-controller br-extra tcp:10.108.125.20:8700
        ;;
    del)
        sudo ovs-vsctl del-controller br-int
        sudo ovs-vsctl del-controller br-sdn
        sudo ovs-vsctl del-controller br-extra
        ;;
    *)
        echo "ERROR: The options input is error"
        ;;
esac

