import streamlit as st
from PIL import Image

# ----------------------- #
#      Page Configuration #
# ----------------------- #
st.markdown(
    """
    <style>
    .main {
        background-color: #043c75; /* Navy blue color */
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Set page configuration as the first Streamlit command
st.set_page_config(
    page_title="Sneha Cenoy for General Secretary",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------- #
#          CSS            #
# ----------------------- #

def inject_css():
    # Custom CSS for white and blue color scheme with a round image
    custom_css = """
    <style>
    /* Overall background */
    body {
        background-color: #ffffff;
        color: #0e1e2a;
    }

    /* Header styling */
    .css-1aumxhk h1 {
        color: #1e90ff;
        text-align: center;
    }
    .css-1aumxhk h2, .css-1aumxhk h3, .css-1aumxhk h4, .css-1aumxhk h5, .css-1aumxhk h6 {
        color: #1e90ff;
    }

    /* Sidebar styling */
    .sidebar .sidebar-content {
        background-color: #f0f8ff;
        color: #0e1e2a;
    }

    /* Button styling */
    .stButton>button {
        background-color: #1e90ff;
        color: white;
        border: None;
        border-radius:5px;
        padding: 10px 24px;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #63b3ed;
        color: white;
    }

    /* Links styling */
    a {
        color: #1e90ff;
        text-decoration: none;
    }

    a:hover {
        text-decoration: underline;
    }

    /* Markdown text */
    .markdown-text-container {
        color: #0e1e2a;
    }

    /* Footer styling */
    footer {
        visibility: hidden;
    }

    /* Hide the hamburger menu */
    #MainMenu {visibility: hidden;}

    /* Round image */
    .round-image {
        border-radius: 50%;
        width: 250px;
        height: 250px;
        object-fit: cover;
        border: 5px solid #1e90ff;
    }

    /* Testimonials */
    .testimonial {
        border-left: 4px solid #1e90ff;
        padding-left: 10px;
        margin-bottom: 20px;
        font-style: italic;
    }

    /* Social Media Icons */
    .social-icons a img {
        width: 30px;
        margin-right: 10px;
    }

    /* Contact Form */
    .contact-form {
        background-color: #f0f8ff;
        padding: 20px;
        border-radius: 10px;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

# Inject the custom CSS
inject_css()

# ----------------------- #
#        Configuration    #
# ----------------------- #

# Candidate information
CANDIDATE = {
    "name": "Sneha Cenoy",
    "position": "General Secretary",
    "agenda": """
1. **Provide Cheaper and Better Food**: Ensure affordable, high-quality meal options for students.
2. **Renovate Mess and Washrooms**: Improve hygiene and comfort in shared facilities.
3. **Split Mess Fee and Accommodation Costs**: Allow students to pay for mess and accommodation separately for more financial flexibility.
4. **Assign Cleaning Staff for hostel Rooms**: Ensure rooms are regularly cleaned by dedicated personnel.
5. **Install Water Dispensers Throughout Campus**: Make clean drinking water easily accessible for everyone.
6. **Upgrade Lab Equipment for Biotechnology**: Enhance resources for biotech students to support better research and learning.
7. **Establish Male and Female Lounges in Main Block**: Create comfortable social spaces for students in the main campus building.
8. **Open Recreational Room All Day**: Make recreational facilities accessible at all times to promote student well-being.
9. **Organize a College Trip**: Plan an enjoyable group outing to foster camaraderie among students.
10. **Use Tinted Buses for All**: Ensure privacy and comfort by providing tinted buses for student transportation.
11. **Reduce Fines for Late Return books in library**: Implement a less stringent policy for fines related to late returns to alleviate financial burdens. 
 """,
    "image2": "sneha12.jpg",
    "contact": {
        "Email": "f20220134@dubai.bits-pilani.ac.in",
        "Social Media": {
            "LinkedIn": "https://www.linkedin.com/in/sneha-cenoy-0007b5281",
        }
    }
}

# ----------------------- #
#          App            #
# ----------------------- #

def main():
    inject_css()


    # Your app content here
    # Title of the app
    st.title("🎓 Sneha Cenoy for General Secretary 🎓")

    # Layout: Three columns
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        # Round-framed image of Sneha
        st.markdown("---")

    # About Sneha and Agenda on the Home Page
    st.header("About Me")
    col1, col2 = st.columns([1, 2])
    with col1:
        try:
             st.image(CANDIDATE["image2"], width=300)
        except FileNotFoundError:
            st.warning("Sneha's image not found. Please ensure the image is placed in the 'images/' directory.")
    with col2:
        st.markdown(f"### {CANDIDATE['name']}")
        st.markdown(f"**Position:** {CANDIDATE['position']}")
        st.write("""
            Hey everyone! 👋 I'm Sneha, a third-year CS student, and I'm super excited to be running for 
            General Secretary in the 2024-2025 student council elections! 🎓✨ I'm here to be your voice –
             whether you're a day scholar, a hosteler, or from any discipline! I want to make sure every student’s 
            voice is heard loud and clear. Got any concerns or ideas? I'm always here to listen and make things
             happen! Let’s make this year epic together! 🚀💬
        """)
        st.header("📍 Where to Vote")
        st.markdown("""
              <div class='vote-info'>
              🗳️ **Date and Time**: Thursday, 3rd October<br>
              🗳️ **Time**: 7:00AM to 2:00 pm<br>
              🗳️ **Venue**: EG LAB<br>
              </div>
               """, unsafe_allow_html=True)
        st.header("What makes me unique?")
        st.write("""
            Often, when we raise concerns, the solutions offered are 
            impractical and end up causing inconvenience or extra costs for students.

            But if we approach them with the right solution from the 
            start, we're more likely to see a positive outcome. The key is knowing how to 
            effectively present our requests to make sure they truly benefit us as students.

            As your General Secretary, I'll ensure we ask the right
            questions and propose the best solutions – no more impractical fixes or shifting blame. 
            You come up with the problems, we'll discuss plausible solutions together, and then approach the right people to
            make it happen. This way, we make real changes that actually work for everyone.
        """)
    st.header("Agenda and Vision")
    st.markdown(CANDIDATE["agenda"])

    # Testimonials Section
    st.header("Testimonials")
    testimonial1 = """
    <div class="testimonial">
    "Sneha has been an incredible leader in our study groups, always ensuring everyone's voice is heard."
    <br>
    <strong>- Ananya Gupta, Class of 2024</strong>
    </div>
    """
    testimonial2 = """
    <div class="testimonial">
    "Her dedication to improving campus facilities is truly inspiring."
    <br>
    <strong>- Rohan Mehta, Faculty Advisor</strong>
    </div>
    """
    st.markdown(testimonial1, unsafe_allow_html=True)
    st.markdown(testimonial2, unsafe_allow_html=True)

    st.markdown("---")
    # Optional: Download Manifesto
    st.header("Download Sneha's Campaign poster")
    manifesto_url = "https://drive.google.com/file/d/1kjTeuX1Bm8EKc8b8tMcGV7rxotWoHyJP/view?usp=sharing"
    st.markdown(f'[Click here to view my poster]({manifesto_url})', unsafe_allow_html=True)
    # Contact Section
    st.header("Get in Touch")
    st.markdown(f"**Email**: {CANDIDATE['contact']['Email']}")

    st.subheader("Follow Sneha on Social Media")
    social_links = ""
    for platform, link in CANDIDATE['contact']['Social Media'].items():
        if platform.lower() == "linkedin":
            icon = "https://cdn-icons-png.flaticon.com/512/174/174857.png"
        else:
            icon = ""
        social_links += f'<a href="{link}" target="_blank"><img src="{icon}" alt="{platform}" title="{platform}"></a>'
    st.markdown(f'<div class="social-icons">{social_links}</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()

