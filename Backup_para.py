import paramiko
import datetime

user = 'admin'
secret = 'admin'
port = 22

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

time_now = datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_%S')
infilepath = "F:\\Automation\\cisco automation\\"
outfilepath = "F:\\Automation\\cisco automation\\"
devicelist = "device-list1.txt"

input_file = open(infilepath + devicelist, "r")
iplist = input_file.readlines()
input_file.close()

for ip in iplist:
    ipaddr = ip.strip()
    ssh.connect(hostname=ipaddr, username=user, password=secret, port=port)
    stdin, stdout, stderr = ssh.exec_command('show run')
    config_list = stdout.readlines()

    outfile = open(outfilepath + ipaddr + "_" + time_now, "w")
    for line in config_list:
        outfile.write(line)

    ssh.close()
    outfile.close()
