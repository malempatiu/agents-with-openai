flowchart TD
    %% --- Sales Agents ---
    SA1[Sales Agent 1]
    SA2[Sales Agent 2]
    SA3[Sales Agent 3]

    SA1T[Sales Agent 1 Tool]
    SA2T[Sales Agent 2 Tool]
    SA3T[Sales Agent 3 Tool]

    SA1 -->|as_tool| SA1T
    SA2 -->|as_tool| SA2T
    SA3 -->|as_tool| SA3T

    %% --- Sales Manager ---
    SM[Sales Manager Agent<br/>• name<br/>• instructions<br/>• tools<br/>• model<br/>• handoff]

    SA1T -->|tool| SM
    SA2T -->|tool| SM
    SA3T -->|tool| SM

    %% --- LLM Interaction ---
    User[(User)]
    LLM[LLM<br/>gpt-4o-mini]

    User -->|message| SM
    SM -->|response| User

    SM -->|request| LLM
    LLM -->|response| SM

    %% --- Handoff to Email Manager ---
    SM -->|handoff| EM[Email Manager Agent]

    %% --- Email Composition Agents ---
    SubjectAgent[Subject Agent]
    BodyAgent[HTML Body Agent]

    SubjectTool[Subject Tool]
    BodyTool[HTML Body Tool]

    SubjectAgent -->|as_tool| SubjectTool
    BodyAgent -->|as_tool| BodyTool

    SubjectTool --> EM
    BodyTool --> EM

    %% --- Send Email ---
    SendEmailTool[Send HTML Email Tool]
    EM --> SendEmailTool
