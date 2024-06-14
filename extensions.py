from faker import Faker
fake = Faker()

def generate_fulltext(num_words):
    words = []
    for i in range(1, num_words + 1):
        word = fake.word()
        words.append(f"'{word}':{i}")
    return ' '.join(words)

def generate_special_features():
    features = ['Trailers', 'Commentaries', 'Deleted Scenes', 'Behind the Scenes']
    num_features = fake.random_int(min=1, max=len(features))
    selected_features = fake.random_sample(elements=features, length=num_features)
    return selected_features