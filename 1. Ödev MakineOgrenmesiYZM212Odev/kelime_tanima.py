import numpy as np
from hmmlearn import hmm

# EV kelimesi için model
model_ev = hmm.MultinomialHMM(n_components=2, n_iter=100)

X_ev = np.array([[0],[1],[0],[1],[0]])
lengths_ev = [5]

model_ev.fit(X_ev, lengths_ev)


# OKUL kelimesi için model
model_okul = hmm.MultinomialHMM(n_components=3, n_iter=100)

X_okul = np.array([[1],[1],[0],[1],[0],[1]])
lengths_okul = [6]

model_okul.fit(X_okul, lengths_okul)


def kelime_tahmin(obs):

    obs = np.array(obs).reshape(-1,1)

    score_ev = model_ev.score(obs)
    score_okul = model_okul.score(obs)

    if score_ev > score_okul:
        return "Tahmin edilen kelime: EV"
    else:
        return "Tahmin edilen kelime: OKUL"


# test verisi
test = [0,1]

print(kelime_tahmin(test))