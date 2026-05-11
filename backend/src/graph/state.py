import operator
from typing import Annotated, List, Dict, Optional, Any, TypedDict



#define schema the schema for a singe compliance

class ComplianceIssue(TypedDict):
    category: str
    description: str
    severity: str      # crtical warning
    timestamp:  Optional[str]


#define the global graph state

class VideoAuditState(TypedDict):
    '''
    define the data schema for langgraph execution content
    '''
    video_url: str
    video_id: str
    
    #ingestion and extraction data
    local_file_path: Optional[str]
    video_metadata: Dict[str,any]
    transcript: Optional[str]
    ocr_text: List[str]
    
    #analasys output
    compile_result: Annotated[List[ComplianceIssue],operator.add]
    
    
    #final deliverables
    
    final_status: str #pass | fail
    final_report: str #markdown format
    
    
    #system obervability
    # error: API timeout , system level error
    
    error: Annotated[List[str],operator.add]
    
