#!/bin/bash
mysql -uusername -ppassword<< EOF
use nova;
DELETE FROM nova.security_group_instance_association instance_uuid='$1';
DELETE FROM nova.instance_info_caches WHERE instance_uuid='$1';

DELETE FROM nova.instance_actions WHERE instance_uuid='$1';
DELETE FROM nova.instances WHERE uuid='$1';
EOF
