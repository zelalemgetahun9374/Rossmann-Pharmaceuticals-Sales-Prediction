import streamlit as st
import awesome_streamlit as ast


def write():
    """Used to write the page in the app.py file"""
    st.title('Insights from the historical data')

    st.write('---')
    st.markdown('## StoreType vs Sales and Customers')
    st.image("./src/images/a.png")
    st.write('The most selling and crowded store type is b.')

    st.write('---')
    st.markdown('## Assortment vs Sales and Customers')
    st.image("./src/images/b.png")
    st.write('The most selling and crowded assortment is b.')

    st.write('---')
    st.markdown('## Open vs DayOfWeek')
    st.image("./src/images/c.png")
    st.write('Most of the stores are closed at sundays but almost every store is open at saturday.')

    st.write('---')
    st.markdown('## CompetitionDistance vs Sales')
    st.image("./src/images/d.png")
    st.write("""
            Stores with the smallest competition distance have the highest sales. This indicates that the
            stores are located at city center or near hospitals. Even though having large distance between
            competitors is ideally considered great for sales, stores located at city centers will still get more
            sales regardless of competitors distance as there are more customers at city centers.
        """)

    st.write('---')
    st.markdown('## Correlation Analysis')
    st.image("./src/images/e.png")
    st.write('As we can see sales is highly correlated to customers.')

    st.write('---')
    st.markdown('## Monthly sales per StoreType and Promo')
    st.image("./src/images/f.png")

    st.write('---')
    st.markdown('## Monthly sales per Assortment and Promo')
    st.image("./src/images/g.png")
    st.write("""
            For all stores, promotion leads to increase in Sales and Customers. But promotions have low
            impact on store type b and assortment b when comparing to the other store types and
            assortments. So promotions should be applied more in the other store types and assortments.
        """)

    st.write('---')
    st.markdown('## Sales of stores open per DayOfWeek and StoreType')
    st.image("./src/images/h.png")
    st.write('Store type b is the most opened store type on all weekdays and has its highest sales on sundays than the other days.')

    st.write('---')
    st.markdown('## Sales of stores open per DayOfWeek and Assortment')
    st.image("./src/images/i.png")
    st.write('Assortment a and b are the most opened assortments on all weekdays and have their highest sales on Sundays than the other days.')

    st.write('---')
    st.markdown('## Sales before, after and during Christmas')
    st.image("./src/images/j.png")
    st.write("""
            Sales are increased during Christmas week, especially the week before. This might be due to the
            fact that people buy more beauty products or some common medicines for precaution during
            Christmas celebrations.
        """)