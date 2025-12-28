```mermaid
flowchart TB
    A[Start]
    B[Runner.run (get_sales_manager_agent)]

    A --> B

    C[Invoke sales agent tools]

    D[Sales Agent 1 - Professional]
    E[Sales Agent 2 - Engaging]
    F[Sales Agent 3 - Busy]

    G[Generate 3 drafts]
    H[Select best draft]

    B --> C
    C --> D
    C --> E
    C --> F

    D --> G
    E --> G
    F --> G

    G --> H

    I[Handoff to Email Manager]
    H --> I

    J[Invoke email tools]
    I --> J

    K[Subject Writer]
    L[HTML Converter]

    J --> K
    J --> L

    M[Format email]
    K --> M
    L --> M

    N[Send HTML Email]
    M --> N

    O[Email Sent]
    N --> O
