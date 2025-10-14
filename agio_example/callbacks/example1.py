from agio.core.events import callback, AEvent


@callback('agio.init.done')
def on_core_init(event: AEvent):
    print('CORE INIT DONE!!!!!!!!', event)


@callback('agio.init.package_loaded')
def on_package_load(event: AEvent):
    print('PACKAGE LOADED', event.payload['package'])


@callback('example.command*')
def on_example_command(event: AEvent):
    print('Example Event', event.payload)
