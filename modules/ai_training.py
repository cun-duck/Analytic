# modules/ai_training.py
import pandas as pd


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

training_data = pd.DataFrame({
    'text': ["laporan keuangan", "absensi karyawan", "data penjualan"],
    'label': ["keuangan", "absensi", "penjualan"]
})

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(training_data['text'])
y = training_data['label']
model = MultinomialNB()
model.fit(X, y)

def classify_document(text):
    X_new = vectorizer.transform([text])
    prediction = model.predict(X_new)
    return prediction[0]

def enhance_training_with_common_columns(df, common_columns):
    text_data = " ".join([" ".join(df[col].astype(str)) for col in common_columns['tanggal'] + common_columns['harga'] + common_columns['nama']])
    training_data.append({'text': text_data, 'label': 'detected_type'})
    X = vectorizer.fit_transform(training_data['text'])
    model.fit(X, training_data['label'])
