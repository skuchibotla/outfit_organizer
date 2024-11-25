from pathlib import Path
from flask import Flask, jsonify, request
from flask_cors import CORS
from rembg import remove
from io import BytesIO
from dotenv import load_dotenv
import os
import boto3

app = Flask(__name__)
s3_client = boto3.client('s3')
CORS(app, resources={r"/*": { "origins": "http://localhost:3000" }})

# Load environment variables
load_dotenv()

def is_valid_user_id(user_id):
  if isinstance(user_id, (int, float)):
    return True 

  if isinstance(user_id, str):
    try:
      float(user_id)
      return True
    except ValueError:
      return False
    
  return False

def params_validation(user_id, files):
  # Validate user_id
  if not user_id:
    return {'error': 'Param user_id missing'}, None, None

  if not is_valid_user_id(user_id):
    return {'error': 'user_id is not valid'}, None, None

  # Validate file
  if 'file' not in files:
    return {'error': 'File not provided'}, None, None

  file = files['file']
  if file.filename == '':
    return {'error': 'No selected file'}, None

  return None, user_id, file

@app.route('/remove-background/<int:user_id>', methods=['POST'])
def remove_background(user_id):
  # Ensure params are valid, return error if validation fails
  validation_error, user_id, file = params_validation(user_id, request.files)
  if validation_error:
    return jsonify(validation_error), 400

  try:
    # Remove background from the image using rembg
    input_bytes = file.read()
    output_image = remove(input_bytes, force_return_bytes=True)
    output_bytes = BytesIO(output_image)

    # Upload processed image to S3 bucket
    key = f"{user_id}/clothes/{file.filename}"
    s3_client.upload_fileobj(output_bytes, os.getenv('S3_BUCKET'), key)
  
    return jsonify({'message': 'Successfully removed background and uploaded image to S3'}), 200

  except Exception as e:
    # Handle any S3 upload issues
    return jsonify({'error': f'Failed to process image or upload: {str(e)}'}), 500

if __name__ == '__main__':
  app.run(port=8000)
