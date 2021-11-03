# wedding
The great wedding will be taken place here :) 

# Intial configuration:
1. Execute L4Re regular setup steps based on https://github.com/kernkonzept/manifest/wiki
2. Add extra line to /l4re-snapshot-21.07.0/src/l4/conf/modules.list:  
include ../../../../wedding/conf/wedding.list  
3. Extend /l4re-snapshot-21.07.0/src/l4/conf/Makeconf.boot with extra line:  
SOMEDIR = /home/adto/dome   
MODULE_SEARCH_PATH = $(SOMEDIR)/build-fiasco-aarch64:$(SOMEDIR)/ramdisk:$(SOMEDIR)/wedding/conf:$(SOMEDIR)/wedding/pkg:$(SOMEDIR)/build-linux-aarch64/arch/arm64/boot/   
4. Extend /l4re-snapshot-21.07.0/src/l4/conf/Makeconf.boot with extra line for QUMU extension:  
QEMU_OPTIONS-arm64 = -M virt,virtualization=true -cpu cortex-a57 -m 1024 -display none  


# Build & run custom package:
`~/dome/wedding/pkg/net$ make O=../../../build-l4-aarch64`  
`~/dome/build-l4-aarch64$ make E=net qemu`

# Troubleshooting
1. virt-arm_virt-64.dtb had to move to the right  location inside L4 src.   
2. bootargs = "console=hvc0 earlyprintk=1 rdinit=/bin/sh", was fixed for uvmm lua files, to avoid linux kernel panik  
 