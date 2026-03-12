import datetime


class AuditManager:

    def log_event(self, request_id, event, details):

        log = {
            "request_id": request_id,
            "event": event,
            "details": details,
            "timestamp": str(datetime.datetime.now())
        }

        print("AUDIT LOG:", log)