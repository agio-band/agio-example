import logging
import time

from agio.core.plugins.base_service import ThreadServicePlugin, make_action

logger = logging.getLogger(__name__)


class ExampleThreadService(ThreadServicePlugin):
    name = "example_thread"

    def execute(self, **kwargs):
        while not self.is_stopped():
            time.sleep(1)

    @make_action()
    def example_action1(self, **kwargs):
        """Invisible in menu"""
        return {"example": "example1"}

    @make_action(
        menu_name=('tray.main_menu', 'example_menu'),
        app_name=('desk', 'front'),
        label='Example Action 2',
        args=['a1', 'a2', 'a3'],
        kwargs={'k1': 'v1'}
    )
    def example_action2(self, *args, **kwargs):
        logger.debug("Example Action 2 Called")
        print(f'\nEXAMPLE CALLED ARGS: {args} {kwargs}\n')
        return {"example": "example2"}

    @make_action(
        menu_name=('maya.main_menu', 'example_menu'),
        app_name=('maya', 'desk', 'front'),
        label='Example Action 3',
    )
    def example_action3(self, **kwargs):
        logger.debug("Example Action 3 Called")
        return {"example": "example3"}

    # ordered
    @make_action(
        menu_name=('example_menu',),
        app_name=('desk', 'front'),
        label='Example Action 4',
        order=10, group='grp1'
    )
    def example_action4(self, **kwargs):
        return {"example": "example4"}

    @make_action(
        menu_name=('example_menu',),
        app_name=('desk', 'front'),
        label='Example Action 5',
        order=9, group='grp1'
    )
    def example_action5(self, **kwargs):
        return {"example": "example5"}

    @make_action(
        menu_name=('example_menu',),
        app_name=('desk', 'front'),
        label='Example Action 6',
        order=9, group='grp2'
    )
    def example_action6(self, **kwargs):
        return {"example": "example6"}

    @make_action(
        menu_name=('example_menu',),
        app_name=('desk', 'front'),
        label='Example Action 7',
        order=10, group='grp2'
    )
    def example_action7(self, **kwargs):
        return {"example": "example7"}

