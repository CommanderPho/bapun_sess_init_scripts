## Greatlakes


#### Speedtest current directory:
```bash
dd if=/dev/zero of=./speedtest.tmp bs=1M count=1024 conv=fdatasync status=progress && rm ./speedtest.tmp

```

`/scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel`
548405248 bytes (548 MB, 523 MiB) copied, 1 s, 548 MB/s
1024+0 records in
1024+0 records out
1073741824 bytes (1.1 GB, 1.0 GiB) copied, 1.69257 s, 634 MB/s


`/dev/shm/halechr/Day5TwoNovel`
[halechr@gl0006 Day5TwoNovel]$ dd if=/dev/zero of=./speedtest.tmp bs=1M count=1024 conv=fdatasync status=progress && rm ./speedtest.tmp
1024+0 records in
1024+0 records out
1073741824 bytes (1.1 GB, 1.0 GiB) copied, 0.321801 s, 3.3 GB/s


`/nfs/turbo/umms-kdiba/Bapun/RatS/Day4Openfield/SORTING/folder_KS4_v1_sorting_analyzer/sorting`
[halechr@gl0006 sorting]$ dd if=/dev/zero of=./speedtest.tmp bs=1M count=1024 conv=fdatasync status=progress && rm ./speedtest.tmp
1024+0 records in
1024+0 records out
1073741824 bytes (1.1 GB, 1.0 GiB) copied, 2.4302 s, 442 MB/s
[halechr@gl0006 sorting]$ pwd



`/tmpssd/halechr`
[halechr@gl0006 halechr]$ dd if=/dev/zero of=./speedtest.tmp bs=1M count=1024 conv=fdatasync status=progress && rm ./speedtest.tmp
1073741824 bytes (1.1 GB, 1.0 GiB) copied, 0.704594 s, 1.5 GB/s



# Day4

rsync -a -W --no-compress --info=progress2 --exclude='*_BAK*' --exclude='*bak' /nfs/turbo/umms-kdiba/Bapun/RatS/Day4OpenTwoNovel/spykcirc /tmpssd/halechr/Day5TwoNovel


[text](../../../Data/Bapun/RatS/Day4Openfield/SORTING/folder_KS4_v1_sorting_analyzer)