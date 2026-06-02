halechr@RDLU0039:~$ mount_turbo 
(halechr@greatlakes.arc-ts.umich.edu) Password: 
(halechr@greatlakes.arc-ts.umich.edu) Duo two-factor login for halechr

Enter a passcode or select one of the following options:

1. Duo Push to XXX-XXX-6612
2. Duo Push to Samsung Tab 2020 (Android)
3. Duo Push to iPad 2023 (iOS)
4. Duo Push to Old White iPad (iOS)
5. Duo Push to iPad Mini (White, Pink Case) (iOS)
6. Duo Push to 2020 Black iPad (iOS)
7. Duo Push to iPad Mini (K) (iOS)
8. Duo Push to XXX-XXX-7688
9. Phone call to XXX-XXX-6612
10. Phone call to XXX-XXX-7688
11. SMS passcodes to XXX-XXX-6612
12. SMS passcodes to XXX-XXX-7688

Passcode or option (1-12): 1
turbo mounted at /home/halechr/cloud/turbo
halechr@RDLU0039:~$ mount_
mount_all_cloud_drives   mount_cloud_drive        mount_greatlakes         mount_locker_dataDen     mount_sshfs_cloud_drive  mount_symlinked_drive    mount_turbo              
halechr@RDLU0039:~$ mount_all_cloud_drives 
Error: unknown flag: --network-mode
Usage:
  rclone mount remote:path /path/to/mountpoint [flags]

Flags:
      --allow-non-empty                        Allow mounting over a non-empty directory (not Windows).
      --allow-other                            Allow access to other users.
      --allow-root                             Allow access to root user.
      --async-read                             Use asynchronous reads. (default true)
      --attr-timeout duration                  Time for which file/directory attributes are cached. (default 1s)
      --daemon                                 Run mount as a daemon (background mode).
      --daemon-timeout duration                Time limit for rclone to respond to kernel (not supported by all OSes).
      --debug-fuse                             Debug the FUSE internals - needs -v.
      --default-permissions                    Makes kernel enforce access control based on the file mode.
      --dir-cache-time duration                Time to cache directory entries for. (default 5m0s)
      --dir-perms FileMode                     Directory permissions (default 0777)
      --file-perms FileMode                    File permissions (default 0666)
      --fuse-flag stringArray                  Flags or arguments to be passed direct to libfuse/WinFsp. Repeat if required.
      --gid uint32                             Override the gid field set by the filesystem. (default 65500)
  -h, --help                                   help for mount
      --max-read-ahead SizeSuffix              The number of bytes that can be prefetched for sequential reads. (default 128k)
      --no-checksum                            Don't compare checksums on up/download.
      --no-modtime                             Don't read/write the modification time (can speed things up).
      --no-seek                                Don't allow seeking in files.
  -o, --option stringArray                     Option for libfuse/WinFsp. Repeat if required.
      --poll-interval duration                 Time to wait between polling for changes. Must be smaller than dir-cache-time. Only on supported remotes. Set to 0 to disable. (default 1m0s)
      --read-only                              Mount read-only.
      --uid uint32                             Override the uid field set by the filesystem. (default 114191263)
      --umask int                              Override the permission bits set by the filesystem.
      --vfs-cache-max-age duration             Max age of objects in the cache. (default 1h0m0s)
      --vfs-cache-max-size SizeSuffix          Max total size of objects in the cache. (default off)
      --vfs-cache-mode CacheMode               Cache mode off|minimal|writes|full (default off)
      --vfs-cache-poll-interval duration       Interval to poll the cache for stale objects. (default 1m0s)
      --vfs-case-insensitive                   If a file name not found, find a case insensitive match.
      --vfs-read-ahead SizeSuffix              Extra read ahead over --buffer-size when using cache-mode full.
      --vfs-read-chunk-size SizeSuffix         Read the source objects in chunks. (default 128M)
      --vfs-read-chunk-size-limit SizeSuffix   If greater than --vfs-read-chunk-size, double the chunk size after each chunk read, until the limit is reached. 'off' is unlimited. (default off)
      --vfs-read-wait duration                 Time to wait for in-sequence read before seeking. (default 20ms)
      --vfs-write-back duration                Time to writeback files after last use when using cache. (default 5s)
      --vfs-write-wait duration                Time to wait for in-sequence write before giving error. (default 1s)
      --volname string                         Set the volume name (not supported by all OSes).
      --write-back-cache                       Makes kernel buffer writes before sending them to rclone. Without this, writethrough caching is used.

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.

2026/06/02 11:20:04 Fatal error: unknown flag: --network-mode
Error: unknown flag: --network-mode
Usage:
  rclone mount remote:path /path/to/mountpoint [flags]

