# Signature Detection Flask App

This is a simple Flask web application for signature detection using a pre-trained deep learning model. Users can upload an image, and the application will determine whether a signature is present in the image or not.

## Prerequisites

Before running this application, make sure you have the following dependencies installed:

- Python 3.x
- Flask
- OpenCV (cv2)
- NumPy
- Keras (with a pre-trained signature detection model)
- HTML/CSS for web templates

You can install Python dependencies using `pip`:

```bash
pip install flask opencv-python-headless numpy keras

```
**Customization:**
You can customize this application for your specific needs:

- **Modify the model:** Replace signature_detection_model.h5 with your trained model for signature detection.

- **Adjust the image preprocessing:** Modify the preprocess_image function in app.py to match your model's input requirements.

- **Update the HTML templates:** Customize the index.html and results.html templates to match your application's branding and user interface.

- **Tune the confidence threshold:** In app.py, you can change the confidence threshold (0.5 by default) to control when the application classifies an image as having a signature or not.

  ## Shots:

  ![Screenshot (292)](https://github.com/RohitBhandare/custom-ml-model-signature-detection/assets/92716110/1556ac9c-2ed3-4a8b-97e4-2e66442ce0a1)
  ![Screenshot (293)](https://github.com/RohitBhandare/custom-ml-model-signature-detection/assets/92716110/5ae24399-480f-4356-a7b5-1e0f6d4a721e)
![Screenshot (294)](https://github.com/RohitBhandare/custom-ml-model-signature-detection/assets/92716110/963d5adf-5f2c-4720-a6a6-951d76a22117)
