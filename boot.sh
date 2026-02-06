
cd turdus_m3rula_v1.2_56442188_macosx
./bin/turdusra1n -D
sleep 2;
cd ..
echo [*] Sending LLB.img4 ...
irecovery -f LLB.img4
sleep 2;
echo [*] Booting into pongoOS ...
palera1n -fpV -k Pongo.bin
sleep 3;
echo [*] Booting into iOS 18 ...
printf 'fuse lock\n/send %s\nmodload\n/send %s\nsep payload\nsep sep_flag 0x12\nsep pwn\n/send %s\nmodload\npalera1n_flags 0x1\n/send %s\nramdisk\n/send %s\noverlay\nxargs %s\nbootx\n' \
	"sep_racer" \
	"sep-firmware.im4p" \
	"checkra1n-kpf-pongo" \
	"ramdisk.dmg" \
	"binpack.dmg" \
	'serial=3' | pongoterm