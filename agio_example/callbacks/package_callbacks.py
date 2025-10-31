from agio.core import workspaces as ws


def on_installed(package_manager: ws.APackageManager, ws_manager: ws.AWorkspaceManager):
    print('On package installed callback', package_manager)


def before_uninstalling(package_manager: ws.APackageManager, ws_manager: ws.AWorkspaceManager):
    print('On before package uninstalled callback', package_manager)


def after_uninstalling(package_manager: ws.APackageManager, ws_manager: ws.AWorkspaceManager):
    print('On after package uninstalled callback', package_manager)