Flags:
      --allow-non-empty                        Allow mounting over a non-empty directory (not Windows).
      --allow-other                            Allow access to other users.
      --allow-root                             Allow access to root user.
      --async-read                             Use asynchronous reads. (default true)
      --attr-timeout duration                  Time for which file/directory attributes are cached. (default 1s)
      --daemon                                 Run mount as a daemon (background mode).
      --daemon-timeout duration                Time limit for rclone to respond to kernel (not supported by all OSes).
      --debug-fuse                             Debug the FUSE internals - needs -v.
      --default-permissions                    Makes kernel enforce access control based on the file mode.
      --dir-cache-time duration                Time to cache directory entries for. (default 5m0s)
      --dir-perms FileMode                     Directory permissions (default 0777)
      --file-perms FileMode                    File permissions (default 0666)
      --fuse-flag stringArray                  Flags or arguments to be passed direct to libfuse/WinFsp. Repeat if required.
      --gid uint32                             Override the gid field set by the filesystem. (default 65500)
  -h, --help                                   help for mount
      --max-read-ahead SizeSuffix              The number of bytes that can be prefetched for sequential reads. (default 128k)
      --no-checksum                            Don't compare checksums on up/download.
      --no-modtime                             Don't read/write the modification time (can speed things up).
      --no-seek                                Don't allow seeking in files.
  -o, --option stringArray                     Option for libfuse/WinFsp. Repeat if required.
      --poll-interval duration                 Time to wait between polling for changes. Must be smaller than dir-cache-time. Only on supported remotes. Set to 0 to disable. (default 1m0s)
      --read-only                              Mount read-only.
      --uid uint32                             Override the uid field set by the filesystem. (default 114191263)
      --umask int                              Override the permission bits set by the filesystem.
      --vfs-cache-max-age duration             Max age of objects in the cache. (default 1h0m0s)
      --vfs-cache-max-size SizeSuffix          Max total size of objects in the cache. (default off)
      --vfs-cache-mode CacheMode               Cache mode off|minimal|writes|full (default off)
      --vfs-cache-poll-interval duration       Interval to poll the cache for stale objects. (default 1m0s)
      --vfs-case-insensitive                   If a file name not found, find a case insensitive match.
      --vfs-read-ahead SizeSuffix              Extra read ahead over --buffer-size when using cache-mode full.
      --vfs-read-chunk-size SizeSuffix         Read the source objects in chunks. (default 128M)
      --vfs-read-chunk-size-limit SizeSuffix   If greater than --vfs-read-chunk-size, double the chunk size after each chunk read, until the limit is reached. 'off' is unlimited. (default off)
      --vfs-read-wait duration                 Time to wait for in-sequence read before seeking. (default 20ms)
      --vfs-write-back duration                Time to writeback files after last use when using cache. (default 5s)
      --vfs-write-wait duration                Time to wait for in-sequence write before giving error. (default 1s)
      --volname string                         Set the volume name (not supported by all OSes).
      --write-back-cache                       Makes kernel buffer writes before sending them to rclone. Without this, writethrough caching is used.

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.

2026/06/02 11:20:04 Fatal error: unknown flag: --network-mode
Error: unknown flag: --network-mode
Usage:
  rclone mount remote:path /path/to/mountpoint [flags]

Flags:
      --allow-non-empty                        Allow mounting over a non-empty directory (not Windows).
      --allow-other                            Allow access to other users.
      --allow-root                             Allow access to root user.
      --async-read                             Use asynchronous reads. (default true)
      --attr-timeout duration                  Time for which file/directory attributes are cached. (default 1s)
      --daemon                                 Run mount as a daemon (background mode).
      --daemon-timeout duration                Time limit for rclone to respond to kernel (not supported by all OSes).
      --debug-fuse                             Debug the FUSE internals - needs -v.
      --default-permissions                    Makes kernel enforce access control based on the file mode.
      --dir-cache-time duration                Time to cache directory entries for. (default 5m0s)
      --dir-perms FileMode                     Directory permissions (default 0777)
      --file-perms FileMode                    File permissions (default 0666)
      --fuse-flag stringArray                  Flags or arguments to be passed direct to libfuse/WinFsp. Repeat if required.
      --gid uint32                             Override the gid field set by the filesystem. (default 65500)
  -h, --help                                   help for mount
      --max-read-ahead SizeSuffix              The number of bytes that can be prefetched for sequential reads. (default 128k)
      --no-checksum                            Don't compare checksums on up/download.
      --no-modtime                             Don't read/write the modification time (can speed things up).
      --no-seek                                Don't allow seeking in files.
  -o, --option stringArray                     Option for libfuse/WinFsp. Repeat if required.
      --poll-interval duration                 Time to wait between polling for changes. Must be smaller than dir-cache-time. Only on supported remotes. Set to 0 to disable. (default 1m0s)
      --read-only                              Mount read-only.
      --uid uint32                             Override the uid field set by the filesystem. (default 114191263)
      --umask int                              Override the permission bits set by the filesystem.
      --vfs-cache-max-age duration             Max age of objects in the cache. (default 1h0m0s)
      --vfs-cache-max-size SizeSuffix          Max total size of objects in the cache. (default off)
      --vfs-cache-mode CacheMode               Cache mode off|minimal|writes|full (default off)
      --vfs-cache-poll-interval duration       Interval to poll the cache for stale objects. (default 1m0s)
      --vfs-case-insensitive                   If a file name not found, find a case insensitive match.
      --vfs-read-ahead SizeSuffix              Extra read ahead over --buffer-size when using cache-mode full.
      --vfs-read-chunk-size SizeSuffix         Read the source objects in chunks. (default 128M)
      --vfs-read-chunk-size-limit SizeSuffix   If greater than --vfs-read-chunk-size, double the chunk size after each chunk read, until the limit is reached. 'off' is unlimited. (default off)
      --vfs-read-wait duration                 Time to wait for in-sequence read before seeking. (default 20ms)
      --vfs-write-back duration                Time to writeback files after last use when using cache. (default 5s)
      --vfs-write-wait duration                Time to wait for in-sequence write before giving error. (default 1s)
      --volname string                         Set the volume name (not supported by all OSes).
      --write-back-cache                       Makes kernel buffer writes before sending them to rclone. Without this, writethrough caching is used.

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.

