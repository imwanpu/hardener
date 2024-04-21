vmrun -T ws revertToSnapshot "C:\Users\huber\Documents\hardener\vms\hd-centos7\hd-centos7.vmx" "start after init"
vmrun -T ws start "C:\Users\huber\Documents\hardener\vms\hd-centos7\hd-centos7.vmx"
vmrun -T ws revertToSnapshot "C:\Users\huber\Documents\hardener\vms\hd-ubuntu2004\hd-ubuntu2004.vmx" "start after init"
vmrun -T ws start "C:\Users\huber\Documents\hardener\vms\hd-ubuntu2004\hd-ubuntu2004.vmx"
Start-Sleep -Seconds 3

