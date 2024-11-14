from app.service.kafka_service.producer import publish_explosive, publish_hostage

def reorder_sentences(email):
    suspicious_keywords = ["explosive", "hostage"]
    reordered_sentences = sorted(
        email.get('sentences', []),
        key=lambda sentence: any(keyword in sentence for keyword in suspicious_keywords),
        reverse=True
    )
    email['sentences'] = reordered_sentences

def check_if_contains_suspicious_content(email):
    for sentence in email.get('sentences', []):
        if "explosive" in sentence:
            reorder_sentences(email)
            publish_explosive(email)
            return
        elif "hostage" in sentence:
            reorder_sentences(email)
            publish_hostage(email)
            return
