import os
import json
from pathlib import Path
from turtle import down
from nylas import Client


class NylasService:
    def __init__(self):
        self.client = Client(
            api_key=os.environ.get("NYLAS_API_KEY"),
            api_uri=os.environ.get("NYLAS_API_URI"),
        )

    def load_webhook_data(self, uuid):
        """Load webhook data from a JSON file in the events directory."""
        base_dir = Path(__file__).resolve().parent.parent.parent
        events_dir = base_dir / "requests" / "events"
        file_path = events_dir / f"{uuid}.json"

        if not file_path.exists():
            raise FileNotFoundError(f"No webhook data found for UUID: {uuid}")

        with open(file_path, "r") as f:
            return json.load(f)

    def download_attachment(self, attachment_id, grant_id, message_id):
        """Download an attachment from Nylas."""
        # Get the attachment using the grant_id and message_id
        attachment = self.client.attachments.find(
            identifier=grant_id,
            attachment_id=attachment_id,
            query_params={"message_id": message_id},
        )

        # Download the file content
        file_content = self.client.attachments.download_bytes(
            identifier=grant_id,
            attachment_id=attachment_id,
            query_params={"message_id": message_id},
        )

        return {
            "content": file_content,
            "content_type": attachment.data.content_type,
            "filename": attachment.data.filename,
        }

# To Run download_attachment from this application from the command  below:
# python -c "from your_module import NylasService; s = NylasService(); print(s.download_attachment('ATTACHMENT_ID', 'GRANT_ID', 'MESSAGE_ID'))"

# If I want to instantiate the Nylas service and run download, see the code below. My next objective is to create an interface for it.
"""
# Step 1: Import and initialize the service
service = NylasService()

# Step 2: Call the method with your actual values
result = service.download_attachment(
    attachment_id="ATTACHMENT_ID_HERE",
    grant_id="GRANT_ID_HERE",
    message_id="MESSAGE_ID_HERE"
)

# Step 3: (Optional) Save the file
with open(result["filename"], "wb") as f:
    f.write(result["content"])
print(f"Downloaded: {result['filename']}")
"""
