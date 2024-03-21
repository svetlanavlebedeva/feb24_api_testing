schema = {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "category": {"type": "object"},
            "name": {"type": "string"},
            "photoUrls": {"type": "array"},
            "tags": {"type": "array"},
            "status": {"type": "string"},
        },
        "required": ["id", "name", "status"]
    }