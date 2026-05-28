import json 
import os
import re
import logging
from typing import Dict,Any , List

from langchain_openai import AzureChatOpenAI ,AzureOpenAIEmbeddings
from langchain_comminity.vectorstores import AzureSearch
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMesaage,HumanMessage

#import state schema

from backend.src.graph.state import VideoAuditState,ComplianceIssue

#import service
from backend.src.services.video_indexer import VideoIndexerService

#configure logger
logger= logging.getLogger("brand-guardian")
logging.basicConfig(level=logging.INFO)

# NODE-1 : Indexer
def index_video_node(state: VideoAuditState)-> Dict[str,Any]:
    '''
    Download the youtube video from the url
    upload to the azure video indexer
    extract the insights
    '''
    video_url = state.get("video_url")
    video_id_input = state.get("video_id","vid_demo")
    
    logger.info(f"----- [Node:Inder] Processing...: {video_url}")
    local_filename= "temp_audit_video.mp4"
    
    try:
        vi_service = VideoIndexerService()
        # download
        if "youtube.com" in video_url or "youtube.be" in video_url:
            local_path = vi_service.download_youtube_video(video_url , output_path = local_filename)
            logger.info(" video download completed 100%")
        else:
            raise Exception("Please provide a valid youtube url for this")
        
        # upload to azure vi services
        azure_video_id = vi_service.upload_video(local_path , video_name = video_id_input)
        logger.info(f" upload success Azure id: {azure_video_id}") 
        
        # clean
        if os.path.exists(local_path):
            os.remove(local_path)
        
        
        # wait 
        raw_insights = vi_service.wait_for_processing(azure_video_id)
        # extract
        clean_data = vi_service.extract_date(raw_insights)
        logger.info(f"----- [ Node: Indexer ] Extraction completed ....")
        return clean_data
    except Exception as e:
        logger.error(f"video indexing failed : {e}")
        return {
            "errors": [str(e)],
            "final_status" : "FAIL",
            "transcript" : "",
            "ocr_text" : []
        }



# Node 2 : Compliance Auditor
def audio_content_node(state: VideoAuditState) -> Dict[str,Any]:
    '''
    Performs Retrieval Augmented Generation To Audit The Content
    '''
    
    logger.info("--- [Node Auditor] quering knowledge base & LLM")
    transcript = state.get("transcript" , "")
    if not transcript:
        logger.info("No Transcript available skippping the audit.....")
        return {
            "final_status" : "FAIL",
            "final_result" : "Audit skipped because video processing failed ( NO Transcipt )."
        }
    
    # initialize clients
    llm = AzureChatOpenAI(
        azure_deployment = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT"),
        openai_api_version = os.getenv("AZURE_OPENAI_API_VERSION"),
        temperature = 0.0
    )
    
    embeddings = AzureOpenAIEmbeddings(
        azure_search_endpoint = os.getenv("AZURE_SEARCH_ENDPOINT"),
        azure_search_key = os.getenv("AZURE_SEARCH_API_KEY"),
        index_name = os.getenv("AZURE_SEARCH_INDEX_NAME"),
        embedding_function = embeddings.embed_query
    )
    
    # RAG Retrieval
    ocr_text = state.get("ocr_text",[]),
    query_text = f"{transcript} {''.join(ocr_text)}"
    docs = vector_store.similarity_search(query_text , k=3)
    retrieved_rules = "\n\n".join([doc.page_count for doc in docs])
    
    
    system_prompt = f""" 
                    you are a senior brand compliance auditor.
                    OFFICIAL REGULATORY RULES:
                    {retrieved_rules}
                    INSTRUCTIONS
                    1. ANALYZE THE TRANSCRIPT and OCR text below.
                    2. Indentify Any Violation of the Rules.
                    3. Return strictly json in the following format:
                       {{
        "compliance_results": [
            {{
                "category": "Claim Validation",
                "severity": "CRITICAL",
                "description": "Explanation of the violation..."
            }}
        ],
        "status": "FAIL", 
        "final_report": "Summary of findings..."
    }}

    If no violations are found, set "status" to "PASS" and "compliance_results" to [].
    """
    
    user_message = f"""
    VIDEO_METADATA: {state.get('video_metadata', {})}
    TRANSCRIPT: {transcript}
    ON-SCREEN TEXT (OCR): {ocr_text}
    """

    try:
        response = llm.invoke([
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_message)
        ])
        
        # --- FIX: Clean Markdown if present (```json ... ```) ---
        content = response.content
        if "```" in content:
            # Regex to find JSON inside code blocks
            content = re.search(r"```(?:json)?(.*?)```", content, re.DOTALL).group(1)
            
        audit_data = json.loads(content.strip())
        
        return {
            "compliance_results": audit_data.get("compliance_results", []),
            "final_status": audit_data.get("status", "FAIL"),
            "final_report": audit_data.get("final_report", "No report generated.")
        }

    except Exception as e:
        logger.error(f"System Error in Auditor Node: {str(e)}")
        # Log the raw response to see what went wrong
        logger.error(f"Raw LLM Response: {response.content if 'response' in locals() else 'None'}")
        return {
            "errors": [str(e)],
            "final_status": "FAIL"
        }
          
        
    
    
    

        
    

