from hd_core.defs import functions, classes, enums


from test_infomation import *

# def test_shell_file2str():
#     shell_content_of_echo_hello_sh = '''#!/bin/bash
# echo "Hi, This is \`hd_core\` written by https://github.com/imwanpu using to harden Linux, like CentOS 7, Ubuntu 20.04 and so on."
# date -u > /home/hd_admin/hello.txt
# '''
#     assert functions.shell_file2str('echo_hello.sh') == shell_content_of_echo_hello_sh

# def test_run_command_to_target_host():
#     target_host = classes.TargetHost(
#         address_ipv4=test_centos7_ip,
#         username=test_centos7_username,
#         password=test_centos7_password
#         )
#     command = '''#!/bin/bash
# date -u > /home/hd_admin/hello.txt
# ''' # 执行完此测试后, 测试机上看看 hello.txt 是否更新
#     result = functions.run_command_to_target_host(target_host,command)
#     assert result == enums.EnumForResoultOfExecutedCommand.SUCCESS
