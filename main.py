import json
import subprocess
#import logging
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction


#logger = logging.getLogger(__name__)

class RunTerminalCommands(Extension):

    def __init__(self):
        super(RunTerminalCommands, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        command = event.get_argument()
        return RenderResultListAction([ExtensionResultItem(icon='icon.png',
                                                                  name='Run',
                                                                  description='The command you type will be runned',
                                                                  on_enter=ExtensionCustomAction(data=command))])


class ItemEnterEventListener(EventListener):

    def on_event(self, event, extension):
        command = event.get_data()
        #logger.info(command)
        subprocess.run(command,shell=True)
        return HideWindowAction()


if __name__ == '__main__':
    RunTerminalCommands().run()