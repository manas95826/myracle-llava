# Myracle-llava

This repository contains code to generate comprehensive testing instructions for the **Red Bus** mobile app using screenshots of the app interface. The project leverages **Groq** and **Gradio** to handle image processing and generate detailed testing instructions with AI. The code works with images to create precise, step-by-step testing guidance for key app features such as seat selection, bus filters, and offers.

## Features
- **Image Upload and Processing**: Upload screenshots of the app and resize them to a target resolution.
- **AI-Powered Testing Instruction Generation**: Using the Groq API with the llava-v1.5-7b-4096-preview model, the system creates testing instructions for app features.
- **Key App Features Supported**:
  - Source, Destination, and Date Selection
  - Bus Selection
  - Seat Selection
  - Pick-up and Drop-off Point Selection
  - Offers and Promotions
  - Filters for Time, Price, and Preferences
  - Detailed Bus Information
 
![image](https://github.com/user-attachments/assets/7a164c94-6a72-49ca-b52a-91c05d964a04)

  
## How it Works
1. Upload app screenshots.
2. Provide optional context to refine the AI output.
3. The AI analyzes the images and returns a set of testing instructions for the app features visible in the screenshots.

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/manas95826/myracle-llava.git
   cd myracle-llava
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the **Groq** API:
   - Create a Groq account and get your API key.
   - Set your API key in the environment:
     ```bash
     export GROQ_API_KEY='your-api-key'
     ```

4. Run the app:
   ```bash
   python main.py
   ```

## Usage
Once the app is running, open the Gradio interface in your browser. Upload screenshots of the Red Bus app, provide optional context, and click "Describe Testing Instructions" to generate AI-powered instructions.

## File Structure
- **main.py**: Core script to handle image uploads, resizing, and testing instruction generation.
- **requirements.txt**: Contains all required libraries (Gradio, Pillow, Groq).
  
## Future Enhancements
- Support for additional languages for testing instructions.
- Improved image processing with more formats and higher resolution handling.
