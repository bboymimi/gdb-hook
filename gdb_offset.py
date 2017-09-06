import gdb

class Offsets(gdb.Command):
    def __init__(self):
        super (Offsets, self).__init__ ('offsets-of', gdb.COMMAND_DATA)

    def invoke(self, arg, from_tty):
        argv = gdb.string_to_argv(arg)
        if len(argv) != 1:
            raise gdb.GdbError('offsets-of takes exactly 1 argument.')

        stype = gdb.lookup_type('struct ' + argv[0])

        print ('struct ' + argv[0], '{')
        for field in stype.fields():
            print ('    %s => %d(0x%x)' % (field.name, field.bitpos//8, field.bitpos//8))
        print ('}')

Offsets()
