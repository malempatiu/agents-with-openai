This project implements an automated Sales Development Representative (SDR) system. It leverages multiple AI agents to generate, evaluate, and send personalized cold sales emails. The system orchestrates various agents and tools to streamline the outbound sales process, from drafting compelling messages to handling email delivery.

## Sales Project Architecture Flowchart

```mermaid
graph TD
    A[main.py] --> B{Sales Manager Agent};
    B --> C1[Professional Sales Agent Tool];
    B --> C2[Engaging Sales Agent Tool];
    B --> C3[Busy Sales Agent Tool];
    C1 --> D{Select Best Email};
    C2 --> D;
    C3 --> D;
    D --> E{Email Manager Agent};
    E --> F[Email Subject Writer Tool];
    F --> G[HTML Email Body Converter Tool];
    G --> H[Send HTML Email Tool];
    H --> I[Email Sent];
```
