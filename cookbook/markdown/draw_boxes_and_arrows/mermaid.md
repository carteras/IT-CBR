# Mermaid.js

```mermaid
  graph TD;
      Ada-->Bob;
      Ada-->Charlie;
      Bob-->Della;
      Charlie-->Della;
```

```mermaid
    flowchart LR;
        A[Hard] -->|Text| B(Round);
        B --> C{Decision};
        C -->|One| D[Result 1];
        C -->|Two| E[Result 2];
        D --> F[Awesome];
        E --> F[Awesome];
```

```mermaid
    flowchart TD;
        A[Hard] -->|Text| B(Round);
        B --> C{Decision};
        C -->|One| D[Result 1];
        C -->|Two| E[Result 2];
        D --> F[Awesome];
        E --> F[Awesome];
```

```mermaid
    sequenceDiagram LR;
        Alice->>+John: Hello John, how are you?;
        Alice->>+John: John, can you hear me?;
        John-->>-Alice: Hi Alice, I can hear you!;
        John-->>-Alice: I feel great!;
```

```mermaid
    classDiagram TD;
        Class01 <|-- AveryLongClass : Cool
        Class03 *-- Class04
        Class05 o-- Class06
        Class07 .. Class08
        Class09 --> C2 : Where am i?
        Class09 --* C3
        Class09 --|> Class07
        Class07 : equals()
        Class07 : Object[] elementData
        Class01 : size()
        Class01 : int chimp
        Class01 : int gorilla
        Class08 <--> C2: Cool label
```

```mermaid
    gantt
        title A Gantt Diagram
        dateFormat  YYYY-MM-DD
        section Section
        A task           :a1, 2014-01-01, 30d
        Another task     :after a1  , 20d
        section Another
        Task in sec      :2014-01-12  , 12d
        another task      : 24d
```