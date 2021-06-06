import re
from io import StringIO
import streamlit as st

def get_md_contensts():
    uploaded_file = st.sidebar.file_uploader("upload a markdown file")
    if uploaded_file is not None:
        title = uploaded_file.name
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        string_data = stringio.readlines()
        return title, string_data 

def display(title, clean_data):
    st.title(title.replace('.md',''))
    st.markdown('---')
    for para in clean_data:
        if para.startswith("#"):
            st.subheader(para.replace("#","").strip())
            #st.markdown(para)
        else:
            st.markdown(para)
    st.markdown('---')

def get_clean_data(data, pat, rep):
    clean_data = []
    for i in data:
        if len(i) != 0:
            clean_data.append(re.sub(pattern=pat, repl=rep, string=i))
    clean_data = [i for i in clean_data if len(i) >=3]
    return clean_data

# --------

try :
    #--- sidebar instructions ---
    st.sidebar.markdown("### This app display a markdown file makde with \nMarkDownload - Markdown Web Clipper")
    st.sidebar.markdown("---")
    data = False 
    title, data = get_md_contensts()
    if data:
        pat = '(\[.+\)*\[\\\\.*\))'
        repl = ''
        nct = get_clean_data(data, pat, repl)
        for e,Z in enumerate(nct):
            if Z.startswith("#"):
                print(f"{e} : {Z}")
    #--- display markdown contents ---
        display(title, nct)
        st.sidebar.markdown("---")
        st.sidebar.markdown("_This will save the file wherever the script is running_")
        check = st.sidebar.button("Save the clean markdown file")
        if check:
            try:
                with open(title.replace(' ', '_').replace('.md', '_cleaned.md'), 'w') as ofh:
                    for i in nct:
                        ofh.writelines(i+"\n")
                st.sidebar.write("File Saved")
            except:
                st.sidebar.write("Couldn't Save")
    else :
        st.markdown("damn")
except :
    #--- instructions ---
    st.markdown("""- This app display the markdown file made with [MarkDownload - Markdown Web Clipper](https://chrome.google.com/webstore/detail/markdownload-markdown-web/pcmpcfapbekmbjjkdalcgopdkipoggdi?hl=en-GB)""")
    st.markdown("""- MarkDownload doesn't parse the scientific article the way I want, so this app cleans the markdown files made by the webclipper. The cleaned markdown file can be saved or use for making notes in Obsidian or to pass it through speachify.""")
    st.markdown("---")
    pass


