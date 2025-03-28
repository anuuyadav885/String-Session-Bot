from os import environ

API_ID = int(environ.get("API_ID", "24509126"))
API_HASH = environ.get("API_HASH", "2c1e3e02b9e1b0a3f9c7955d5d55a1d5")
BOT_TOKEN = environ.get("BOT_TOKEN", "7692624621:AAHnW_JShY4EghKpvorRD6xsA-LQgW6ypcg")
OWNER_ID = int(environ.get("OWNER_ID", "6127347210"))
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "https://t.me/+fK5x8NgiYKQ0ZThl"))
MONGO_DB_URI = environ.get("MONGO_DB_URI", "mongodb+srv://codaga9286:JgH1nbOW5JSXUO4U@cluster0.if4xdya.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
PORT = int(environ.get('PORT', 8080))
AUTH_CHANNELS = environ.get("AUTH_CHANNEL", "-1002584614736")
AUTH_CHANNELS = [int(channel_id) for channel_id in AUTH_CHANNELS.split(",")]
