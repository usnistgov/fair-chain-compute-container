#! /bin/sh

# Linux data-gathering commands for container manifest specifications of hardware resources.
#
# ls -al /data/hw-specs/collect_hw_info.sh > /data/hw-outputs/ls_shell_script.txt
# cd /
grep MemTotal /proc/meminfo > /data/hw-outputs/memtotal.txt
lscpu > /data/hw-outputs/cpucores.txt
grep -o 'avx[^ ]*' /proc/cpuinfo > /data/hw-outputs/cpuavx.txt
grep -o 'avx2[^ ]*' /proc/cpuinfo > /data/hw-outputs/cpuavx2.txt
set > /data/hw-outputs/setgpu.txt

