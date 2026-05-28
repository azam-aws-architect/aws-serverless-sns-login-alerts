import json

def lambda_handler(event, context):
    for record in event['Records']:
        sns_message = record['Sns']['Message']
        print(f"🚨 SECURITY ALERT: New Login Detected! Details: {sns_message}")

    return {
        'statusCode': 200,
        'body': json.dumps('Security notification processed successfully!')
    }
