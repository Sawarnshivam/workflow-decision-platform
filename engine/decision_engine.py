from engine.rule_engine import RuleEngine
from engine.workflow_engine import WorkflowEngine
from engine.state_manager import StateManager
from engine.audit_manager import AuditManager


class DecisionEngine:

    def __init__(self):

        self.rule_engine = RuleEngine()
        self.workflow_engine = WorkflowEngine()
        self.state_manager = StateManager()
        self.audit_manager = AuditManager()

    def process_request(self, request_id, data):

        # Log request received
        self.audit_manager.log_event(request_id, "REQUEST_RECEIVED", data)

        # Evaluate rules
        rule_results = self.rule_engine.evaluate_rules(data)

        self.audit_manager.log_event(request_id, "RULES_EVALUATED", rule_results)

        # Process workflow
        decision = self.workflow_engine.process(rule_results)

        # Update state
        self.state_manager.update_state(request_id, decision)

        self.audit_manager.log_event(request_id, "FINAL_DECISION", decision)

        return {
            "request_id": request_id,
            "decision": decision,
            "rules": rule_results
        }