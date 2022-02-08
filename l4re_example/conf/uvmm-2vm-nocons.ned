package.path = "rom/?.lua";

local L4 = require "L4";
local vmm = require "vmm";

local function vm(id)
  vmm.start_vm({
    id = id,
    mem = 128,
    rd = "rom/ramdisk-armv8-64.cpio.gz",
    fdt = "rom/virt-arm_virt-64.dtb",
    kernel = "rom/Image.gz",
    bootargs = "console=hvc0 earlyprintk=1 rdinit=/bin/sh",
    log = L4.Env.log
  });
end

vm(1);
vm(2);