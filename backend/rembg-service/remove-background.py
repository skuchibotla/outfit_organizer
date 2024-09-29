from pathlib import Path
from flask import Flask, jsonify, request
from rembg import remove
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv
import os
import boto3

app = Flask(__name__)
s3_client = boto3.client('s3')

# Load environment variables
load_dotenv()

# Validation functions
def is_valid_image(file_path):
  try:
    if not file_path.is_file():
      return False
    Image.open(file_path).verify()
    return True
  except (OSError, Image.UnidentifiedImageError):
    return False

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

def params_validation(params):
  if not params:
    return {'error': 'Required params not provided'}, None, None

  if 'image_path' not in params:
    return {'error': 'Param image_path missing'}, None, None

  if 'user_id' not in params:
    return {'error': 'Param user_id missing'}, None, None

  # Validate image_path
  image_path = Path(params.get('image_path'))
  if not is_valid_image(image_path):
    return {'error': 'image_path is not a valid image file'}, None, None

  # Validate user_id
  user_id = params.get('user_id')
  if not is_valid_user_id(user_id):
    return {'error': 'user_id is not valid'}, None, None

  return None, user_id, image_path

@app.route('/remove-background', methods=['GET'])
def remove_background():
  # Ensure params are valid, return error if validation fails
  validation_error, user_id, image_path = params_validation(request.args)
  if validation_error:
    return jsonify(validation_error), 400

  try:
    with open(image_path, 'rb') as input_image:
      # Remove background from the image using rembg
      input_bytes = input_image.read()
      output_image = remove(input_bytes, force_return_bytes=True)
      output_bytes = BytesIO(output_image)

      # Upload processed image to S3 bucket
      key = f"{user_id}/clothes/{image_path.stem}-rembg{image_path.suffix}"
      s3_client.upload_fileobj(output_bytes, os.getenv('S3_BUCKET'), key)
    
    return jsonify({'message': 'Successfully removed background and uploaded image to S3'}), 200

  except Exception as e:
    # Handle any S3 upload issues
    return jsonify({'error': f'Failed to process image or upload: {str(e)}'}), 500

if __name__ == '__main__':
  app.run(port=8000)