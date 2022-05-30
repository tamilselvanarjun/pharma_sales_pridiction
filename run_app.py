import streamlit as st
import awesome_streamlit as ast
import assets.pages.home
import assets.pages.data
import assets.pages.pred
import assets.pages.insights

ast.core.services.other.set_logging_format()

# create the choices
PAGES = {
    "Home": assets.pages.home,
    "Historical Data":assets.pages.data,
    "Bussiness Insights": assets.pages.insights,
    "View Predictions": assets.pages.pred
}


# render the pages
def main():
    """Main function of these App"""
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]

    with st.spinner(f"Loading Features {selection} ..."):
        ast.shared.components.write_page(page)

    st.sidebar.title("About The Rosemann")
    st.sidebar.info(
        """
        An end-to-end product which enables the Rosemann pharmaceutical company to 
        view predictions on sales across their stores and six weeks ahead of time and the trends expected.
"""
    )

# run it
if __name__ == "__main__":
    main()