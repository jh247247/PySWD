import logging


def load(optparser, options):
    if not options.adapter:
        optparser.error("--adapter must be specified")
    if options.debug:
        logging.basicConfig(level=logging.DEBUG)
    mod_name = options.adapter
    if mod_name.endswith(".py"):
        mod_name = mod_name[:-len(".py")]
    mod = __import__(mod_name)
    cls = mod.Adapter
    adapter = cls(options)
    return adapter


def add_options(optparser):
    optparser.add_option('', '--debug', action="store_true",
            help='Debug logging')
    optparser.add_option('-a', '--adapter',
            help='Use specified JTAG adapter plugin')
    optparser.add_option('-p', '--port',
            help='Port/device adapter uses')
