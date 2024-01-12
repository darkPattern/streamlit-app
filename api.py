import firebase_admin
import streamlit as st
from firebase_admin import credentials, firestore


@st.cache_resource
def get_db():
    try:
        cred = credentials.Certificate("dark-pattern-24460-firebase-adminsdk-co96w-8c09e0305f.json")
    except FileNotFoundError:
        cred = credentials.Certificate({
            "type": "service_account",
            "project_id": "dark-pattern-24460",
            "private_key_id": st.secrets["private_key_id"],
            "private_key": st.secrets["private_key"],
            "client_email": st.secrets["client_email"],
            "client_id": st.secrets["client_id"],
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": st.secrets["client_x509_cert_url"],
            "universe_domain": "googleapis.com",
        })

    firebase_admin.initialize_app(cred)
    return firestore.client()


db = get_db()
web_col = db.collection(u'websites')

ecommerce_data = {
}


def get_collection():
    web_dict = {}
    web_stats = web_col.stream()
    for web in web_stats:
        web_dict[web.id] = web.to_dict()

    return web_dict


def set_the_data(name, url, tScore, uniquePattern, tPattern):
    web_col.document(name).set({
        'name': name,
        'url': url,
        'tScore': tScore,
        'uniquePattern': uniquePattern,
        'tPattern': tPattern
    })


def push_to_db():
    all_id = []
    for key, value in ecommerce_data.items():
        web_col.document(key).set(value)
        all_id.append(key)
    return all_id


if __name__ == '__main__':
    pass
