import streamlit as st
import pickle
from datetime import datetime

startTime = datetime.now()
# import znanych nam bibliotek

filename = "model2.sv"
model = pickle.load(open(filename, 'rb'))


# otwieramy wcześniej wytrenowany model

# sex_d = {0:"Kobieta",1:"Mężczyzna"}
# pclass_d = {0:"Pierwsza",1:"Druga", 2:"Trzecia"}
# embarked_d = {0:"Cherbourg", 1:"Queenstown", 2:"Southampton"}
# o ile wcześniej kodowaliśmy nasze zmienne, to teraz wprowadzamy etykiety z ich nazewnictwem
def main():
    st.set_page_config(page_title="Czy wyzdrowiejesz po tygodniu? 😷")
    overview = st.container()
    left, right = st.columns(2)
    prediction = st.container()

    st.image(
        "https://blog.medisave.co.uk/wp-content/uploads/2020/09/Funny-Doctors-Medical-Memes-137-5b50a25d568a0__700.jpg")

    with overview:
        st.title("Czy wyzdrowiejesz po tygodniu? 😷")
        st.title("")

    with left:
        st.write(
            "Jak dowodzą najnowsze badania amerykańskich naukowców*, im więcej chorób i objawów, tym większa szansa na wyzdrowienie po tygodniu. "
            "Brzmi jak żart? Nic bardziej mylnego! Z wykorzystaniem naszego niezwykle skomplikowanego modelu matematycznego możesz z niezwykłą precyzją dowiedzieć się, czy osoba z danymi parametrami życiowymi jest w stanie wykurować się w ciągu 7 dni!")
        st.caption("\* potrzebne źródło")

    with right:
        symptoms_slider = st.slider("Liczba objawów", value=3, min_value=1, max_value=5)
        age_slider = st.slider("Wiek", value=50, min_value=1, max_value=100)
        diseases_slider = st.slider("Liczba chorób współistniejących",value=2, min_value=0, max_value=5)
        height_slider = st.slider("Wzrost",value=150, min_value=100, max_value=200)

    data = [[symptoms_slider, age_slider, diseases_slider, height_slider]]
    recovery = model.predict(data)
    s_confidence = model.predict_proba(data)

    with prediction:
        st.header("")
        st.header("Czy dana osoba wyzdrowieje po tygodniu? {0}".format("Tak!!! 🥳" if recovery[0] == 1 else "Nie 🤧"))
        st.subheader("Pewność predykcji {0:.2f} %".format(s_confidence[0][recovery][0] * 100))


if __name__ == "__main__":
    main()

## Źródło danych [https://www.kaggle.com/c/titanic/](https://www.kaggle.com/c/titanic), zastosowanie przez Adama Ramblinga
