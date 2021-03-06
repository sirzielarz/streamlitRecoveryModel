import streamlit as st
import pickle
from datetime import datetime

startTime = datetime.now()

filename = "model2.sv"
model = pickle.load(open(filename, 'rb'))


def main():
    st.set_page_config(page_title="Czy wyzdrowiejesz po tygodniu? 馃樂")
    overview = st.container()
    left, right = st.columns(2)
    prediction = st.container()

    st.image(
        "https://blog.medisave.co.uk/wp-content/uploads/2020/09/Funny-Doctors-Medical-Memes-137-5b50a25d568a0__700.jpg")
    st.caption("s19086, Jacek Zi贸艂kowski")

    with overview:
        st.title("Czy wyzdrowiejesz po tygodniu? 馃樂")
        st.title("")

    with left:
        st.write(
            "Jak dowodz膮 najnowsze badania ameryka艅skich naukowc贸w*, im mniej chor贸b i objaw贸w, tym wi臋ksza szansa na wyzdrowienie po tygodniu. "
            "Brzmi jak 偶art? Nic bardziej mylnego! Przy wykorzystaniu naszego niezwykle skomplikowanego modelu matematycznego mo偶esz z nieznan膮 wcze艣niej precyzj膮 dowiedzie膰 si臋, czy osoba z danymi parametrami 偶yciowymi jest w stanie wykurowa膰 si臋 w ci膮gu 7 dni!")
        st.caption("\* potrzebne 藕r贸d艂o")

    with right:
        symptoms_slider = st.slider("Liczba objaw贸w", value=3, min_value=1, max_value=5)
        age_slider = st.slider("Wiek", value=50, min_value=1, max_value=100)
        diseases_slider = st.slider("Liczba chor贸b wsp贸艂istniej膮cych", value=2, min_value=0, max_value=5)
        height_slider = st.slider("Wzrost", value=150, min_value=100, max_value=200)

    data = [[symptoms_slider, age_slider, diseases_slider, height_slider]]
    recovery = model.predict(data)
    s_confidence = model.predict_proba(data)

    with prediction:
        st.header("")
        st.header("Czy dana osoba wyzdrowieje po tygodniu? {0}".format("Tak!!! 馃コ" if recovery[0] == 0 else "Nie 馃ぇ"))
        st.subheader("Pewno艣膰 predykcji {0:.2f} %".format(s_confidence[0][recovery][0] * 100))


if __name__ == "__main__":
    main()
