#!/usr/bin/env bash

#输出代码所在的行数,该方法在./xx.sh的时候生效
#$LINENO是linux内部的环境变量
echo $LINENO

#获取当前文件的目录的绝对路径
#dirname $0是文件相对执行命令所在路径的相对路径
TOP_DIR=$(cd $(dirname $0) && pwd)
echo $TOP_DIR
echo $(dirname $0)

##文件比较运算
    #-e filename     如果 filename存在，则为真   [ -e /var/log/syslog ]
    #-d filename     如果 filename为目录，则为真     [ -d /tmp/mydir ]
    #-f filename     如果 filename为常规文件，则为真     [ -f /usr/bin/grep ]
    #-L filename     如果 filename为符号链接，则为真     [ -L /usr/bin/grep ]
    #-r filename     如果 filename可读，则为真   [ -r /var/log/syslog ]
    #-w filename     如果 filename可写，则为真   [ -w /var/mytmp.txt ]
    #-x filename     如果 filename可执行，则为真     [ -L /usr/bin/grep ]
    #filename1-nt filename2  如果 filename1比 filename2新，则为真    [ /tmp/install/etc/services -nt /etc/services ]
    #filename1-ot filename2  如果 filename1比 filename2旧，则为真    [ /boot/bzImage -ot arch/i386/boot/bzImage ]

##字符串比较运算
    #-z string   如果 string长度为零，则为真     [ -z "$myvar" ]
    #-n string   如果 string长度非零，则为真     [ -n "$myvar" ]
    #string1= string2    如果 string1与 string2相同，则为真  [ "$myvar" = "one two three" ]
    #string1!= string2   如果 string1与 string2不同，则为真  [ "$myvar" != "one two three" ]

##算数比较运算
    #num1-eq num2    等于[ 3 -eq $mynum ]
    #num1-ne num2    不等于[ 3 -ne $mynum ]
    #num1-lt num2    小于[ 3 -lt $mynum ]
    #num1-le num2    小于或等于[ 3 -le $mynum ]
    #num1-gt num2    大于[ 3 -gt $mynum ]
    #num1-ge num2    大于或等于[ 3 -ge $mynum ]
if [[ -r $TOP_DIR/xxx ]]; then
    rm $TOP_DIR/xxx
fi

#判断用户是不是root
if [[$EUID -eq 0]]; then
    echo "It is a root user"
fi
