from langchain.tools import AIPluginTool
from langchain.chat_models import ChatOpenAI
from langchain.agents import load_tools, initialize_agent


class LangChain:

    def __init__(self):
        self.plugins = None
        self.agent = None

    def set_plugins(self, plugins):
        self.plugins = [AIPluginTool.from_plugin_url(plugin) for plugin in plugins]
        return self

    def build_agent(self, agent):
        tools = load_tools(["requests"])
        if self.plugins is not None:
            tools.extend(self.plugins)
        self.agent = initialize_agent(tools, ChatOpenAI(temperature=0), agent=agent, verbose=True)
        return self

    def run(self, text):
        return self.agent.run(text)
