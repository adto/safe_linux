package.path = "rom/?.lua";

local L4 = require "L4";
local vmm = require "vmm";

vmm.loader.log_fab = L4.default_loader:new_channel();

local function vm(id)
  vmm.start_vm({
    id = id,
    mem = 128,
    rd = "rom/ramdisk-armv8-64.cpio.gz",
    fdt = "rom/virt-arm_virt-64.dtb",
    kernel = "rom/Image.gz",
    bootargs = "console=hvc0 earlyprintk=1 rdinit=/bin/sh",
  });
end

L4.default_loader:start(	
  {
    log = L4.Env.log,
    caps = { cons = vmm.loader.log_fab:svr() }
  }, "rom/cons -a");

vm(1);
vm(2);