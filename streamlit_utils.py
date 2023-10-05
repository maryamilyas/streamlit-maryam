import streamlit as st

def set_svg_background_image(svg_path):
    """
    Set an SVG file as the background image for the Streamlit app.
    """
    background_css = f"""
    <style>
    body {{
        background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%"><rect width="100%" height="100%" fill="your-color" /><image xlink:href="{svg_path}" width="100%" height="100%" /></svg>');
        background-size: cover;
    }}
    </style>
    """

    st.markdown(background_css, unsafe_allow_html=True)

def add_tooltip_to_subheader(subheader_text, tooltip_text):
    """
    Adds a tooltip to a Streamlit subheader.

    Parameters:
    subheader_text (str): The text to display in the subheader.
    tooltip_text (str): The text to display in the tooltip.

    Returns:
    None
    """
    tooltip_html = f'<span class="tooltip">{subheader_text}<span class="tooltiptext">{tooltip_text}</span></span>'
    tooltip_css = """
    <style>
        .tooltip {
            position: relative;
            display: inline-block;
        }

        .tooltiptext {
            visibility: hidden;
            width: max-content;
            background-color: #333;
            color: #fff;
            text-align: center;
            border-radius: 6px;
            padding: 5px;
            position: absolute;
            z-index: 1;
            bottom: 125%;
            left: 50%;
            transform: translateX(-50%);
            opacity: 0;
            transition: opacity 0.3s;
        }

        .tooltip:hover .tooltiptext {
            visibility: visible;
            opacity: 1;
        }
    </style>
    """

    st.markdown(tooltip_css, unsafe_allow_html=True)
    st.markdown(tooltip_html, unsafe_allow_html=True)