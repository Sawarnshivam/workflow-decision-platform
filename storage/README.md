# Storage Layer

The **storage** folder represents the persistence layer of the system.

In a production system, this layer would be responsible for storing and retrieving application data such as:

- Request states
- Workflow execution history
- Rule evaluation results
- Audit logs
- External service responses (cache)

## Current Implementation

For the purpose of this assignment, the system uses **in-memory storage** through the `StateManager` component located in:

```
engine/state_manager.py
```

Therefore, no physical database or file-based storage is implemented in this layer.

## Future Extensions

This folder can be extended to support real persistence solutions such as:

- SQL / NoSQL databases
- Redis or in-memory caching systems
- File-based storage
- Cloud storage services

The architecture keeps this layer separate to ensure the system remains **modular, scalable, and easy to extend**.