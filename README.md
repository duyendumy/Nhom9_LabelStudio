## What is Label Studio?

Label Studio is an open source data labeling tool. It lets you label data types like audio, text, images, videos, and time series with a simple and straightforward UI and export to various model formats. It can be used to prepare raw data or improve existing training data to get more accurate ML models.

This project is used for testing the Label Studio application. Group 9 use Selenium to test the basic functionalities and use Allure to generate reports.

#### Build a local image with Docker

```bash
# Dowload zip or git clone source code
pip clone "https://github.com/duyendumy/Nhom9_LabelStudio.git"

# To Build a local image, run
docker build -t username/label-studio:latest .
```
