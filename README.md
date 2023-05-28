## Test Label Studio

Label Studio is an open source data labeling tool. It lets you label data types like audio, text, images, videos, and time series with a simple and straightforward UI and export to various model formats. It can be used to prepare raw data or improve existing training data to get more accurate ML models.

This project is used for testing the Label Studio application. Group 9 use Selenium to test the basic functionalities and use Allure to generate reports.

#### Install locally with Docker

Group 09 Label Studio docker image is [here](https://hub.docker.com/repository/docker/duyendu/group_09_label_studio).

```bash
# You can pull this docker repository
docker pull duyendu/group_09_label_studio

# Run this image after install
docker run -it -p 8080:8080 duyendu/group_09_label_studio
```

#### Build a local image with Docker

```bash
# Download zip or git clone source code
pip clone "https://github.com/duyendumy/Nhom9_LabelStudio.git"

# To Build a local image, run:
docker-compose build

# List docker images, run:
docker images

# Run this image after install
docker run -it -p 8080:8080 duyendu/group09_label_studio
```

#### Deploy in a cloud instance

We deploy this app to AWS Academy using Elastic Beanstalk service.
This is domain [here](http://testlabelstudio.us-east-1.elasticbeanstalk.com/)
