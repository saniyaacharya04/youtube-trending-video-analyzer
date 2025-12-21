def prepare_visualization_payload(videos):
    return {
        "count": len(videos),
        "titles": [v.title for v in videos]
    }
