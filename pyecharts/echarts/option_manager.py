from lml.plugin import PluginManager, PluginInfo

import pyecharts.constants as constants


class EchartsOptionHandlerManager(PluginManager):

    def __init__(self):
        super(EchartsOptionHandlerManager, self).__init__(
            constants.ECHARTS_OPTION_PLUGIN_TYPE
        )

    def __iter__(self):
        for handler_plugin_infos in self.registry.values():
            for a_handler_plugin_info in handler_plugin_infos:
                yield (a_handler_plugin_info.option(),
                       a_handler_plugin_info.cls)


class Option(PluginInfo):

    def __init__(self, option_for=None):
        super(Option, self).__init__(constants.ECHARTS_OPTION_PLUGIN_TYPE)
        self.option_for = option_for

    def option(self):
        if self.option_for:
            return self.option_for
        else:
            return self.cls.__name__

    def tags(self):
        """
        tags() return the keys to store this plugin info
        in PluginManager.
        """
        return [self.option()]
