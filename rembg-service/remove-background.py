from pathlib import Path
from flask import Flask, jsonify, request
from rembg import remove
from PIL import Image

app = Flask(__name__)

@app.route('/remove-background', methods=['GET'])
def remove_background():
  def is_image(file_path):
    try:
      Image.open(file_path)
      return True
    except (OSError, Image.UnidentifiedImageError):
      return False

  if not request.args or 'image_path' not in request.args:
    return jsonify({ 'error': 'Required params not provided' }), 400
  
  image_path = Path(request.args.get('image_path'))

  if not image_path.is_file() or not is_image(image_path):
    return jsonify({ 'error': 'image_path is not a valid image file' }), 400

  output_path = str(Path.home() / "Desktop" / f"{image_path.stem}-rembg{image_path.suffix}")

  with open(image_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)

  return jsonify({ 'message': 'Successfully removed background from image' })

if __name__ == '__main__':
  app.run(port=8000)