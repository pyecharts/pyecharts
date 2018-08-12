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
                yield a_handler_plugin_info.cls


class Option(PluginInfo):

    def __init__(self):
        super(Option, self).__init__(constants.ECHARTS_OPTION_PLUGIN_TYPE)

    def tags(self):
        yield self.cls.__name__
