import logging
from langchain.tools import AIPluginTool
from langchain.chat_models import ChatOpenAI
from langchain.agents import load_tools, initialize_agent
from openai.error import InvalidRequestError


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

    def run(self, text, max_retry_count=3):
        retry_count = 0
        for i in range(max_retry_count):
            try:
                return self.agent.run(text)
            except InvalidRequestError as e:
                logging.warning(f"agent run error: {e.error['message']}")
                if retry_count + 1 == max_retry_count:
                    raise e
            except Exception as e:
                logging.warning(f"agent run error: {str(e)}")
                if retry_count + 1 == max_retry_count:
                    raise e
            logging.info("agent run retry.")
            retry_count += 1
