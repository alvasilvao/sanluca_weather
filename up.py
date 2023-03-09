import subprocess

subprocess.run(["cd","~"])
subprocess.run(["git","add","."])
subprocess.run(["git","commit","-m","'msg'"])
subprocess.run(["git","branch","-M","main"])
subprocess.run(["git","push","-u","origin","main"])
