#Class for a doctors note

class DoctorNote:

    def __init__(self,PatientName="",DateStamp=0,Note=[], Token="") -> None:
        '''Trying to add sceurity with a token think about blockchain potentiall'''
        try:
            self.PatientName = PatientName
            self.DateStamp = DateStamp
            self.Note = Note
            self.Token = Token
        except Exception:
            raise ValueError 
    
    def __getPatientName__(self) -> str:
        return self.PatientName

    def __setPatientName__(self, __PatientName: str) -> None:
        self.PatientName = __PatientName

    def __getNote__(self) -> str:
        return self.Note

    def __setNote__(self, __Note: str) -> None:
        self.Note = __Note

    def __repr__(self) -> str:
        return {"Patient Name":self.PatientName,"Note":self.Note,"Date":self.DateStamp}


    