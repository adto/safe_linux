PKGDIR		?= ../..
L4DIR		?= $(PKGDIR)/../../../l4re-snapshot-21.07.0/src/l4

TARGET		= $(PKGNAME)

# list your .c or .cc files here
SRC_C		= main.c #foo.c #socket.c 
SRC_CC          =

LIBS := -l :foo --warn-unresolved-symbols #-Bdynamic -Bstatic
#PRIVATE_LIBDIR := /home/adto/dome/build-l4-aarch64/lib/arm64_armv8a/l4f

##adto add private include directories here: (it must be fixed later!)
#PRIVATE_INCDIR = $(SRC_DIR)/include $(SRC_DIR)/include/uapi $(SRC_DIR)/include/generated $(SRC_DIR)/include/generated/uapi
##adto add experimantal paramters as well, try to reduce it later on
CFLAGS += -nostdinc
#CFLAGS += -isystem /usr/lib/gcc-cross/aarch64-linux-gnu/7/include 
PRIVATE_INCDIR += /home/adto/dome/linux/arch/arm64/include 
PRIVATE_INCDIR += /home/adto/dome/build-linux-aarch64/arch/arm64/include/generated  
PRIVATE_INCDIR += /home/adto/dome/linux/include 
PRIVATE_INCDIR += /home/adto/dome/build-linux-aarch64/include 
PRIVATE_INCDIR += /home/adto/dome/linux/arch/arm64/include/uapi 
PRIVATE_INCDIR += /home/adto/dome/build-linux-aarch64/arch/arm64/include/generated/uapi 
PRIVATE_INCDIR += /home/adto/dome/linux/include/uapi 
PRIVATE_INCDIR += /home/adto/dome/build-linux-aarch64/include/generated/uapi 
CFLAGS += -include /home/adto/dome/linux/include/linux/kconfig.h  
CFLAGS += -include /home/adto/dome/linux/include/linux/compiler_types.h  
PRIVATE_INCDIR += /home/adto/dome/linux/net 
PRIVATE_INCDIR += net 

##adto add proper compiler options. (it is coming from .socket.0.cmd)
#CFLAGS += -D__KERNEL__ -Wall -Wundef -Wstrict-prototypes -Wno-trigraphs -fno-strict-aliasing -fno-common -fshort-wchar -Werror-implicit-function-declaration -Wno-format-security -std=gnu89 -fno-PIE -DCC_HAVE_ASM_GOTO -mgeneral-regs-only -DCONFIG_AS_LSE=1 -fno-asynchronous-unwind-tables -mabi=lp64 -fno-delete-null-pointer-checks -Wno-frame-address -Wno-format-truncation -Wno-format-overflow -Wno-int-in-bool-context -O2 --param=allow-store-data-races=0 -Wframe-larger-than=2048 -fstack-protector-strong -Wno-unused-but-set-variable -Wno-unused-const-variable -fno-omit-frame-pointer -fno-optimize-sibling-calls -fno-var-tracking-assignments -g -Wdeclaration-after-statement -Wno-pointer-sign -fno-strict-overflow -fno-merge-all-constants -fmerge-constants -fno-stack-check -fconserve-stack -Werror=implicit-int -Werror=strict-prototypes -Werror=date-time -Werror=incompatible-pointer-types -Werror=designated-init 

##adto make few try for unresolved symbols
#LDFLAGS += -symbolic#--warn-once #-unresolved-symbols=ignore-all


#$(info $$CFLAGS are [${CFLAGS}])


include $(L4DIR)/mk/prog.mk
