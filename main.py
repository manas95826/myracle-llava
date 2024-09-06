import gradio as gr
import base64
from PIL import Image
from groq import Groq
import os

client = Groq(api_key=os.environ.get('GROQ_API_KEY'))

def encode_images(image_paths):
    base64_images = []
    for image_path in image_paths:
        with open(image_path, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode("utf-8")
            base64_images.append(f"data:image/jpeg;base64,{base64_image}")
    return base64_images

def resize_images(image_paths, target_size=(224, 224)):
    resized_images = []
    for image_path in image_paths:
        img = Image.open(image_path)
        img_resized = img.resize(target_size) 
        resized_images.append(img_resized)
    return resized_images

def generate_testing_instructions(images, context):
    resized_images = resize_images(images)

    base64_images = encode_images(images)

    completion = client.chat.completions.create(
        model="llava-v1.5-7b-4096-preview",
        messages=[
        {
            "role": "user",
            "content": [
                {"type": "image_url", "image_url": {"url": base64_image}},
                {"type": "text", "text": '''
You're a helpful assistant that creates comprehensive testing instructions. Based on the screenshot of app interface you should tell:

- **Description**: A brief explanation of the feature being tested.
- **Pre-conditions**: The required setup or state of the app before beginning the test.
- **Testing Steps**: A clear, step-by-step guide for performing the test, including any user interactions or actions.
- **Expected Result**: The outcome you should observe if the feature is functioning correctly.

Please demonstrate your approach using the following features of a mobile app:

1. **Source, Destination, and Date Selection**: The user selects their departure location, destination, and the travel date.
2. **Bus Selection**: Displays a list of available buses, allowing the user to choose a specific one.
3. **Seat Selection**: Enables the user to select seats on the chosen bus.
4. **Pick-up and Drop-off Point Selection**: Allows the user to specify the starting point and final stop for the trip.
5. **Offers**: Showcases available promotions and discounts.
6. **Filters**: Options to filter buses by time, price, or other preferences.
7. **Bus Information**: Provides details about the selected bus, including amenities, photos, and reviews.

'''},
                {"type": "text", "text": context}
            ]
        }
        for base64_image in base64_images
    ],
    temperature=0,
    max_tokens=1024,
    top_p=1,
    stream=False,
    stop=None,
)
    return completion.choices[0].message.content

with gr.Blocks() as demo:
    gr.Markdown("## 🚌 Red Bus App Testing Instructions Generator")

    with gr.Row():
        context = gr.Textbox(label="Optional Context", placeholder="Add any specific instructions or questions...")

    image_upload = gr.File(label="Upload Screenshots (PNG or JPG)", type="filepath", file_count="multiple")

    output = gr.Textbox(label="Generated Testing Instructions", placeholder="The instructions will appear here...")

    button = gr.Button("Describe Testing Instructions")

    button.click(
        generate_testing_instructions,
        inputs=[image_upload, context],
        outputs=output
    )

demo.launch(debug=True)
