import boto3
import json
from datetime import datetime

REGION = "us-east-1"

bedrock = boto3.client("bedrock-runtime", region_name=REGION)
s3 = boto3.client("s3", region_name=REGION)
ses = boto3.client("ses", region_name=REGION)

BUCKET_NAME = "codementorai-daily-questions-409513749721"

SENDER_EMAIL = "deepakrajjs2909@gmail.com"
RECIPIENT_EMAIL = "deepakrajjs2909@gmail.com"


def lambda_handler(event, context):

    prompt = """
Generate today's coding interview preparation.

Include:
1. One DSA interview question
2. Difficulty level
3. One hint
4. One interview tip

Keep the response under 200 words.
"""

    response = bedrock.invoke_model(
        modelId="amazon.nova-lite-v1:0",
        contentType="application/json",
        accept="application/json",
        body=json.dumps({
            "schemaVersion": "messages-v1",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "text": prompt
                        }
                    ]
                }
            ],
            "inferenceConfig": {
                "maxTokens": 300,
                "temperature": 0.7
            }
        })
    )

    result = json.loads(response["body"].read())

    ai_text = result["output"]["message"]["content"][0]["text"]

    timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"question_{timestamp}.json"

    # Save to S3
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=filename,
        Body=json.dumps(result, indent=2),
        ContentType="application/json"
    )

    # Send email
    try:
        ses.send_email(
            Source=SENDER_EMAIL,
            Destination={
                "ToAddresses": [RECIPIENT_EMAIL]
            },
            Message={
                "Subject": {
                    "Data": "Today's AI Coding Interview Question"
                },
                "Body": {
                    "Text": {
                        "Data": ai_text
                    }
                }
            }
        )

        email_status = "Email sent successfully"

    except Exception as e:
        email_status = str(e)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Interview question generated successfully.",
            "email_status": email_status,
            "file": filename,
            "question": ai_text
        })
    }
