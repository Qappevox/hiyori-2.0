import os

def clear_data(data):
    for i in data:
        try:
            os.remove(i)
        except:
            pass
data = ["AI_model.h5","classes.pkl","words.pkl"]

clear_data(data=data)