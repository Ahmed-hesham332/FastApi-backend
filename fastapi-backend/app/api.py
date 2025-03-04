from fastapi import APIRouter, Depends, HTTPException
from app.config import settings  
from app.dependencies import get_api_key
from app.logger import logger
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

from fastapi import Request

router = APIRouter()

recoreds = []
limit = 50
offset = 0
start_date = "2025-01-01"
end_date = "2025-01-08"


configuration = sib_api_v3_sdk.Configuration()
configuration.api_key["api-key"] = settings.API_KEY  
api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
        sib_api_v3_sdk.ApiClient(configuration)
    )

records = [] 
limit = 50
offset = 0
start_date = "2025-01-01"
end_date = "2025-01-08"

def get_TransactionalEmails():
    
    while True:
        try:
            response = api_instance.get_email_event_report(
                limit=limit,
                offset=offset,
                start_date=start_date,
                end_date=end_date,
            )

            if not response.events:
                break  

            records.extend(response.events)   

        except ApiException as e:
            logger.error(f"Error: {e}")
            return []  

    return records  


@router.get("/email-logs", dependencies=[Depends(get_api_key)])
def export_logs():
    log = get_TransactionalEmails()

    if not log:
        return {"message": "No logs available"}  

    return {"logs": log}
