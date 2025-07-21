from agio.core.events import callback

@callback('agio.init.done')
def on_core_init(event, payload=None):
    print('CORE INIT DONE!!!!!!!!', event)


@callback('agio.init.package_loaded')
def on_package_load(event, pkg):
    print('PACKAGE LOADED', pkg)


@callback('example.command*')
def on_example_command(event, payload):
    print('Example Event', payload)
