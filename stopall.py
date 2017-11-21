import psutil

PROCNAME = "python.exe"

print("Killing")

for proc in psutil.process_iter():
	# check whether the process name matches
	print(proc)
	if (proc.name() == PROCNAME):
		proc.kill()