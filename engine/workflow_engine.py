import json


class WorkflowEngine:

    def __init__(self):

        with open("config/workflow_config.json") as f:
            self.workflow_config = json.load(f)

    def process(self, rule_results):

        step = self.workflow_config["workflow"]["start"]

        fail = any(r["result"] == "FAIL" for r in rule_results)

        if fail:
            return self.workflow_config["workflow"]["steps"][step]["on_fail"]

        return self.workflow_config["workflow"]["steps"][step]["on_pass"]