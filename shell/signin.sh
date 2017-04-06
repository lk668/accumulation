echo "Please input the server you will ssh:"
echo "Num         ServerName"
echo "1           xxx"
read val
case $val in
	1)
		ssh xxx@10.10.10.10
		;;
	*)
		echo "ERROR: The number you input is error!"
		;;
esac
