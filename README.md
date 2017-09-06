# GDB utilities

Utilities used for GDB debugging

0\. Enable the .gdbinit to use the specific class
=====================
Firstly, put the script inside the .gdbinit:

```
python
sys.path.insert(0, '/home/ubuntu/os/gdb-hook')
import gdb_offset
end
```
"/home/ubuntu/os/gdb-hook" is where I git clone the gdb-hook repository.

1\. offsets-of
=====================
This is the tool you can use to get the struct member offset of the
specific struct. For example:

```
# To get member offset inside the EventNotifier
(gdb) offsets-of EventNotifier
struct EventNotifier {
    rfd => 0(0x0)
    wfd => 4(0x4)
}

# You can also get the offes by using pahole
$ pahole -C EventNotifier /usr/lib/debug/.build-id/a7/5078d5d59e0c662709153caf6c841dfc75045d.debug
struct EventNotifier {
        int                        rfd;                  /*     0     4 */
        int                        wfd;                  /*     4     4 */

        /* size: 8, cachelines: 1, members: 2 */
        /* last cacheline: 8 bytes */
};
```
