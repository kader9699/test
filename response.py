import random
import time
# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "kader: Sannu da zuwa! Yaya zan taimake ka yau?",
            "kader: Hello, mutum! Ko akwai wani abu da zan iya taimaka maka da shi?",
            "kader: Kuna bukatar taimako?",
            "kader: Sannu! Me zan yi miki yau?",
            "kader: Hello! Yaya zan iya inganta ranar ku?",
            "kader: Sannu! Yaya zan iya zama hidima?",
            "kader: Kai can! Me kuke buƙatar taimako da shi?",
            "kader: Hi! Yaya zan iya taimaka maka a yanzu?",
            "kader: Sannu! Me zan taimake ka yau?",
            "kader: Barka da rana! Yaya zan iya taimaka muku?",
            "kader: Hello! Yaya zan taimake ka yau?",
            "kader: Kai! Me zan yi maka?",
            "kader: Sannu! Ta yaya zan taimake ka fita?",
            "kader: Sannunku! Yaya zan iya taimaka muku a wannan lokacin?",
            "kader:Sannu da zuwa! Me kuke bukata taimako da shi?",
            "kader: Kai! Yaya zan taimake ka yau?",
            "kader: Kai! Bana san dabanci fa ?",
            "kader: Kai! Nagaji bazani taimaka maka ba ?",
            "kader: Kai! Kanada kudi malan ?",
            "kader: Sannu! Ko akwai wani abu da kuke buƙatar taimako da shi?",
            "kader: Hi! Yaya zan iya taimaka muku yau?",
            "kader: Lafiya! Me zan taimake ka da shi?",
            "kader: Kai! Kuna buƙatar taimako yau?"
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)