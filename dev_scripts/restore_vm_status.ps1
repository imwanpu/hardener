vmrun -T ws revertToSnapshot "d:\virtual_machine\hd-centos8\hd-centos8.vmx" "start after init"
vmrun -T ws start "d:\virtual_machine\hd-centos8\hd-centos8.vmx"
Start-Sleep -Seconds 3