2026/06/02 11:20:04 Fatal error: unknown flag: --network-mode
Error: unknown flag: --network-mode
Usage:
  rclone mount remote:path /path/to/mountpoint [flags]

Flags:
      --allow-non-empty                        Allow mounting over a non-empty directory (not Windows).
      --allow-other                            Allow access to other users.
      --allow-root                             Allow access to root user.
      --async-read                             Use asynchronous reads. (default true)
      --attr-timeout duration                  Time for which file/directory attributes are cached. (default 1s)
      --daemon                                 Run mount as a daemon (background mode).
      --daemon-timeout duration                Time limit for rclone to respond to kernel (not supported by all OSes).
      --debug-fuse                             Debug the FUSE internals - needs -v.
      --default-permissions                    Makes kernel enforce access control based on the file mode.
      --dir-cache-time duration                Time to cache directory entries for. (default 5m0s)
      --dir-perms FileMode                     Directory permissions (default 0777)
      --file-perms FileMode                    File permissions (default 0666)
      --fuse-flag stringArray                  Flags or arguments to be passed direct to libfuse/WinFsp. Repeat if required.
      --gid uint32                             Override the gid field set by the filesystem. (default 65500)
  -h, --help                                   help for mount
      --max-read-ahead SizeSuffix              The number of bytes that can be prefetched for sequential reads. (default 128k)
      --no-checksum                            Don't compare checksums on up/download.
      --no-modtime                             Don't read/write the modification time (can speed things up).
      --no-seek                                Don't allow seeking in files.
  -o, --option stringArray                     Option for libfuse/WinFsp. Repeat if required.
      --poll-interval duration                 Time to wait between polling for changes. Must be smaller than dir-cache-time. Only on supported remotes. Set to 0 to disable. (default 1m0s)
      --read-only                              Mount read-only.
      --uid uint32                             Override the uid field set by the filesystem. (default 114191263)
      --umask int                              Override the permission bits set by the filesystem.
      --vfs-cache-max-age duration             Max age of objects in the cache. (default 1h0m0s)
      --vfs-cache-max-size SizeSuffix          Max total size of objects in the cache. (default off)
      --vfs-cache-mode CacheMode               Cache mode off|minimal|writes|full (default off)
      --vfs-cache-poll-interval duration       Interval to poll the cache for stale objects. (default 1m0s)
      --vfs-case-insensitive                   If a file name not found, find a case insensitive match.
      --vfs-read-ahead SizeSuffix              Extra read ahead over --buffer-size when using cache-mode full.
      --vfs-read-chunk-size SizeSuffix         Read the source objects in chunks. (default 128M)
      --vfs-read-chunk-size-limit SizeSuffix   If greater than --vfs-read-chunk-size, double the chunk size after each chunk read, until the limit is reached. 'off' is unlimited. (default off)
      --vfs-read-wait duration                 Time to wait for in-sequence read before seeking. (default 20ms)
      --vfs-write-back duration                Time to writeback files after last use when using cache. (default 5s)
      --vfs-write-wait duration                Time to wait for in-sequence write before giving error. (default 1s)
      --volname string                         Set the volume name (not supported by all OSes).
      --write-back-cache                       Makes kernel buffer writes before sending them to rclone. Without this, writethrough caching is used.

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.

