
CREATE TABLE IF NOT EXISTS raw_logs(
    id INT AUTO_INCREMENT PRIMARY KEY,
    EventTime VARCHAR(255) NOT NULL,
    Hostname VARCHAR(255) NOT NULL,
    Keywords VARCHAR(255) NOT NULL,
    EventType VARCHAR(255) NOT NULL, 
    SeverityValue INT NOT NULL, 
    Severity VARCHAR(255) NOT NULL, 
    EventID INT NOT NULL, 
    SourceName VARCHAR(255) NOT NULL, 
    ProviderGuid VARCHAR(255) NOT NULL, 
    Version_ INT NOT NULL, 
    Task INT NOT NULL,
    OpcodeValue INT NOT NULL,
    RecordNumber INT NOT NULL,
    ProcessID INT NOT NULL,
    ThreadID INT NOT NULL,
    Channel VARCHAR(255) NOT NULL,
    Domain VARCHAR(255) NOT NULL,
    AccountName VARCHAR(255) NOT NULL,
    UserID VARCHAR(255) NOT NULL,
    AccountType VARCHAR(255) NOT NULL,
    Message_ VARCHAR(255) NOT NULL,
    Opcode VARCHAR(255) NOT NULL,
    EventReceivedTime VARCHAR(255) NOT NULL,
    SourceModuleName VARCHAR(255) NOT NULL,
    SourceModuleType VARCHAR(255) NOT NULL
);