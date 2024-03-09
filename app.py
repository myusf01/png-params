import gradio as gr
from PIL import Image
from urllib.request import Request, urlopen

def display_image_from_url(url, input_image):
    if url == '' and input_image is None:
        return None, "", ""

    image = None
    if url != '':
        req = Request(
            url=url, 
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        res = urlopen(req)
        image = Image.open(res)
        image.load()

    if input_image is not None:
        image = input_image

    parameters = "Parameters have been erased from this image or unsupported format"
    if 'parameters' in image.info:
        parameters = image.info['parameters']

    return image, parameters, image.info

# Define the interface
iface = gr.Interface(
    fn=display_image_from_url,
    inputs=[
        gr.Textbox(label="Source URL"),
        gr.Image(label="Source Image", type='pil')
    ],
    outputs=[
        gr.Image(type='pil', label="Output Image"),
        gr.Textbox(label="Generation Parameters"),
        gr.Textbox(label="Metadata")
    ],
    title="Image Display from URL",
    description="Enter a URL or upload an image to display its parameters and metadata."
)

# Launch the interface
iface.launch()
