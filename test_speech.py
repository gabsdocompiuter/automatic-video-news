from text_to_speech import Speech

sp = Speech()
sp.add_phrase('Esse é apenas um teste de fala simples. Estou cansado')
sp.save('outputs/speech.mp3')