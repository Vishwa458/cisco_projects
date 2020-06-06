import getpass
import telnetlib
import paramiko
import os
import sys
from ftplib import FTP
from scp import SCPClient


def telnet(host,username,password):
    with telnetlib.Telnet(host) as tn:    #Using with keyword as context manager to release the resource once done
        tn.write(username.encode('ascii') + b"\n")
        tn.write(password.encode('ascii') + b"\n")
        tn.write(b"ls\n")
        tn.write(b"exit\n")
        print(tn.read_all().decode('ascii'))

def ssh(host, port, username, password):     #Secure shell  and checking disk space in remote server
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host=host, port=port, username=username, password=password)

def inode():
    # Directory to be scanned
    path = os.getcwd()
    # Using os.scandir() method
    # scan the specified directory
    # and yield os.DirEntry object
    # for each file and sub-directory
    print("Directory entry name and their inode number")
    with os.scandir(path) as itr:       #Using with keyword as context manager to release the resource once done
        for entry in itr:
            # Exclude the entry name
            # starting with '.'
            if not entry.name.startswith('.'):
                # print entry name
                # and entry's inode() number
                print(entry.name, " :", entry.inode())


def ls(path):                           #LS(FileList)
    dirlist = os.listdir(path)
    pprint(dirlist)
def df(path):                               #DF(Diskspace) Commands
    diskspace=os.system(df(path))
    pprint(diskspace)

def copyfiles():
            with paramiko.SSHClient() as ssh:   #Using with keyword as context manager to release the resource once done
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(host=host, port=port, username=username, password=password)
                with ssh.open_sftp() as sftp:     #Implementing SFTP using python module paramiko.SSHClient
                    localpath = '/home/e100075/python/'
                    remotepath = '/home/developers/screenshots/'
                    sftp.put(localpath, remotepath)
            def enter_dir(f, path):
                original_dir = f.pwd()
                try:
                    f.cwd(path)
                except:
                    return
                print(path)
                names = f.nlst()
                for name in names:
                    enter_dir(f, path + '/' + name)
                f.cwd(original_dir)
            with FTP(host) as f:     #Implementing FTP using python module paramiko.SSHClient
                f.login()
                enter_dir(f, '/pub/linux/kernel/Historic/old-versions')
            with SCPClient(ssh.get_transport()) as scp:  #Implementing SCP using python module paramiko.SSHClient
                scp.put('test.txt', 'test2.txt')
                scp.get('test2.txt')

print("Enter below details to perform all the operations: ")
host=input("Enter remote server IP Address: ")
username=input("Enter remote server username: ")
password=input("Enter host remote server password: ")
port=int(input("Enter host remote server password: "))
path=print("PLease enter the path to get the list of files from the specified path:")

telnet(host,password)                #fucntion for telnet Command
ssh(host,username,password)          #fucntion for SSH(SecureShell)
inode(host,username,password)        #fucntion for inode Command
copyfiles(host,port,username,password)    #fucntion for FTP,SFTP,SCP Commands

ls(path)
df(path)
