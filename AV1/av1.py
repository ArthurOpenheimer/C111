import numpy as np

posts = np.loadtxt('social_media.csv', delimiter=';', dtype=str, encoding='utf-8', skiprows=1)

#q1
count = np.count_nonzero(posts[:, 4] == 'Brazil')

print('questao 1 -', count)

#q2
total = len(posts)
education = np.count_nonzero(posts[:, 2] == 'Education')
        
porcentagem = (education/total)*100

print(f'questao 2 - {porcentagem:.2f}%')

#q3
instagram = posts[posts[:, 1] == 'Instagram']
media_views = instagram[:, 5].astype(int).mean()
media_likes = instagram[:, 6].astype(int).mean()
dicionario = {'media_views': float(media_views), 'media_likes': float(media_likes)}

print('questao 3 -', dicionario)

#q4
plataformas = np.unique(posts[:, 1], return_counts=True)
maior = plataformas[0][np.argmax(plataformas[1])]
numero = np.max(plataformas[1])

print('questao 4 -', maior, numero)

#q5
likes = posts[:, 6].astype(int)
maximo = np.argmax(likes)

print('questao 5 -', posts[maximo][4])