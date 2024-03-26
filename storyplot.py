import streamlit as st
import openai
from method_class import MethodClass as mc

def main():

    # Apply custom CSS for title styling
    st.markdown(
    """
     <style>
    @import url('https://fonts.googleapis.com/css2?family=Brush+Script+MT&display=swap');
    .title-text {
        font-family: 'Brush Script MT', cursive;
        font-size: 85px;
        text-align: center;
        font-weight: bold;
        background: linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(9,9,121,1) 16%, rgba(143,80,8,1) 30%, rgba(61,112,78,1) 45%, rgba(137,45,137,1) 59%, rgba(192,113,74,1) 78%, rgba(0,212,255,1) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title with custom styling and decorative font
    st.markdown('<p class="title-text">AI Story Plot Generator</p>', unsafe_allow_html=True)

    # User Input Section
    st.sidebar.title("User Input")

    genre = st.sidebar.selectbox(
        "Genre", ["Sci-Fi", "Fantasy", "Mystery", "Romance", "Thriller"],
        help=" * Choose the genre for your story."
    )
    theme = st.sidebar.text_input(
        "Theme", "", help=" * Briefly describe the central idea or conflict of your story (e.g., love conquers all, redemption, survival)."
    )
    characters = st.sidebar.text_input(
        "Characters", "", help=" * Introduce your main characters (e.g., a brave knight, a cunning detective, a rebellious teenager)."
    )
    setting = st.sidebar.text_input(
        "Setting", "", help=" * Describe the world or environment where your story takes place (e.g., a futuristic city, a magical kingdom, a haunted mansion)."
    )
    plot_elements = st.sidebar.text_area(
        "Desired Plot Elements", "", help=" * List events or challenges your characters will encounter (e.g., a betrayal, a chase scene, a discovery)."
    )

    # Generate Story Plot
    if st.sidebar.button("Generate Plot"):
        # Construct prompt from user input
        prompt = f"In a {setting} setting, {characters} encounter a {theme} situation. They embark on a journey filled with {plot_elements}. As the story unfolds, unexpected twists and turns shape the narrative.\n\nWrite a compelling story outline in the {genre} genre, incorporating these elements."

        # Generate story plot
        story_plot = mc.generate_story_plot(prompt)

        # Display generated story plot
        st.subheader("Generated Story Plot:")
        st.write(story_plot)

    

if __name__ == "__main__":
    main()