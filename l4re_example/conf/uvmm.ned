package.path = "rom/?.lua";

local L4 = require "L4";
local vmm = require "vmm";

vmm.start_vm({
  id = 1,
  mem = 128,
  mon = false,
  rd = "rom/ramdisk-armv8-64.cpio.gz",
  fdt = "rom/virt-arm_virt-64.dtb",
  bootargs = "console=hvc0 earlyprintk=1 rdinit=/bin/sh",
  kernel = "rom/Image.gz",
  log = L4.Env.log
});