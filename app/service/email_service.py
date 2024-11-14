from collections import Counter

from app.repository.email_repository import get_user_by_email, get_all_sentences
from app.service.kafka_service.producer import publish_explosive, publish_hostage
from dictalchemy.utils import asdict

def reorder_sentences(email):
    suspicious_keywords = ["explos", "hostage"]
    reordered_sentences = sorted(
        email.get('sentences', []),
        key=lambda sentence: any(keyword in sentence for keyword in suspicious_keywords),
        reverse=True
    )
    email['sentences'] = reordered_sentences

def check_if_contains_suspicious_content(email):
    for sentence in email.get('sentences', []):
        if "explos" in sentence:
            reorder_sentences(email)
            publish_explosive(email)
            return
        elif "hostage" in sentence:
            reorder_sentences(email)
            publish_hostage(email)
            return

def get_suspicious_content(email):
    user = get_user_by_email(email)
    if not user:
        return None, "User not found"
    hostage_sentences = [sentence.sentence for sentence in user.hostage_sentences]
    explosive_sentences = [sentence.sentence for sentence in user.explosive_sentences]
    location = user.location
    device_info = user.device_info
    return {
            "email": email,
            "hostage_sentences": hostage_sentences,
            "explosive_sentences": explosive_sentences,
            "location": asdict(location),
            "device_info": asdict(device_info)
    }, None

def get_most_common_word():
    try:
        all_sentences = get_all_sentences()
        words = [word.lower() for sentence in all_sentences for word in sentence[0].split()]
        word_counts = Counter(words).most_common(1)

        if word_counts:
            most_common_word, frequency = word_counts[0]
            return most_common_word, frequency
        else:
            return None, 0
    except Exception as e:
        raise e
