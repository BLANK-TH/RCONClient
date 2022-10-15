from PyQt5 import QtWidgets


class PluginBase:
    def __init__(self, name, version, author, description):
        self.name = name
        self.version = version
        self.author = author
        self.description = description
        self.main_window = None

    def on_load(self):
        """Called when the plugin is loaded. This will be called after main_window is set."""
        pass

    def on_command_send(self, command) -> str:
        """Called when a command is sent

        :param command: The command that is sent.
        :return: Any text you want to append to the console.
        """
        pass

    def on_response_received(self, command, response) -> str:
        """Called when a response is received

        :param command: The command that was sent.
        :param response: The response that was received
        :return: Any text you want to append to the console.
        """
        pass

    def on_menu(self):
        """Called when the plugin's menu is opened. By default, just returns the plugin's info."""
        QtWidgets.QMessageBox.information(None, "Plugin Info", "Name: {}\nVersion: {}\nAuthor: {}\nDescription: {}"
                                          .format(self.name, self.version, self.author, self.description))

    def _set_main_window(self, main_window):
        """Sets the main window of the plugin. This is called by the manager, it is not recommended to override this."""
        self.main_window = main_window
