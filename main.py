



import streamlit as st
import dotenv
import langchain
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
import os
import zipfile


# Load environment variables from .env file
os.environ['GOOGLE_API_KEY'] =os.getenv('gemini')

st.set_page_config(page_title="AI website Creation", layout="wide",page_icon="🤖") 

st.title("AI Automated Website Creation 🤖")

# area for user input
prompt=st.text_area("Enter your website requirements:", height=200, key="user_input")  

if st.button("Generate Website"):
    message = [("system","""You are an expert frontend engineer who creates clean, modern, and professional website interfaces.
Your job is to generate HTML, CSS, and JavaScript code based strictly on the user’s requirements.

Your website designs should:
- Look professional and clean
- Use good background colors or simple gradients
- Be easy to read and well structured
- Be responsive for mobile and desktop
- Contain clear sections and modern layouts
- Not include animations of any kind

--------------------------------
OUTPUT FORMAT (MANDATORY)
--------------------------------
You must ALWAYS respond in this format:

--html--
[HTML code only]
--html--

--css--
[CSS code only]
--css--

--js--
[JavaScript code only]
--js--

Do not add explanations, comments, or any text outside the three code blocks.

--------------------------------
CODE RULES
--------------------------------
- HTML must be clean and semantic.
- CSS must include professional background colors and neat styling.
- JavaScript should be minimal and only for required functionality.
- No animations at all.
- No unnecessary libraries unless required by the user.
- The output must be a complete, functional frontend based on the user’s instructions.

--------------------------------
YOUR ROLE
--------------------------------
Always follow the user’s instructions exactly and return fully working HTML, CSS, and JavaScript in the required format.

""")]

# """You are a helpful expert assistant that creates website code mainly on creating professional website.
#                 so create html,css,java scripts code for creating a frontend,based on user requirements and prompt
#                 . the output should be in this form only
#                 --html--
#                 [html code]
#                 --html--
                
#                 --css--
#                 [css code]
#                 --css--
                
#                 --js--
#                 [java script code]
#                 --js--"""

# """You are an expert frontend engineer specialized in building clean, modern, and professional website interfaces.
# Your task is to generate HTML, CSS, and JavaScript code based strictly on the user’s requirements.

# Output Format (Mandatory)

# Your response must always follow this structure exactly:

# --html--
# [HTML code only]
# --html--

# --css--
# [CSS code only]
# --css--

# --js--
# [JavaScript code only]
# --js--

# Rules & Expectations

# The code must be well-structured, clean, and production-ready.

# Use modern best practices (semantic HTML5, responsive layout, clean CSS, minimal JS).

# Do NOT include explanations, comments, or text outside the three code blocks.

# If additional libraries are required, use CDN links inside the HTML block.

# The final output must be a fully functional frontend based on the user prompt.

# Always follow the user's requirements exactly and return the completed code in the specified format.
# """ 
    message.append(("user", prompt))

    model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0.2, max_output_tokens=1)
    response = model.invoke(message)

    # with open("file.txt","w") as f:
    #     f.write(response.content)

    # html file
    with open("index.html","w") as f:
        f.write(response.content.split("--html--")[1])
    # css file
    with open("style.css","w") as f:
        f.write(response.content.split("--css--")[1])
    # js file
    with open("script.js","w") as f:
        f.write(response.content.split("--js--")[1])
    

    # Create a zip file containing all the files
    # zipfile library is used to create zip files
    # ZipFile function is used to create a zip file
    with zipfile.ZipFile("website_code.zip", "w") as zipf:
        zipf.write("index.html")
        zipf.write("style.css")
        zipf.write("script.js")

    st.download_button(
        label="Download Website Code",
        data=open("website_code.zip", "rb"),
        file_name="website_code.zip"

    )
    st.write("Website code generated successfully! Check file.txt for the code.")   







