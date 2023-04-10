import os
import yaml
from lang_chain import LangChain
from openai.error import InvalidRequestError

with open('config.yml', 'r') as yml:
    config = yaml.safe_load(yml)

os.environ["OPENAI_API_KEY"] = config["open-ai"]["api-key"]

agent = LangChain()\
    .set_plugins(config["lang-chain"]["api-plugins"])\
    .build_agent(config["lang-chain"]["agent"])


def run(request):
    req_json = request.get_json()
    if "message" in req_json:
        try:
            result = agent.run(req_json["message"])
            response = {
                "result": result
            }
        except InvalidRequestError as e:
            response = {
                "error": {
                    "code": e.error["code"],
                    "message": e.error["message"],
                }
            }
        except Exception as e:
            response = {
                "error": {
                    "code": "internal_server_error",
                    "message": str(e),
                }
            }
        return response
    else:
        response = {
            "error": {
                "code": "required",
                "message": "Missing parameter for message in request body."
            }
        }
    return response
