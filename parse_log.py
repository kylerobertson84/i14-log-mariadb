
import json
# import mysql.connector
# from mysql.connector import Error
from dataclasses import dataclass, fields

from Log import Log
from sql import *

with open('log.json', 'r') as file:

    json_objects = json.load(file)


data = {
    "logs": json_objects
}

# print(data)
list_log_objects = []



for index, log in enumerate(data["logs"]):
    print(f"log {index + 1}:")
    print("whatever:", log["EventTime"])
    log_obj = Log(
        log["EventTime"],
        log["Hostname"],
        log["Keywords"],
        log["EventType"],
        log["SeverityValue"],
        log["Severity"],
        log["EventID"],
        log["SourceName"],
        log["ProviderGuid"],
        log["Version"],
        log["Task"],
        log["OpcodeValue"],
        log["RecordNumber"],
        log["ProcessID"],
        log["ThreadID"],
        log["Channel"],
        log["Domain"],
        log["AccountName"],
        log["UserID"],
        log["AccountType"],
        log["Message"],
        log["Opcode"],
        log["EventReceivedTime"],
        log["SourceModuleName"],
        log["SourceModuleType"]
        
    )
    insert_str = f"""
    INSERT INTO raw_logs (
        EventTime, 
        Hostname, 
        Keywords, 
        EventType, 
        SeverityValue, 
        Severity, 
        EventID, 
        SourceName, 
        ProviderGuid, 
        Version_, 
        Task,
        OpcodeValue,
        RecordNumber,
        ProcessID,
        ThreadID,
        Channel,
        Domain,
        AccountName,
        UserID,
        AccountType,
        Message_,
        Opcode,
        EventReceivedTime,
        SourceModuleName,
        SourceModuleType
    ) VALUES (
        '{log_obj.EventTime}',
        '{log_obj.Hostname}',
        '{log_obj.Keywords}',
        '{log_obj.EventType}',
        {log_obj.SeverityValue},
        '{log_obj.Severity}',
        {log_obj.EventID},
        '{log_obj.SourceName}',
        '{log_obj.ProviderGuid}',
        {log_obj.Version},
        {log_obj.Task},
        {log_obj.OpcodeValue},
        {log_obj.RecordNumber},
        {log_obj.ProcessID},
        {log_obj.ThreadID},
        '{log_obj.Channel}',
        '{log_obj.Domain}',
        '{log_obj.AccountName}',
        '{log_obj.UserID}',
        '{log_obj.AccountType}',
        '{log_obj.Message}',
        '{log_obj.Opcode}',
        '{log_obj.EventReceivedTime}',
        '{log_obj.SourceModuleName}',
        '{log_obj.SourceModuleName}'
    );
    """
    connect(insert_str)
    # list_log_objects.append(log_obj)






# for obj in list_log_objects:
#     print(obj.EventTime)
#     print(obj.Hostname)
#     print(obj.Keywords)
#     print(obj.EventType)
#     print(obj.SeverityValue)
#     # and so on . . .
#     print()




