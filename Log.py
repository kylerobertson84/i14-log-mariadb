
class Log:
    def __init__(
            self, 
            EventTime, 
            Hostname, 
            Keywords, 
            EventType, 
            SeverityValue, 
            Severity, 
            EventID, 
            SourceName, 
            ProviderGuid, 
            Version, 
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
            Message,
            Opcode,
            EventReceivedTime,
            SourceModuleName,
            SourceModuleType
        ):
        self._EventTime = EventTime  
        self._Hostname = Hostname
        self._Keywords = str(Keywords)
        self._EventType = EventType
        self._SeverityValue = SeverityValue
        self._Severity = Severity
        self._EventID = EventID
        self._SourceName = SourceName
        self._ProviderGuid = ProviderGuid
        self._Version = Version
        self._Task = Task
        self._OpcodeValue = OpcodeValue
        self._RecordNumber = RecordNumber
        self._ProcessID = ProcessID
        self._ThreadID = ThreadID
        self._Channel = Channel
        self._Domain = Domain
        self._AccountName = AccountName
        self._UserID = UserID
        self._AccountType = AccountType
        self._Message = Message
        self._Opcode = Opcode
        self._EventReceivedTime = EventReceivedTime
        self._SourceModuleName = SourceModuleName
        self._SourceModuleType = SourceModuleType
    
    @property
    def EventTime(self):
        return self._EventTime

    @EventTime.setter
    def EventTime(self, value):
        if not isinstance(value, str):
            raise TypeError("EventTime must be string")
        self._EventTime = value
        
    
    @property
    def Hostname(self):
        return self._Hostname
    
    @Hostname.setter
    def Hostname(self,value):
        if not isinstance(value, str):
            raise TypeError("Hostname must be string")
        self._Hostname = value

    
    @property
    def Keywords(self):
        return self._Keywords

    @Keywords.setter
    def Keywords(self,value):
        if not isinstance(value, str):
            raise TypeError("Keywords must be int")
        self._Keywords = value
    
    @property
    def EventType(self):
        return self._EventType

    @EventType.setter
    def EventType(self,value):
        if not isinstance(value, str ):
            raise TypeError("EventType must be string")
        self.EventType = value

        
    @property
    def SeverityValue(self):
        return self._SeverityValue

    @SeverityValue.setter
    def SeverityValue(self,value):
        if not isinstance(value, int):
            raise TypeError("SeverityValue")
        self._SeverityValue = value

    @property
    def Severity(self):
        return self._Severity

    @Severity.setter
    def Severity(self,value):
        if not isinstance(value, str):
            raise TypeError("Severity")
        self._Severity = value
    
    @property
    def EventID(self):
        return self._EventID

    @EventID.setter
    def EventID(self,value):
        if not isinstance(value, int):
            raise TypeError("EventID")
        self._EventID = value
    
    @property
    def SourceName(self):
        return self._SourceName

    @SourceName.setter
    def SourceName(self,value):
        if not isinstance(value, str):
            raise TypeError("SourceName")
        self._SourceName = value
    
    @property
    def ProviderGuid(self):
        return self._ProviderGuid

    @ProviderGuid.setter
    def ProviderGuid(self,value):
        if not isinstance(value, str):
            raise TypeError("ProviderGuid")
        self._ProviderGuid = value
    
    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self,value):
        if not isinstance(value, int):
            raise TypeError("Version")
        self._Version = value
    
    @property
    def Task(self):
        return self._Task

    @Task.setter
    def Task(self,value):
        if not isinstance(value, int):
            raise TypeError("Task")
        self._Task = value
    
    @property 
    def OpcodeValue(self):
        return self._OpcodeValue

    @OpcodeValue.setter
    def OpcodeValue(self,value):
        if not isinstance(value, int):
            raise TypeError("OpcodeValue")
        self._OpcodeValue = value
    
    @property
    def RecordNumber(self):
        return self._RecordNumber

    @RecordNumber.setter
    def RecordNumber(self,value):
        if not isinstance(value,int):
            raise TypeError("RecordNumber")
        self._RecordNumber = value
    
    @property
    def ProcessID(self):
        return self._ProcessID

    @ProcessID.setter
    def ProcessID(self,value):
        if not isinstance(value,int ):
            raise TypeError("ProcessID")
        self._ProcessID = value
    
    @property
    def ThreadID(self):
        return self._ThreadID

    @ThreadID.setter
    def ThreadID(self,value):
        if not isinstance(value,int ):
            raise TypeError("ThreadID")
        self._ThreadID = value
    
    @property
    def Channel(self):
        return self._Channel

    @Channel.setter
    def Channel(self,value):
        if not isinstance(value,str ):
            raise TypeError("Channel")
        self._Channel = value
    
    @property
    def Domain(self):    
        return self._Domain

    @Domain.setter
    def Domain(self,value):
        if not isinstance(value, str):
            raise TypeError("Domain")
        self._Domain = value
    
    @property
    def AccountName(self):    
        return self._AccountName

    @AccountName.setter
    def AccountName(self,value):
        if not isinstance(value, str):
            raise TypeError("AccountName")
        self._AccountName = value
    
    @property
    def UserID(self):
        return self._UserID

    @UserID.setter
    def UserID(self,value):
        if not isinstance(value, str):
            raise TypeError("UserID")
        self._UserID = value
    
    @property
    def AccountType(self):    
        return self._AccountType

    @AccountType.setter
    def AccountType(self,value):
        if not isinstance(value, str):
            raise TypeError("AccountType")
        self._AccountType = value
    
    @property
    def Message(self):   
        return self._Message

    @Message.setter
    def Message(self,value):
        if not isinstance(value, str ):
            raise TypeError("Message")
        self._Message = value
    

    @property
    def Opcode(self):    
        return self._Opcode

    @Opcode.setter
    def Opcode(self,value):
        if not isinstance(value,str ):
            raise TypeError("Opcode")
        self._Opcode = value
    

    @property
    def EventReceivedTime(self):
        return self._EventReceivedTime

    @EventReceivedTime.setter
    def EventReceivedTime(self,value):
        if not isinstance(value, str):
            raise TypeError("EventReceivedTime")
        self._EventReceivedTime = value
    

    @property
    def SourceModuleName(self):   
        return self._SourceModuleName

    @SourceModuleName.setter
    def SourceModuleName(self,value):
        if not isinstance(value, str):
            raise TypeError("SourceModuleName")
        self._SourceModuleName = value
    

    @property
    def SourceModuleType(self):    
        return self._SourceModuleType

    @SourceModuleType.setter
    def SourceModuleType(self,value):
        if not isinstance(value,str ):
            raise TypeError("SourceModuleType")
        self._SourceModuleType = value
