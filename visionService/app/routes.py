from flask import Blueprint, request, jsonify
from .model.vision import get_image_caption

api_bp = Blueprint('api_bp', __name__)


@api_bp.route('/vision', methods=['POST'])
def vision():
    image_url = request.json['image_url']
    message = request.json['message']
    choice_response = get_image_caption(image_url, message)
    if hasattr(choice_response, 'message') and hasattr(choice_response.message, 'content'):
        # Extract the content of the message
        caption = choice_response.message.content
        # Return a JSON response with the caption
        return jsonify({"caption": caption})
    else:
        # Handle case where response does not have the expected structure
        return jsonify({"error": "Could not extract caption"}), 500
