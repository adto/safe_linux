package.path = "rom/?.lua";

local L4 = require "L4";
local vmm = require "vmm";

vmm.loader.log_fab = L4.default_loader:new_channel();

local function vm(id, net, args)
  vmm.start_vm({
    id = id,
    mem = 128,
    rd = "rom/ramdisk-armv8-64.cpio.gz",
    fdt = "rom/virt-arm_virt-64.dtb",
    kernel = "rom/Image.gz",
    net = net,
    bootargs = "console=hvc0 earlyprintk=1 rdinit=/bin/sh" .. (args or ""),
  });
end

L4.default_loader:start(
  {
    log = L4.Env.log,
    caps = { cons = vmm.loader.log_fab:svr() }
  }, "rom/cons -a");

local net_ports = {
  net0 = 1,
  net1 = 1,
}

vmm.start_virtio_switch(net_ports);

vm(1, net_ports.net0);
vm(2, net_ports.net1);
---vm(1, net_ports.net0, "ip=192.168.1.1:::255.255.255.0:server:eth0");
---vm(2, net_ports.net1, "ip=192.168.1.2:::255.255.255.0:server:eth0");