2026/06/02 11:20:04 Fatal error: unknown flag: --network-mode
halechr@RDLU0039:~$ mount_
mount_all_cloud_drives   mount_cloud_drive        mount_greatlakes         mount_locker_dataDen     mount_sshfs_cloud_drive  mount_symlinked_drive    mount_turbo              
halechr@RDLU0039:~$ mount_locker_dataDen 
(halechr@greatlakes-oncampus.arc-ts.umich.edu) Password: 
(halechr@greatlakes-oncampus.arc-ts.umich.edu) Duo two-factor login for halechr

Enter a passcode or select one of the following options:

1. Duo Push to XXX-XXX-6612
2. Duo Push to Samsung Tab 2020 (Android)
3. Duo Push to iPad 2023 (iOS)
4. Duo Push to Old White iPad (iOS)
5. Duo Push to iPad Mini (White, Pink Case) (iOS)
6. Duo Push to 2020 Black iPad (iOS)
7. Duo Push to iPad Mini (K) (iOS)
8. Duo Push to XXX-XXX-7688
9. Phone call to XXX-XXX-6612
10. Phone call to XXX-XXX-7688
11. SMS passcodes to XXX-XXX-6612
12. SMS passcodes to XXX-XXX-7688

Passcode or option (1-12): 1
locker_dataDen mounted at /home/halechr/cloud/locker_dataDen via ssh through greatlakes
halechr@RDLU0039:~$ cd ~/FastData/Bapun/RatS/Day1Openfield/spyk-circ/RatS-Day1Openfield/RatS-Day1Openfield-merged.GUI
halechr@RDLU0039:~/FastData/Bapun/RatS/Day1Openfield/spyk-circ/RatS-Day1Openfield/RatS-Day1Openfield-merged.GUI$ mamba activate phy2
(phy2) halechr@RDLU0039:~/FastData/Bapun/RatS/Day1Openfield/spyk-circ/RatS-Day1Openfield/RatS-Day1Openfield-merged.GUI$ phy template-gui params.py 
12:14:37.067 [W] model:668            Skipping spike waveforms that do not exist, they will be extracted on the fly from the raw data as needed.
12:14:37.068 [W] traces:161           Inconsistent number of channels between the params file and the binary dat file
12:17:13.790 [I] supervisor:711       Change metadata_group for clusters 63 to noise.
12:17:27.998 [I] supervisor:711       Change metadata_group for clusters 119 to good.
12:17:42.686 [I] supervisor:711       Change metadata_group for clusters 102 to noise.
12:18:00.749 [I] supervisor:711       Change metadata_group for clusters 67 to good.
12:18:15.789 [I] supervisor:711       Change metadata_group for clusters 117 to good.
12:18:37.310 [I] supervisor:711       Change metadata_group for clusters 78 to good.
12:19:14.548 [I] supervisor:711       Change metadata_q for clusters 78 to 8.
12:29:11.103 [W] actions:213          Error when executing action MahalanobisDist.
^[x12:29:37.454 [W] actions:213          Error when executing action MahalanobisDist.
Selected channels =  71 72
12:30:14.863 [I] supervisor:702       Assigned 736 spikes.
12:30:33.000 [I] supervisor:698       Undo cluster assign.
12:31:08.688 [W] recluster:231        Running K-means clustering
12:31:08.755 [I] supervisor:702       Assigned 736 spikes.
12:31:08.762 [W] recluster:244        K means clustering complete
12:31:16.083 [I] supervisor:698       Undo cluster assign.
(phy2) halechr@RDLU0039:~/FastData/Bapun/RatS/Day1Openfield/spyk-circ/RatS-Day1Openfield/RatS-Day1Openfield-merged.GUI$ phy template-gui params.py 
12:41:44.081 [W] model:668            Skipping spike waveforms that do not exist, they will be extracted on the fly from the raw data as needed.
12:41:44.082 [W] traces:161           Inconsistent number of channels between the params file and the binary dat file
12:41:44.672 [E] plugin:113           No module named 'umap'
Traceback (most recent call last):
  File "/home/halechr/miniforge3/envs/phy2/lib/python3.11/site-packages/phy/utils/plugin.py", line 111, in discover_plugins
    spec.loader.exec_module(mod)
  File "<frozen importlib._bootstrap_external>", line 940, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/halechr/.phy/plugins/recluster_v2.py", line 9, in <module>
    import umap
ModuleNotFoundError: No module named 'umap'
12:41:52.823 [W] plugin:152           The plugin ReclusterUMAP couldn't be found.
(phy2) halechr@RDLU0039:~/FastData/Bapun/RatS/Day1Openfield/spyk-circ/RatS-Day1Openfield/RatS-Day1Openfield-merged.GUI$ 
